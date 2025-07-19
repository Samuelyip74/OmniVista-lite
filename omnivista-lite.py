# omnivista-lite.py

"""
# OmniVista Lite

OmniVista Lite is a lightweight Network Management System (NMS) written in Python using PySide6 for GUI and aos8-api for OmniSwitch device integration. 
It supports network device inventory management, online status monitoring, backup scheduling, syslog collection, and alerting.

## Features
- Device inventory (OmniSwitch, Stellar AP, third-party)
- Status monitoring (via ping)
- Syslog listener and dashboard
- Configuration backup (OmniSwitch)
- Email alerting and daily status report
- GUI built with PySide6

## Modules
- GUI: `gui/ui/nmslite_ui.py`
- API: `aos8_api.ApiBuilder`
- DB: `SQLite`
- Automation: `QTimer`, `threading`
- Web access: `selenium`
- Email: `smtplib`
"""

# Imports: standard, third-party, and internal

import re
import os
import sys
import logging
import socket
import threading
import sqlite3
import glob
import shutil
import subprocess
import platform
from email.message import EmailMessage
import smtplib
from datetime import datetime, timedelta
import ipaddress
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.remote_connection import LOGGER
from aos8_api.ApiBuilder import AosApiClientBuilder
from PySide6.QtCore import QThread, Signal, QObject, QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QHeaderView,QAbstractItemView, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from gui.ui.nmslite_ui import Ui_nmslite

# Logging config
LOGGER.setLevel(logging.WARNING)

# Global paths and directories
APP_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))  # works for .exe or .py
BACKUP_DIR = os.path.join(APP_DIR, "backup")
LOG_DIR = os.path.join(APP_DIR, "logs")
DB_PATH = os.path.join(APP_DIR, "devices.db")
SYSLOG_FILE = os.path.join(LOG_DIR, "syslog")

# Ensure directories exist
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Utility Functions
def is_valid_ip(ip):
    """Check if an IP string is valid."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_email(email):
    """Validate email format."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_email_list(email_string):
    """Check all emails in a comma-separated string.

    Args:
        email_string (str): Comma-separated emails

    Returns:
        List[str]: Invalid email addresses
    """
    emails = [e.strip() for e in email_string.split(',')]
    invalid = [e for e in emails if not is_valid_email(e)]
    return invalid

def is_valid_fqdn(fqdn):
    """Validate FQDN format.

    Args:
        fqdn (str): Fully qualified domain name

    Returns:
        bool: True if valid, else False
    """
    pattern = r"^(?=.{1,253}$)(?:[a-zA-Z0-9](?:[-a-zA-Z0-9]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
    return re.match(pattern, fqdn) is not None

def resource_path(relative_path):
    """
    Get absolute path to a resource, compatible with PyInstaller.

    Args:
        relative_path (str): Relative file path

    Returns:
        str: Absolute path
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class OmniVistaLite(QMainWindow):
    """
    Main application class for the OmniVista Lite Network Management System.

    This GUI-based system enables users to manage network devices such as OmniSwitches,
    monitor their online/offline status, configure alerting and email reporting, backup
    configuration data, and collect syslog events from devices.

    Inherits from:
        QMainWindow (PySide6)

    Attributes:
        db (sqlite3.Connection): SQLite database connection
        ui (Ui_nmslite): GUI object
        devices (list): Cached list of devices
    """
    def __init__(self):
        super().__init__()
        self.devices = []
        self.current_client = None
        self.backup_ran_today = False
        self.ui = Ui_nmslite()
        self.ui.setupUi(self)

        # Set window icon and logo
        self.setWindowIcon(QIcon(resource_path("assets/logo-small.jpg")))
        self.ui.logo.setPixmap(QPixmap(resource_path("assets/logo.png")))

        # Set up database
        self.db = sqlite3.connect(DB_PATH)
        self.init_db()

        # Connect buttons
        self.ui.MainTabWidget.currentChanged.connect(self.on_tab_changed)
        self.ui.t2_new_btn.clicked.connect(self.clear_fields)
        self.ui.t2_add_update_btn.clicked.connect(self.add_or_update_device)
        self.ui.t2_delete_btn.clicked.connect(self.delete_device)
        self.ui.t2_manage_btn.clicked.connect(self.manage_device)
        self.ui.t2_inventory_table.cellClicked.connect(self.select_device)
        self.ui.t3_refresh_btn.clicked.connect(self.refresh_syslog_messages)
        self.ui.t4_save_btn.clicked.connect(self.save_settings)
        self.ui.t4_test_btn.clicked.connect(self.test_email_settings)

        self.check_all_devices_status_async() 

        # Check devices health every 5 minutes
        self.ping_timer = QTimer(self)
        self.ping_timer.timeout.connect(self.check_all_devices_status_async)
        self.ping_timer.start(5 * 60 * 1000) 

        # Poll devices data every 3 hours
        self.poll_timer = QTimer(self)
        self.poll_timer.timeout.connect(self.poll_devices)
        self.poll_timer.start(1 * 60 * 60 * 1000) 

        # Schedule midnight tasks
        self.schedule_midnight_tasks()    

        # Start Syslog Service
        self.start_syslog_listener()

        # Initialized data
        self.ui.MainTabWidget.setCurrentIndex(0)
        self.load_dashboard()

    def init_db(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS devices (
                ip TEXT PRIMARY KEY,
                name TEXT,
                username TEXT,
                password TEXT,
                type TEXT,
                model TEXT,
                sw_version TEXT,
                is_alive INTEGER,
                last_alive TEXT,
                backup_status TEXT,
                last_check TEXT,
                last_alert_status TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                mail_server TEXT,
                port TEXT,
                protocol TEXT,
                username TEXT,
                password TEXT,
                from_addr TEXT,
                recipients TEXT,
                retain_days INTEGER,
                daily_report INTEGER  -- 0=False, 1=True
            )
        ''')

        cursor.execute("SELECT COUNT(*) FROM settings")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO settings (
                    id, mail_server, port, protocol, username, password, from_addr,
                    recipients, retain_days, daily_report
                ) VALUES (1, '', '', 'SSL', '', '', '', '', 7, 0)
            ''')    

        self.db.commit()

    def load_settings(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM settings WHERE id = 1")
        row = cursor.fetchone()
        if not row:
            return

        (
            _id, mail_server, port, protocol, username, password,
            from_addr, recipients, retain_days, daily_report
        ) = row

        self.ui.t4_mail_server.setText(mail_server)
        self.ui.t4_mail_server_port.setText(port)
        self.ui.t4_username.setText(username)
        self.ui.t4_password.setText(password)
        self.ui.t4_from.setText(from_addr)
        self.ui.t4_recipients.setText(recipients)
        self.ui.t4_backup_days.setText(str(retain_days))

        self.ui.t4_ssl_radio.setChecked(protocol == "SSL")
        self.ui.t4_tls_radio.setChecked(protocol == "TLS")

        self.ui.t4_backup_report_yes.setChecked(daily_report == 1)
        self.ui.t4_backup_report_no.setChecked(daily_report == 0)

    def save_settings(self):
        protocol = "SSL" if self.ui.t4_ssl_radio.isChecked() else "TLS"
        daily_report = 1 if self.ui.t4_backup_report_yes.isChecked() else 0

        mail_server = self.ui.t4_mail_server.text()
        if not is_valid_fqdn(mail_server):
            QMessageBox.warning(self, "Error", "Mail Server validation failed!")
            self.ui.t4_mail_server.clear()
            return  
        
        mail_server_port = self.ui.t4_mail_server_port.text()
        if not mail_server_port.isdigit():
            QMessageBox.warning(self, "Error", "Port validation failed!")
            self.ui.t4_mail_server_port.clear()
            return  
        
        username = self.ui.t4_username.text()
        if not is_valid_email(username):
            QMessageBox.warning(self, "Error", "Username validation failed!")
            self.ui.t4_username.clear()
            return  
        
        from_email = self.ui.t4_from.text()
        if not is_valid_email(from_email):
            QMessageBox.warning(self, "Error", "From Email validation failed!")
            self.ui.t4_from.clear()
            return   
             
        to_recipients = self.ui.t4_recipients.text()
        if validate_email_list(to_recipients):
            QMessageBox.warning(self, "Error", "Recipients Email validation failed!")
            self.ui.t4_recipients.clear()
            return       

        backup_in_days = self.ui.t4_backup_days.text()
        if not backup_in_days.isdigit():
            QMessageBox.warning(self, "Error", "Backup input validation failed!")
            self.ui.t4_backup_days.clear()
            return             


        cursor = self.db.cursor()
        cursor.execute('''
            UPDATE settings SET
                mail_server = ?,
                port = ?,
                protocol = ?,
                username = ?,
                password = ?,
                from_addr = ?,
                recipients = ?,
                retain_days = ?,
                daily_report = ?
            WHERE id = 1
        ''', (
            mail_server,
            mail_server_port,
            protocol,
            username,
            self.ui.t4_password.text(),
            from_email,
            to_recipients,
            int(backup_in_days or 0),
            daily_report
        ))
        self.db.commit()
        self.show_auto_dismiss_message("Success", f"Setting saved")

    def start_syslog_listener(self, port=514, output_file=SYSLOG_FILE):
        def listen():
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                try:
                    sock.bind(("", port))
                    # print(f"[Syslog] Listening on UDP port {port}...")
                    with open(output_file, "a", encoding="utf-8") as logfile:
                        while True:
                            data, addr = sock.recvfrom(4096)
                            message = data.decode(errors="ignore").strip()
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            log_entry = f"{timestamp} [{addr[0]}] {message}\n"
                            logfile.write(log_entry)
                            logfile.flush()
                            print(log_entry, end="")  # optional
                except PermissionError:
                    print(f"[Syslog] Permission denied: UDP port {port} requires admin privileges.")
                except Exception as e:
                    print(f"[Syslog] Error: {e}")

        # Run listener in a background thread
        thread = threading.Thread(target=listen, daemon=True)
        thread.start()        


    def load_syslog_messages(self, logfile=SYSLOG_FILE):
        self.ui.t3_major_alerts_table.clear()
        self.ui.t3_medium_alerts_table.clear()
        self.ui.t3_minor_alerts_table.clear()

        try:
            with open(logfile, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    msg = line
                    severity = None

                    # 1. Match classic <PRI> style
                    pri_match = re.match(r"<(\d+)>(.*)", line)
                    if pri_match:
                        pri = int(pri_match.group(1))
                        msg = pri_match.group(2)
                        severity = pri & 0x07

                    else:
                        # 2. Match your format, e.g. "(E 746530)" or "(N 1234)"
                        level_match = re.search(r"\(([A-Z])\s+\d+\)", line)
                        if level_match:
                            code = level_match.group(1).upper()
                            severity_map = {
                                "E": 0,  # Emergency / Error
                                "W": 4,  # Warning
                                "N": 5,  # Notice / Info
                                "D": 7,  # Debug
                            }
                            severity = severity_map.get(code)

                    # Show in correct text area
                    if severity in (0, 1, 2):
                        self.ui.t3_major_alerts_table.appendPlainText(msg)
                    elif severity in (3, 4):
                        self.ui.t3_medium_alerts_table.appendPlainText(msg)
                    elif severity in (5, 6, 7):
                        self.ui.t3_minor_alerts_table.appendPlainText(msg)
                    else:
                        self.ui.t3_minor_alerts_table.appendPlainText(msg)

        except FileNotFoundError:
            print(f"[Syslog] File {logfile} not found.")

    def load_critical_alerts(self, logfile=SYSLOG_FILE):
        self.ui.t1_syslog_alerts.clear()

        try:
            with open(logfile, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    msg = line
                    severity = None

                    # 1. Match classic <PRI> style
                    pri_match = re.match(r"<(\d+)>(.*)", line)
                    if pri_match:
                        pri = int(pri_match.group(1))
                        msg = pri_match.group(2)
                        severity = pri & 0x07

                    else:
                        # 2. Match your format, e.g. "(E 746530)" or "(N 1234)"
                        level_match = re.search(r"\(([A-Z])\s+\d+\)", line)
                        if level_match:
                            code = level_match.group(1).upper()
                            severity_map = {
                                "E": 0,  # Emergency / Error
                                "W": 4,  # Warning
                                "N": 5,  # Notice / Info
                                "D": 7,  # Debug
                            }
                            severity = severity_map.get(code)

                    # Show in correct text area
                    if severity in (0, 1, 2):
                        self.ui.t1_syslog_alerts.appendPlainText(msg)

        except FileNotFoundError:
            print(f"[Syslog] File {logfile} not found.")

    def refresh_syslog_messages(self):
        self.load_syslog_messages()  

    def refresh_syslog_messages(self):
        self.load_syslog_messages()

    def on_tab_changed(self, index):
        if index == 0:
            self.load_dashboard()
        if index == 1:
            self.load_devices()  
            self.clear_fields()  
        if index == 2:
            self.load_syslog_messages()   
        if index == 3:
            self.load_settings() 

    def clear_fields(self):
        self.ui.t2_i_ip_address.clear()
        self.ui.t2_i_ip_address.setDisabled(False)
        self.ui.t2_inventory_table.clearSelection()
        self.ui.t2_i_username.clear()
        self.ui.t2_i_password.clear()
        self.ui.t2_omniswitch_radio.setAutoExclusive(False)
        self.ui.t2_stellar_radio.setAutoExclusive(False)
        self.ui.t2_third_party_radio.setAutoExclusive(False)
        self.ui.t2_omniswitch_radio.setChecked(False)
        self.ui.t2_stellar_radio.setChecked(False)
        self.ui.t2_third_party_radio.setChecked(False)
        self.ui.t2_omniswitch_radio.setAutoExclusive(True)
        self.ui.t2_stellar_radio.setAutoExclusive(True)
        self.ui.t2_third_party_radio.setAutoExclusive(True)

    def add_or_update_device(self):
        ip = self.ui.t2_i_ip_address.text().strip()

        if not is_valid_ip(ip):
            QMessageBox.warning(self, "Error", "Input validation failed!")
            self.ui.t2_i_ip_address.clear()
            return

        username = self.ui.t2_i_username.text().strip()
        password = self.ui.t2_i_password.text().strip()

        if self.ui.t2_omniswitch_radio.isChecked():
            dev_type = "OmniSwitch"
        elif self.ui.t2_stellar_radio.isChecked():
            dev_type = "Stellar AP"
        elif self.ui.t2_third_party_radio.isChecked():
            dev_type = "Third Party"
        else:
            dev_type = "Unknown"

        if not ip or not username or not password or dev_type == "Unknown":
            QMessageBox.warning(self, "Error", "Please complete all fields.")
            return

        cursor = self.db.cursor()

        # Check if device already exists
        cursor.execute("SELECT ip FROM devices WHERE ip=?", (ip,))
        exists = cursor.fetchone()

        if exists:
            # Only update known fields
            cursor.execute('''
                UPDATE devices SET
                    username = ?,
                    password = ?,
                    type = ?
                WHERE ip = ?
            ''', (username, password, dev_type, ip))
            print(f"Device {ip} updated.")
        else:
            # Insert known fields, leave others as NULL
            cursor.execute('''
                INSERT INTO devices (ip, username, password, type)
                VALUES (?, ?, ?, ?)
            ''', (ip, username, password, dev_type))
            self.show_auto_dismiss_message("Success", f"Device {ip} added.")

        self.db.commit()
        self.clear_fields()

        self.poll_device(ip, username, password, dev_type)        
        self.load_devices()

    def select_device(self, row, col):
        # Get real device data from memory
        device = self.devices[row]  # Same order as SELECT

        ip = device[4]
        username = device[9]
        password = device[10]
        dev_type = device[0]

        self.ui.t2_i_ip_address.setText(ip)
        self.ui.t2_i_ip_address.setDisabled(True)
        self.ui.t2_i_username.setText(username)
        self.ui.t2_i_password.setText(password)

        self.ui.t2_omniswitch_radio.setChecked(dev_type == "OmniSwitch")
        self.ui.t2_stellar_radio.setChecked(dev_type == "Stellar AP")
        self.ui.t2_third_party_radio.setChecked(dev_type == "Third Party")

        self.ui.t2_inventory_table.selectRow(row)     


    def load_devices(self):
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT type, name, model, sw_version, ip, 
                is_alive, last_alive, last_check, backup_status, username, 
                password
            FROM devices
        ''')
        rows = cursor.fetchall()
        self.devices = rows
        headers = [
            "Type", "Name", "Model", "Sw Version", "IP Address","IsAlive",
            "Last Known","Last Checked", "Backup", "Username", "Password"  
        ]

        table = self.ui.t2_inventory_table
        table.setRowCount(len(rows))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)


        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                if col_idx == 10:  # password
                    value = "••••••"
                if col_idx == 5:  # is_alive
                    value = "Online" if value == 1 else "Offline"
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  # 🔹 Center-align the text                    
                self.ui.t2_inventory_table.setItem(row_idx, col_idx, item)

        # Optional: Auto-fit columns
        self.ui.t2_inventory_table.verticalHeader().setVisible(False)
        header = table.horizontalHeader()
        for col in range(table.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)          

    def load_offline_devices(self):
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT type, name, model, sw_version, ip, 
                is_alive, last_alive, last_check, backup_status, username, 
                password
            FROM devices
            WHERE is_alive = 0 OR is_alive IS NULL
        ''')
        rows = cursor.fetchall()
        self.devices = rows
        headers = [
            "Type", "Name", "Model", "Sw Version", "IP Address","IsAlive",
            "Last Known","Last Checked", "Backup", "Username", "Password"  
        ]

        table = self.ui.t1_offline_table
        table.setRowCount(len(rows))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                if col_idx == 10:  # password
                    value = "••••••"
                if col_idx == 5:  # is_alive
                    value = "Online" if value == 1 else "Offline"
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  # 🔹 Center-align the text                       
                self.ui.t1_offline_table.setItem(row_idx, col_idx, item)

        # Optional: Auto-fit columns
        self.ui.t1_offline_table.verticalHeader().setVisible(False)
        header = table.horizontalHeader()
        for col in range(table.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)

    def delete_device(self):
        # Get the selected row
        table = self.ui.t2_inventory_table
        selected_row = table.currentRow()

        if selected_row < 0:
            print("No device selected.")
            return

        # Get the IP address from the stored device list
        device = self.devices[selected_row]
        ip = device[4]  # Column 1 in SELECT: IP address

        # 🔒 Show confirmation dialog
        confirm = QMessageBox.question(
            self,
            "Delete Confirmation",
            f"Are you sure you want to delete device {ip}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm != QMessageBox.Yes:
            return

        # Delete from database
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM devices WHERE ip = ?", (ip,))
        self.db.commit()

        # print(f"Device {ip} deleted.")
        
        # Refresh UI
        self.clear_fields()
        self.load_devices()

    def manage_device(self):
        # Get the selected row
        table = self.ui.t2_inventory_table
        selected_row = table.currentRow()

        if selected_row < 0:
            print("No device selected.")
            return

        # Get the IP address from the stored device list
        device = self.devices[selected_row]
        ip = device[4]  # Column 1 in SELECT: IP address
        username = device[9]
        password = device[10]
        dev_type = device[0]


        if not ip:
            print("No IP address found.")
            return  


        if dev_type == "OmniSwitch":
            options = Options()
            options.add_argument('--ignore-certificate-errors')  # 🔹 Ignore self-signed certs
            options.add_argument("--disable-infobars")
            service = Service(log_path=os.devnull)

            driver = webdriver.Chrome(service=service, options=options)
            driver.get(f"https://{ip}/#/login?goBack=%2Fdashboard")

            # 🔄 Wait for username field to load
            wait = WebDriverWait(driver, 10)

            wait.until(EC.presence_of_element_located((By.ID, "login_username-txt")))
            wait.until(EC.presence_of_element_located((By.ID, "login_password-txt")))
            wait.until(EC.element_to_be_clickable((By.ID, "login_login-btn")))

            # 🔐 Fill credentials
            driver.find_element(By.ID, "login_username-txt").send_keys(username)
            driver.find_element(By.ID, "login_password-txt").send_keys(password)
            driver.find_element(By.ID, "login_login-btn").click()

    def load_dashboard(self):   
        cursor = self.db.cursor()

        # Total devices
        cursor.execute("SELECT COUNT(*) FROM devices")
        total = cursor.fetchone()[0]

        # Online devices (is_alive = 1)
        cursor.execute("SELECT COUNT(*) FROM devices WHERE is_alive = 1")
        online = cursor.fetchone()[0]

        # Offline devices (is_alive = 0 OR NULL)
        cursor.execute("SELECT COUNT(*) FROM devices WHERE is_alive IS NULL OR is_alive = 0")
        offline = cursor.fetchone()[0]

        # Update UI
        self.ui.t1_d_manageddevices.setText(str(total))
        self.ui.t1_d_online.setText(str(online))
        self.ui.t1_d_offline.setText(str(offline))

        # Update Offline Table
        self.load_offline_devices()
        self.load_critical_alerts()



    def check_all_devices_status_async(self):
        # Get list of IPs
        cursor = self.db.cursor()
        cursor.execute("SELECT ip FROM devices")
        ips = [row[0] for row in cursor.fetchall()]

        # Set up thread
        self.thread = QThread()
        self.worker = PingWorker(ips)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.update_device_status)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(lambda: (
            self.load_devices(),
            self.load_dashboard(),
        ))

        self.thread.start()

    def update_device_status(self, ip, is_alive, timestamp):
        cursor = self.db.cursor()
        cursor.execute("SELECT is_alive, last_alert_status, name FROM devices WHERE ip = ?", (ip,))
        row = cursor.fetchone()
        if not row:
            return
        prev_is_alive, last_alert_status, name = row
        name = name or ip  # fallback

        alert_triggered = False
        alert_recovered = False

        if is_alive and last_alert_status == "Down":
            # Recovery
            alert_recovered = True
            new_alert_status = "Up"
        elif not is_alive and last_alert_status != "Down":
            # Failure
            alert_triggered = True
            new_alert_status = "Down"
        else:
            new_alert_status = last_alert_status  # no change

        if is_alive:
            cursor.execute('''
                UPDATE devices SET
                    is_alive = 1,
                    last_alive = ?,
                    last_check = ?,
                    last_alert_status = ?
                WHERE ip = ?
            ''', (timestamp, timestamp, new_alert_status, ip))
        else:
            cursor.execute('''
                UPDATE devices SET
                    is_alive = 0,
                    last_check = ?,
                    last_alert_status = ?
                WHERE ip = ?
            ''', (timestamp, new_alert_status, ip))

        self.db.commit()

        if alert_triggered:
            self.send_device_alert(ip, name, up=False)
        elif alert_recovered:
            self.send_device_alert(ip, name, up=True)

    def poll_device(self, ip, username, password, dev_type):
        # print("Polling device for inventory update...")
        cursor = self.db.cursor()
        
        name = None
        model = None
        version = None
        is_alive = 0
        client = None

        try:
            if dev_type == "OmniSwitch":
                baseURL = f"https://{ip}"                 
                client = (
                    AosApiClientBuilder()
                    .setBaseUrl(baseURL)
                    .setUsername(username)
                    .setPassword(password)
                    .build()
                )
                result = client.system.getSystemInformation()
                if result.success:
                    name = result.data["rows"]["sysName"]
                    sysDescr = result.data["rows"]["sysDescr"]
                    match = re.search(r"(OS\d{4,5}[A-Z]?-P\d+)\s+(\d+\.\d+\.\d+\.R\d+)", sysDescr)
                    if match:
                        model = match.group(1)
                        version = match.group(2)
                    is_alive = 1
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            elif dev_type in ("Stellar AP", "Third Party"):
                # TODO: Add polling logic for those types
                pass
            else:
                print(f"[{ip}] Unknown device type: {dev_type}")
                return  # Exit early

            cursor.execute('''
                UPDATE devices SET
                    sw_version = ?,
                    model = ?,
                    is_alive = ?,
                    last_alive = ?,
                    name = ?,
                    last_check = ?
                WHERE ip = ?
            ''', (version, model, is_alive, now, name, now, ip))
            self.db.commit()
            # print(f"[{ip}] Inventory updated.")

        except Exception as e:
            print(f"[{ip}] Polling failed: {e}")

        finally:
            if client:
                client.close()
      

    def poll_devices(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT ip, username, password, type FROM devices")
        devices = cursor.fetchall()

        for ip, username, password, dev_type in devices:
            try:
                if dev_type == "OmniSwitch":
                    baseURL = f"https://{ip}"                 
                    client = (
                        AosApiClientBuilder()
                        .setBaseUrl(baseURL)
                        .setUsername(username)
                        .setPassword(password)
                        .build()
                    )
                    result = client.system.getSystemInformation()
                    if result.success:
                        name = result.data["rows"]["sysName"]
                        sysDescr = result.data["rows"]["sysDescr"]
                        match = re.search(r"(OS\d{4,5}[A-Z]?-P\d+)\s+(\d+\.\d+\.\d+\.R\d+)", sysDescr)
                        if match:
                            model = match.group(1)
                            version = match.group(2)
                    client.close()
                elif dev_type in ("Stellar AP", "Third Party"):
                    pass
                    # Replace this with actual API endpoint for those devices

                else:
                    # print(f"[{ip}] Unknown device type: {dev_type}")
                    continue

                cursor.execute('''
                    UPDATE devices SET
                        sw_version = ?,
                        model = ?,
                        name = ?
                    WHERE ip = ?
                ''', (version, model, name, ip))
                self.db.commit()
                # print(f"[{ip}] Inventory updated.")

            except Exception as e:
                print(f"[{ip}] Polling failed: {e}")   

    def send_device_alert(self, ip, name, up=True):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM settings WHERE id = 1")
        row = cursor.fetchone()
        if not row:
            return

        (
            _id, mail_server, port, protocol, username, password,
            from_addr, recipients, retain_days, daily_report
        ) = row

        if not all([mail_server, port, protocol, username, password, from_addr, recipients]):
            # print(f"Email alert not sent: Incomplete settings.")
            return

        status = "RECOVERED" if up else "DOWN"
        subject = f"[ALERT] Device {name} ({ip}) is {status}"
        body = f"""
    Device Status Alert

    Device: {name}
    IP: {ip}
    Status: {status}
    Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """

        result = self.send_email(
            mail_server=mail_server,
            port=port,
            protocol=protocol,
            username=username,
            password=password,
            from_addr=from_addr,
            to_addrs=recipients,
            subject=subject,
            body=body
        )

        if result:
            pass
            # print(f"Email alert sent for {ip} ({status})")
        else:
            pass
            # print(f"Failed to send alert for {ip} ({status})")              

    def send_email(self, mail_server, port, protocol, username, password, from_addr, to_addrs, subject, body):
        msg = EmailMessage()
        msg["From"] = from_addr
        msg["To"] = to_addrs
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            if protocol == "SSL":
                server = smtplib.SMTP_SSL(mail_server, int(port))
            else:
                server = smtplib.SMTP(mail_server, int(port))
                server.starttls()

            server.login(username, password)
            server.send_message(msg)
            server.quit()
            return True

        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

    def test_email_settings(self):
        server = self.ui.t4_mail_server.text().strip()
        port = self.ui.t4_mail_server_port.text().strip()
        protocol = "SSL" if self.ui.t4_ssl_radio.isChecked() else "TLS"
        username = self.ui.t4_username.text().strip()
        password = self.ui.t4_password.text().strip()
        from_addr = self.ui.t4_from.text().strip()
        recipients = self.ui.t4_recipients.text().strip()

        if not all([server, port, username, password, from_addr, recipients]):
            QMessageBox.warning(self, "Incomplete", "Please fill in all required fields.")
            return

        subject = "NMS Test Email"
        body = "This is a test email from OmniVista Lite."

        result = self.send_email(
            mail_server=server,
            port=port,
            protocol=protocol,
            username=username,
            password=password,
            from_addr=from_addr,
            to_addrs=recipients,
            subject=subject,
            body=body
        )

        if result:
            QMessageBox.information(self, "Success", "Test email sent successfully.")
        else:
            QMessageBox.critical(self, "Failure", "Failed to send test email.")        

    def show_auto_dismiss_message(self, title: str, message: str, timeout=2000):
        try:
            timeout = int(timeout)  # Ensure timeout is an integer
            box = QMessageBox(self)
            box.setWindowTitle(title)
            box.setText(message)
            box.setIcon(QMessageBox.Information)
            box.setStandardButtons(QMessageBox.NoButton)  # Hide buttons
            QTimer.singleShot(timeout, lambda: box.accept())
            box.exec()
        except Exception as e:
            print(f"Failed to show auto-dismiss message: {e}")     

    def backup_configuration(self):
        from datetime import datetime
        cursor = self.db.cursor()

        cursor.execute("SELECT ip, username, password, type FROM devices WHERE is_alive = 1")
        devices = cursor.fetchall()

        for ip, username, password, dev_type in devices:
            status = "Failed"
            try:
                if dev_type == "OmniSwitch":
                    baseURL = f"https://{ip}"                 
                    client = (
                        AosApiClientBuilder()
                        .setBaseUrl(baseURL)
                        .setUsername(username)
                        .setPassword(password)
                        .build()
                    )
                    result = client.cli.sendCommand("show configuration snapshot")
                    if result.success:
                        # Create file with datetime + IP
                        now = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"{ip.replace('.', '_')}_{now}.cfg"
                        filepath = os.path.join(BACKUP_DIR, filename)

                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(result.output)                     
                        status = "Success"
                    client.close()
                elif dev_type in ("Stellar AP", "Third Party"):
                    status = "Unsupported"
                else:
                    status = "Unknown device type"

            except Exception as e:
                print(f"[{ip}] Backup failed: {e}")
                status = f"Error"

            # Update DB with backup result
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                UPDATE devices
                SET backup_status = ?, last_check = ?
                WHERE ip = ?
            ''', (status, now, ip))

        self.db.commit()

    def rotate_syslog_logs(self):

        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM settings WHERE id = 1")
        row = cursor.fetchone()
        if not row:
            return

        (
            _id, mail_server, port, protocol, username, password,
            from_addr, recipients, retain_days, daily_report
        ) = row
    
        today = datetime.now().strftime("%Y%m%d")
        rotated_name = f"syslog_{today}.log"
        rotated_path = os.path.join(LOG_DIR, rotated_name)
        active_log = SYSLOG_FILE

        # If current switch.log exists and is not today's rotated file
        if os.path.exists(active_log):
            shutil.move(active_log, rotated_path)

        # Cleanup old logs older than 7 days
        cutoff_date = datetime.now() - timedelta(days=int(retain_days))
        for file in glob.glob(os.path.join(LOG_DIR, "syslog_*.log")):
            basename = os.path.basename(file)
            date_part = basename.replace("syslog_", "").replace(".log", "")
            try:
                file_date = datetime.strptime(date_part, "%Y%m%d")
                if file_date < cutoff_date:
                    os.remove(file)
            except ValueError:
                continue       

    def schedule_midnight_tasks(self):
        now = datetime.now()
        next_midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        ms_until_midnight = int((next_midnight - now).total_seconds() * 1000)

        self.midnight_timer = QTimer(self)
        self.midnight_timer.setSingleShot(True)
        self.midnight_timer.timeout.connect(self.run_midnight_tasks)
        self.midnight_timer.start(ms_until_midnight)      

    def send_daily_status_report(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT COUNT(*) FROM devices")
        total = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM devices WHERE is_alive = 1")
        online = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM devices WHERE is_alive IS NULL OR is_alive = 0")
        offline = cursor.fetchone()[0]

        # Load settings
        cursor.execute("SELECT * FROM settings WHERE id = 1")
        row = cursor.fetchone()
        if not row:
            return

        (
            _id, mail_server, port, protocol, username, password,
            from_addr, recipients, retain_days, daily_report
        ) = row

        if daily_report != 1:
            print("Daily report disabled.")
            return

        if not all([mail_server, port, username, password, from_addr, recipients]):
            print("Missing email settings. Daily report skipped.")
            return

        subject = "Daily NMS Device Status Report"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = f"""NMS Daily Device Report
    ==========================
    Time: {now}

    Total devices: {total}
    Online devices: {online}
    Offline devices: {offline}

    This is an automated report from OmniVista Lite.
    """

        result = self.send_email(
            mail_server=mail_server,
            port=port,
            protocol=protocol,
            username=username,
            password=password,
            from_addr=from_addr,
            to_addrs=recipients,
            subject=subject,
            body=body
        )

        if result:
            print("[✓] Daily status report sent.")
        else:
            print("[✗] Failed to send daily status report.")


    def run_midnight_tasks(self):
        self.send_daily_status_report()
        self.backup_configuration()
        self.rotate_syslog_logs()
        self.schedule_midnight_tasks()  
                           


class PingWorker(QObject):
    """
    A background worker class to ping a list of devices asynchronously.

    Signals:
        finished (Signal): Emitted when pinging completes.
        progress (Signal): Emitted after each ping with (ip, is_alive, timestamp).

    Args:
        devices (list): List of IP addresses to ping
    """    
    finished = Signal()
    progress = Signal(str, bool, str)  # ip, is_alive, timestamp

    def __init__(self, devices):
        super().__init__()
        self.devices = devices

    def ping_device(self, ip):
        """
        Ping a single IP address to check if it is reachable.

        This method determines the current platform (Windows or Unix-based)
        and constructs the appropriate system ping command. It executes the
        command and returns whether the ping was successful.

        Args:
            ip (str): IP address to ping.

        Returns:
            bool: True if the device responds to ping, False otherwise.
        """        
        try:
            count = "1"
            timeout = "1000"
            if platform.system().lower() == "windows":
                cmd = ["ping", "-n", count, "-w", timeout, ip]
            else:
                cmd = ["ping", "-c", count, "-W", "1", ip]

            result = subprocess.run(cmd, stdout=subprocess.DEVNULL)
            return result.returncode == 0
        except Exception:
            return False

    def run(self):
        """
        Execute the ping operation for all devices in the background.

        Iterates through the list of devices and emits a `progress` signal
        for each device with its IP, online status, and current timestamp.
        Emits a `finished` signal when all devices have been processed.
        """        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for ip in self.devices:
            alive = self.ping_device(ip)
            self.progress.emit(ip, alive, now)

        self.finished.emit()        

# Entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OmniVistaLite()
    window.show()
    sys.exit(app.exec())
