# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nmslite.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_nmslite(object):
    def setupUi(self, nmslite):
        if not nmslite.objectName():
            nmslite.setObjectName(u"nmslite")
        nmslite.resize(808, 697)
        icon = QIcon()
        icon.addFile(u"../../../../assets/logo-small.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        nmslite.setWindowIcon(icon)
        self.centralwidget = QWidget(nmslite)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_23 = QGridLayout(self.centralwidget)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(130, 50))
        self.logo.setPixmap(QPixmap(u"../../../../assets/logo.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_23.addWidget(self.logo, 0, 0, 1, 1)

        self.MainTabWidget = QTabWidget(self.centralwidget)
        self.MainTabWidget.setObjectName(u"MainTabWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_13 = QGridLayout(self.dashboard)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.manageddevices = QGroupBox(self.dashboard)
        self.manageddevices.setObjectName(u"manageddevices")
        self.gridLayout_2 = QGridLayout(self.manageddevices)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.t1_d_manageddevices = QLabel(self.manageddevices)
        self.t1_d_manageddevices.setObjectName(u"t1_d_manageddevices")
        font = QFont()
        font.setPointSize(55)
        font.setBold(False)
        self.t1_d_manageddevices.setFont(font)
        self.t1_d_manageddevices.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.t1_d_manageddevices, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.manageddevices, 0, 0, 1, 1)

        self.online = QGroupBox(self.dashboard)
        self.online.setObjectName(u"online")
        self.gridLayout_3 = QGridLayout(self.online)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.t1_d_online = QLabel(self.online)
        self.t1_d_online.setObjectName(u"t1_d_online")
        self.t1_d_online.setFont(font)
        self.t1_d_online.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.t1_d_online, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.online, 0, 1, 1, 1)

        self.offline = QGroupBox(self.dashboard)
        self.offline.setObjectName(u"offline")
        self.gridLayout_4 = QGridLayout(self.offline)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.t1_d_offline = QLabel(self.offline)
        self.t1_d_offline.setObjectName(u"t1_d_offline")
        self.t1_d_offline.setFont(font)
        self.t1_d_offline.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.t1_d_offline, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.offline, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.groupBox_10 = QGroupBox(self.dashboard)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setEnabled(True)
        font1 = QFont()
        font1.setBold(False)
        self.groupBox_10.setFont(font1)
        self.groupBox_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_10.setFlat(False)
        self.gridLayout_12 = QGridLayout(self.groupBox_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.t1_offline_table = QTableWidget(self.groupBox_10)
        self.t1_offline_table.setObjectName(u"t1_offline_table")
        self.t1_offline_table.setFrameShape(QFrame.Shape.NoFrame)
        self.t1_offline_table.setFrameShadow(QFrame.Shadow.Plain)
        self.t1_offline_table.horizontalHeader().setHighlightSections(False)

        self.gridLayout_12.addWidget(self.t1_offline_table, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_10)

        self.groupBox_2 = QGroupBox(self.dashboard)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.t1_syslog_alerts = QPlainTextEdit(self.groupBox_2)
        self.t1_syslog_alerts.setObjectName(u"t1_syslog_alerts")
        self.t1_syslog_alerts.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.gridLayout_6.addWidget(self.t1_syslog_alerts, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.gridLayout_13.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.MainTabWidget.addTab(self.dashboard, "")
        self.inventory = QWidget()
        self.inventory.setObjectName(u"inventory")
        self.gridLayout_16 = QGridLayout(self.inventory)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_3 = QGroupBox(self.inventory)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_15 = QGridLayout(self.groupBox_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.t2_omniswitch_radio = QRadioButton(self.groupBox_3)
        self.t2_omniswitch_radio.setObjectName(u"t2_omniswitch_radio")
        self.t2_omniswitch_radio.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.t2_omniswitch_radio)

        self.t2_stellar_radio = QRadioButton(self.groupBox_3)
        self.t2_stellar_radio.setObjectName(u"t2_stellar_radio")
        self.t2_stellar_radio.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.t2_stellar_radio)

        self.t2_third_party_radio = QRadioButton(self.groupBox_3)
        self.t2_third_party_radio.setObjectName(u"t2_third_party_radio")

        self.horizontalLayout_2.addWidget(self.t2_third_party_radio)

        self.t2_new_btn = QPushButton(self.groupBox_3)
        self.t2_new_btn.setObjectName(u"t2_new_btn")
        self.t2_new_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.t2_new_btn)

        self.t2_add_update_btn = QPushButton(self.groupBox_3)
        self.t2_add_update_btn.setObjectName(u"t2_add_update_btn")
        self.t2_add_update_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.t2_add_update_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)


        self.gridLayout_15.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.t2_i_ip_address = QLineEdit(self.groupBox_3)
        self.t2_i_ip_address.setObjectName(u"t2_i_ip_address")
        self.t2_i_ip_address.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.t2_i_ip_address)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.t2_i_username = QLineEdit(self.groupBox_3)
        self.t2_i_username.setObjectName(u"t2_i_username")
        self.t2_i_username.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.t2_i_username)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.t2_i_password = QLineEdit(self.groupBox_3)
        self.t2_i_password.setObjectName(u"t2_i_password")
        self.t2_i_password.setMaximumSize(QSize(150, 16777215))
        self.t2_i_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.t2_i_password)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)


        self.gridLayout_15.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.inventory)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_14 = QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.t2_inventory_table = QTableWidget(self.groupBox_5)
        self.t2_inventory_table.setObjectName(u"t2_inventory_table")
        self.t2_inventory_table.setFrameShape(QFrame.Shape.NoFrame)
        self.t2_inventory_table.horizontalHeader().setVisible(True)
        self.t2_inventory_table.horizontalHeader().setHighlightSections(False)
        self.t2_inventory_table.verticalHeader().setHighlightSections(False)

        self.gridLayout_14.addWidget(self.t2_inventory_table, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.t2_manage_btn = QPushButton(self.inventory)
        self.t2_manage_btn.setObjectName(u"t2_manage_btn")
        self.t2_manage_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.t2_manage_btn)

        self.t2_delete_btn = QPushButton(self.inventory)
        self.t2_delete_btn.setObjectName(u"t2_delete_btn")
        self.t2_delete_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.t2_delete_btn)

        self.widget = QWidget(self.inventory)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 0))

        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.gridLayout_16.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.MainTabWidget.addTab(self.inventory, "")
        self.syslog = QWidget()
        self.syslog.setObjectName(u"syslog")
        self.gridLayout_21 = QGridLayout(self.syslog)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.syslog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_18 = QGridLayout(self.groupBox_4)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.t3_major_alerts_table = QPlainTextEdit(self.groupBox_4)
        self.t3_major_alerts_table.setObjectName(u"t3_major_alerts_table")
        self.t3_major_alerts_table.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.gridLayout_18.addWidget(self.t3_major_alerts_table, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.syslog)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_19 = QGridLayout(self.groupBox_6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.t3_medium_alerts_table = QPlainTextEdit(self.groupBox_6)
        self.t3_medium_alerts_table.setObjectName(u"t3_medium_alerts_table")
        self.t3_medium_alerts_table.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.gridLayout_19.addWidget(self.t3_medium_alerts_table, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.syslog)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_20 = QGridLayout(self.groupBox_7)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.t3_minor_alerts_table = QPlainTextEdit(self.groupBox_7)
        self.t3_minor_alerts_table.setObjectName(u"t3_minor_alerts_table")
        self.t3_minor_alerts_table.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.gridLayout_20.addWidget(self.t3_minor_alerts_table, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.t3_refresh_btn = QPushButton(self.syslog)
        self.t3_refresh_btn.setObjectName(u"t3_refresh_btn")
        self.t3_refresh_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.t3_refresh_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)


        self.gridLayout_21.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.MainTabWidget.addTab(self.syslog, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.gridLayout_22 = QGridLayout(self.settings)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.t4_save_btn = QPushButton(self.settings)
        self.t4_save_btn.setObjectName(u"t4_save_btn")

        self.horizontalLayout_16.addWidget(self.t4_save_btn)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)


        self.gridLayout_17.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_9 = QGroupBox(self.settings)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_10 = QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.label_8)

        self.t4_mail_server = QLineEdit(self.groupBox_9)
        self.t4_mail_server.setObjectName(u"t4_mail_server")
        self.t4_mail_server.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_9.addWidget(self.t4_mail_server)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.t4_mail_server_port = QLineEdit(self.groupBox_9)
        self.t4_mail_server_port.setObjectName(u"t4_mail_server_port")
        self.t4_mail_server_port.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.t4_mail_server_port)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_13.addWidget(self.label_10)

        self.t4_ssl_radio = QRadioButton(self.groupBox_9)
        self.t4_ssl_radio.setObjectName(u"t4_ssl_radio")

        self.horizontalLayout_13.addWidget(self.t4_ssl_radio)

        self.t4_tls_radio = QRadioButton(self.groupBox_9)
        self.t4_tls_radio.setObjectName(u"t4_tls_radio")

        self.horizontalLayout_13.addWidget(self.t4_tls_radio)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label = QLabel(self.groupBox_9)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_17.addWidget(self.label)

        self.t4_username = QLineEdit(self.groupBox_9)
        self.t4_username.setObjectName(u"t4_username")
        self.t4_username.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_17.addWidget(self.t4_username)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_20)


        self.gridLayout.addLayout(self.horizontalLayout_17, 3, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_18.addWidget(self.label_13)

        self.t4_password = QLineEdit(self.groupBox_9)
        self.t4_password.setObjectName(u"t4_password")
        self.t4_password.setMaximumSize(QSize(250, 16777215))
        self.t4_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_18.addWidget(self.t4_password)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)


        self.gridLayout.addLayout(self.horizontalLayout_18, 4, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_11.addWidget(self.label_11)

        self.t4_from = QLineEdit(self.groupBox_9)
        self.t4_from.setObjectName(u"t4_from")
        self.t4_from.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_11.addWidget(self.t4_from)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_12.addWidget(self.label_12)

        self.t4_recipients = QLineEdit(self.groupBox_9)
        self.t4_recipients.setObjectName(u"t4_recipients")
        self.t4_recipients.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_12.addWidget(self.t4_recipients)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout_12, 6, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.t4_test_btn = QPushButton(self.groupBox_9)
        self.t4_test_btn.setObjectName(u"t4_test_btn")
        self.t4_test_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.t4_test_btn)

        self.horizontalSpacer_17 = QSpacerItem(37, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)


        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(25, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.settings)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.t4_backup_days = QLineEdit(self.groupBox_8)
        self.t4_backup_days.setObjectName(u"t4_backup_days")
        self.t4_backup_days.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.t4_backup_days)

        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.t4_backup_report_yes = QRadioButton(self.groupBox_8)
        self.t4_backup_report_yes.setObjectName(u"t4_backup_report_yes")
        self.t4_backup_report_yes.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.t4_backup_report_yes)

        self.t4_backup_report_no = QRadioButton(self.groupBox_8)
        self.t4_backup_report_no.setObjectName(u"t4_backup_report_no")
        self.t4_backup_report_no.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.t4_backup_report_no)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 215, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_8, 0, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.horizontalSpacer_19, 2, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.MainTabWidget.addTab(self.settings, "")

        self.gridLayout_23.addWidget(self.MainTabWidget, 1, 0, 1, 1)

        nmslite.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.MainTabWidget, self.t1_offline_table)
        QWidget.setTabOrder(self.t1_offline_table, self.t2_i_ip_address)
        QWidget.setTabOrder(self.t2_i_ip_address, self.t2_i_username)
        QWidget.setTabOrder(self.t2_i_username, self.t2_i_password)
        QWidget.setTabOrder(self.t2_i_password, self.t2_omniswitch_radio)
        QWidget.setTabOrder(self.t2_omniswitch_radio, self.t2_stellar_radio)
        QWidget.setTabOrder(self.t2_stellar_radio, self.t2_third_party_radio)
        QWidget.setTabOrder(self.t2_third_party_radio, self.t2_new_btn)
        QWidget.setTabOrder(self.t2_new_btn, self.t2_add_update_btn)
        QWidget.setTabOrder(self.t2_add_update_btn, self.t2_inventory_table)
        QWidget.setTabOrder(self.t2_inventory_table, self.t2_manage_btn)
        QWidget.setTabOrder(self.t2_manage_btn, self.t2_delete_btn)
        QWidget.setTabOrder(self.t2_delete_btn, self.t3_refresh_btn)
        QWidget.setTabOrder(self.t3_refresh_btn, self.t4_mail_server)
        QWidget.setTabOrder(self.t4_mail_server, self.t4_mail_server_port)
        QWidget.setTabOrder(self.t4_mail_server_port, self.t4_ssl_radio)
        QWidget.setTabOrder(self.t4_ssl_radio, self.t4_tls_radio)
        QWidget.setTabOrder(self.t4_tls_radio, self.t4_username)
        QWidget.setTabOrder(self.t4_username, self.t4_password)
        QWidget.setTabOrder(self.t4_password, self.t4_from)
        QWidget.setTabOrder(self.t4_from, self.t4_recipients)
        QWidget.setTabOrder(self.t4_recipients, self.t4_test_btn)
        QWidget.setTabOrder(self.t4_test_btn, self.t4_backup_days)
        QWidget.setTabOrder(self.t4_backup_days, self.t4_backup_report_yes)
        QWidget.setTabOrder(self.t4_backup_report_yes, self.t4_backup_report_no)
        QWidget.setTabOrder(self.t4_backup_report_no, self.t4_save_btn)

        self.retranslateUi(nmslite)

        self.MainTabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(nmslite)
    # setupUi

    def retranslateUi(self, nmslite):
        nmslite.setWindowTitle(QCoreApplication.translate("nmslite", u"OmniVista Lite", None))
        self.logo.setText("")
        self.manageddevices.setTitle(QCoreApplication.translate("nmslite", u"Managed Devices", None))
        self.t1_d_manageddevices.setText(QCoreApplication.translate("nmslite", u"0", None))
        self.online.setTitle(QCoreApplication.translate("nmslite", u"Online", None))
        self.t1_d_online.setText(QCoreApplication.translate("nmslite", u"0", None))
        self.offline.setTitle(QCoreApplication.translate("nmslite", u"Offline", None))
        self.t1_d_offline.setText(QCoreApplication.translate("nmslite", u"0", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("nmslite", u"Offline", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("nmslite", u"Critial Syslog Alerts", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.dashboard), QCoreApplication.translate("nmslite", u"Dashboard", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("nmslite", u"Device Profile", None))
        self.t2_omniswitch_radio.setText(QCoreApplication.translate("nmslite", u"OmniSwitch", None))
        self.t2_stellar_radio.setText(QCoreApplication.translate("nmslite", u"Stellar AP", None))
        self.t2_third_party_radio.setText(QCoreApplication.translate("nmslite", u"Third Party", None))
        self.t2_new_btn.setText(QCoreApplication.translate("nmslite", u"New", None))
        self.t2_add_update_btn.setText(QCoreApplication.translate("nmslite", u"Add / Update", None))
        self.label_2.setText(QCoreApplication.translate("nmslite", u"IP Address:", None))
        self.label_3.setText(QCoreApplication.translate("nmslite", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("nmslite", u"Password:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("nmslite", u"Devices", None))
        self.t2_manage_btn.setText(QCoreApplication.translate("nmslite", u"Manage", None))
        self.t2_delete_btn.setText(QCoreApplication.translate("nmslite", u"Delete", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.inventory), QCoreApplication.translate("nmslite", u"Inventory", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("nmslite", u"Emergency / Critial / Alerts", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("nmslite", u"Error / Warning", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("nmslite", u"Notice / Information / Debug", None))
        self.t3_refresh_btn.setText(QCoreApplication.translate("nmslite", u"Refresh", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.syslog), QCoreApplication.translate("nmslite", u"Syslog", None))
        self.t4_save_btn.setText(QCoreApplication.translate("nmslite", u"Save", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("nmslite", u"Email Server setting", None))
        self.label_8.setText(QCoreApplication.translate("nmslite", u"Mail Server: ", None))
        self.label_9.setText(QCoreApplication.translate("nmslite", u"Port:", None))
        self.label_10.setText(QCoreApplication.translate("nmslite", u"Protocol:", None))
        self.t4_ssl_radio.setText(QCoreApplication.translate("nmslite", u"SSL", None))
        self.t4_tls_radio.setText(QCoreApplication.translate("nmslite", u"TLS", None))
        self.label.setText(QCoreApplication.translate("nmslite", u"Username:", None))
        self.label_13.setText(QCoreApplication.translate("nmslite", u"Password:", None))
        self.label_11.setText(QCoreApplication.translate("nmslite", u"From:", None))
        self.label_12.setText(QCoreApplication.translate("nmslite", u"Recipients:", None))
        self.t4_test_btn.setText(QCoreApplication.translate("nmslite", u"Test", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("nmslite", u"Backup setting", None))
        self.label_6.setText(QCoreApplication.translate("nmslite", u"Retain configuration for", None))
        self.label_5.setText(QCoreApplication.translate("nmslite", u"day(s)", None))
        self.label_7.setText(QCoreApplication.translate("nmslite", u"Send daily backup report", None))
        self.t4_backup_report_yes.setText(QCoreApplication.translate("nmslite", u"Yes", None))
        self.t4_backup_report_no.setText(QCoreApplication.translate("nmslite", u"No", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.settings), QCoreApplication.translate("nmslite", u"Settings", None))
    # retranslateUi

