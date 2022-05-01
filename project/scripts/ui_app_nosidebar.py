# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_nosidebarHfRbYc.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import new_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 607)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"padding:2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(500, 500))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ToolBar = QFrame(self.centralwidget)
        self.ToolBar.setObjectName(u"ToolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToolBar.sizePolicy().hasHeightForWidth())
        self.ToolBar.setSizePolicy(sizePolicy1)
        self.ToolBar.setAutoFillBackground(False)
        self.ToolBar.setStyleSheet(u"background-color: #0db7ed;")
        self.ToolBar.setFrameShape(QFrame.StyledPanel)
        self.ToolBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Logo = QFrame(self.ToolBar)
        self.Logo.setObjectName(u"Logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy2)
        self.Logo.setMaximumSize(QSize(50, 70))
        self.Logo.setSizeIncrement(QSize(0, 0))
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 6, 0, -1)
        self.logo_img = QLabel(self.Logo)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMinimumSize(QSize(0, 0))
        self.logo_img.setMaximumSize(QSize(100, 70))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.logo_img.setFont(font1)
        self.logo_img.setStyleSheet(u"color:white;\n"
"margin-left:9px")
        self.logo_img.setPixmap(QPixmap(u"icons/assets/stats-free-icon-font (1).png"))
        self.logo_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.logo_img)


        self.horizontalLayout.addWidget(self.Logo)

        self.Icons = QFrame(self.ToolBar)
        self.Icons.setObjectName(u"Icons")
        sizePolicy1.setHeightForWidth(self.Icons.sizePolicy().hasHeightForWidth())
        self.Icons.setSizePolicy(sizePolicy1)
        self.Icons.setFrameShape(QFrame.StyledPanel)
        self.Icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Icons)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_icon = QFrame(self.Icons)
        self.sidebar_icon.setObjectName(u"sidebar_icon")
        self.sidebar_icon.setMaximumSize(QSize(190, 50))
        self.sidebar_icon.setCursor(QCursor(Qt.ArrowCursor))
        self.sidebar_icon.setStyleSheet(u"")
        self.sidebar_icon.setFrameShape(QFrame.StyledPanel)
        self.sidebar_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_icon)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo_name = QLabel(self.sidebar_icon)
        self.logo_name.setObjectName(u"logo_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logo_name.sizePolicy().hasHeightForWidth())
        self.logo_name.setSizePolicy(sizePolicy3)
        self.logo_name.setMinimumSize(QSize(0, 0))
        self.logo_name.setMaximumSize(QSize(90, 16777215))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        self.logo_name.setFont(font2)
        self.logo_name.setStyleSheet(u"color:white;\n"
"")

        self.horizontalLayout_4.addWidget(self.logo_name)

        self.open_close_side_bar = QPushButton(self.sidebar_icon)
        self.open_close_side_bar.setObjectName(u"open_close_side_bar")
        self.open_close_side_bar.setMaximumSize(QSize(100, 16777215))
        self.open_close_side_bar.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_close_side_bar.setStyleSheet(u"margin-left:19px")
        icon = QIcon()
        icon.addFile(u"icons/assets/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar.setIcon(icon)
        self.open_close_side_bar.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar)


        self.horizontalLayout_2.addWidget(self.sidebar_icon)

        self.control_icons = QFrame(self.Icons)
        self.control_icons.setObjectName(u"control_icons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.control_icons.sizePolicy().hasHeightForWidth())
        self.control_icons.setSizePolicy(sizePolicy4)
        self.control_icons.setMaximumSize(QSize(150, 50))
        self.control_icons.setFrameShape(QFrame.StyledPanel)
        self.control_icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.control_icons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.minimize = QPushButton(self.control_icons)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/assets/minus-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimize, 0, Qt.AlignRight|Qt.AlignTop)

        self.expand = QPushButton(self.control_icons)
        self.expand.setObjectName(u"expand")
        self.expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand.setStyleSheet(u"margin-right:15px;\n"
"margin-left:15px;")
        icon2 = QIcon()
        icon2.addFile(u"icons/assets/expand-arrows-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand.setIcon(icon2)
        self.expand.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.expand, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.out = QPushButton(self.control_icons)
        self.out.setObjectName(u"out")
        self.out.setCursor(QCursor(Qt.PointingHandCursor))
        self.out.setStyleSheet(u"margin-right: 5px")
        icon3 = QIcon()
        icon3.addFile(u"icons/assets/cross-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.out.setIcon(icon3)
        self.out.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.out, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.control_icons, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.Icons)


        self.verticalLayout.addWidget(self.ToolBar)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setMinimumSize(QSize(500, 0))
        self.Body.setStyleSheet(u"background-color:#F0F1F3;\n"
"padding:0px;")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Body)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_body = QFrame(self.frame)
        self.left_body.setObjectName(u"left_body")
        sizePolicy4.setHeightForWidth(self.left_body.sizePolicy().hasHeightForWidth())
        self.left_body.setSizePolicy(sizePolicy4)
        self.left_body.setMinimumSize(QSize(0, 0))
        self.left_body.setMaximumSize(QSize(220, 16777215))
        self.left_body.setStyleSheet(u"background-color:#384d54;")
        self.left_body.setFrameShape(QFrame.StyledPanel)
        self.left_body.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.left_body)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.choices = QFrame(self.left_body)
        self.choices.setObjectName(u"choices")
        self.choices.setMinimumSize(QSize(240, 0))
        self.choices.setMaximumSize(QSize(240, 16777215))
        self.choices.setFrameShape(QFrame.StyledPanel)
        self.choices.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.choices)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 22, 0, 0)
        self.home_button = QPushButton(self.choices)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(220, 70))
        self.home_button.setMaximumSize(QSize(220, 70))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.home_button.setFont(font3)
        self.home_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-right:85px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/assets/home-free-icon-font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon4)
        self.home_button.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.home_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.time_button = QPushButton(self.choices)
        self.time_button.setObjectName(u"time_button")
        self.time_button.setMinimumSize(QSize(220, 70))
        self.time_button.setMaximumSize(QSize(220, 70))
        font4 = QFont()
        font4.setPointSize(16)
        self.time_button.setFont(font4)
        self.time_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.time_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"\n"
"padding-right:25px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/assets/pulse (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.time_button.setIcon(icon5)
        self.time_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.time_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.fourier_button = QPushButton(self.choices)
        self.fourier_button.setObjectName(u"fourier_button")
        self.fourier_button.setMinimumSize(QSize(220, 70))
        self.fourier_button.setMaximumSize(QSize(230, 70))
        self.fourier_button.setFont(font4)
        self.fourier_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.fourier_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/assets/wave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fourier_button.setIcon(icon6)
        self.fourier_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.fourier_button, 0, Qt.AlignLeft)

        self.compare_button = QPushButton(self.choices)
        self.compare_button.setObjectName(u"compare_button")
        self.compare_button.setMinimumSize(QSize(210, 70))
        self.compare_button.setMaximumSize(QSize(220, 70))
        self.compare_button.setFont(font3)
        self.compare_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.compare_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"text-align: left;\n"
"padding-left:13px\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/assets/compare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.compare_button.setIcon(icon7)
        self.compare_button.setIconSize(QSize(25, 25))
        self.compare_button.setAutoRepeatInterval(100)
        self.compare_button.setAutoDefault(False)
        self.compare_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.compare_button, 0, Qt.AlignLeft)

        self.upload_button = QPushButton(self.choices)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setMinimumSize(QSize(220, 70))
        self.upload_button.setFont(font4)
        self.upload_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding:10px;\n"
"padding-left:15px;\n"
"text-align:left\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/assets/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_button.setIcon(icon8)
        self.upload_button.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.upload_button, 0, Qt.AlignLeft)


        self.vboxLayout.addWidget(self.choices, 0, Qt.AlignTop)

        self.out_2 = QFrame(self.left_body)
        self.out_2.setObjectName(u"out_2")
        self.out_2.setMinimumSize(QSize(0, 70))
        self.out_2.setMaximumSize(QSize(16777215, 70))
        self.out_2.setFrameShape(QFrame.StyledPanel)
        self.out_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.out_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.out_2)
        self.exit_button.setObjectName(u"exit_button")
        font5 = QFont()
        font5.setPointSize(15)
        self.exit_button.setFont(font5)
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-left: 15px;\n"
"padding-right:13px;\n"
"margin-right:5px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icons/assets/sign-out-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon9)
        self.exit_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.exit_button)


        self.vboxLayout.addWidget(self.out_2)


        self.horizontalLayout_6.addWidget(self.left_body)

        self.right_body = QFrame(self.frame)
        self.right_body.setObjectName(u"right_body")
        self.right_body.setFrameShape(QFrame.StyledPanel)
        self.right_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.right_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font6 = QFont()
        font6.setBold(False)
        font6.setKerning(False)
        self.stackedWidget.setFont(font6)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_5 = QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 120, -1, -1)
        self.label_2 = QLabel(self.home_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(270, 270))
        self.label_2.setMaximumSize(QSize(270, 270))
        font7 = QFont()
        font7.setPointSize(20)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"margin-top:10px;\n"
"border:7px solid #0db7ed;\n"
"border-radius:100px;\n"
"padding: 30px;")
        self.label_2.setPixmap(QPixmap(u"icons/assets/analysis.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setMinimumSize(QSize(182, 0))
        font8 = QFont()
        font8.setPointSize(35)
        font8.setBold(True)
        self.label.setFont(font8)
        self.label.setStyleSheet(u"color:#384d54;\n"
"")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.home_page)
        self.time_page = QWidget()
        self.time_page.setObjectName(u"time_page")
        self.verticalLayout_6 = QVBoxLayout(self.time_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.time_nav = QFrame(self.time_page)
        self.time_nav.setObjectName(u"time_nav")
        self.time_nav.setMaximumSize(QSize(16777215, 60))
        self.time_nav.setFrameShape(QFrame.StyledPanel)
        self.time_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.time_nav)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.time_nav_1 = QFrame(self.time_nav)
        self.time_nav_1.setObjectName(u"time_nav_1")
        self.time_nav_1.setMinimumSize(QSize(0, 50))
        self.time_nav_1.setMaximumSize(QSize(16777215, 50))
        self.time_nav_1.setStyleSheet(u"QFrame{\n"
"border:2px solid #384d54;\n"
"border-radius:15px;\n"
"background-color:#0db7ed \n"
"}\n"
"")
        self.time_nav_1.setFrameShape(QFrame.StyledPanel)
        self.time_nav_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.time_nav_1)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.jan_3 = QPushButton(self.time_nav_1)
        self.jan_3.setObjectName(u"jan_3")
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(False)
        self.jan_3.setFont(font9)
        self.jan_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.jan_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.jan_3)

        self.feb_3 = QPushButton(self.time_nav_1)
        self.feb_3.setObjectName(u"feb_3")
        font10 = QFont()
        font10.setPointSize(13)
        self.feb_3.setFont(font10)
        self.feb_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.feb_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.feb_3)

        self.mar_3 = QPushButton(self.time_nav_1)
        self.mar_3.setObjectName(u"mar_3")
        self.mar_3.setFont(font10)
        self.mar_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.mar_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.mar_3)

        self.apr_3 = QPushButton(self.time_nav_1)
        self.apr_3.setObjectName(u"apr_3")
        self.apr_3.setFont(font10)
        self.apr_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.apr_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.apr_3)

        self.mai_3 = QPushButton(self.time_nav_1)
        self.mai_3.setObjectName(u"mai_3")
        self.mai_3.setFont(font10)
        self.mai_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.mai_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.mai_3)

        self.june_3 = QPushButton(self.time_nav_1)
        self.june_3.setObjectName(u"june_3")
        self.june_3.setFont(font10)
        self.june_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.june_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.june_3)

        self.july_3 = QPushButton(self.time_nav_1)
        self.july_3.setObjectName(u"july_3")
        self.july_3.setFont(font10)
        self.july_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.july_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.july_3)

        self.aug_3 = QPushButton(self.time_nav_1)
        self.aug_3.setObjectName(u"aug_3")
        self.aug_3.setFont(font10)
        self.aug_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.aug_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.aug_3)

        self.sep_3 = QPushButton(self.time_nav_1)
        self.sep_3.setObjectName(u"sep_3")
        self.sep_3.setFont(font10)
        self.sep_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.sep_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.sep_3)

        self.okt_3 = QPushButton(self.time_nav_1)
        self.okt_3.setObjectName(u"okt_3")
        self.okt_3.setFont(font10)
        self.okt_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.okt_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.okt_3)

        self.novem_3 = QPushButton(self.time_nav_1)
        self.novem_3.setObjectName(u"novem_3")
        self.novem_3.setFont(font10)
        self.novem_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.novem_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.novem_3)

        self.dec_3 = QPushButton(self.time_nav_1)
        self.dec_3.setObjectName(u"dec_3")
        self.dec_3.setFont(font10)
        self.dec_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.dec_3.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_14.addWidget(self.dec_3)


        self.horizontalLayout_15.addWidget(self.time_nav_1)


        self.verticalLayout_6.addWidget(self.time_nav)

        self.time_graph = QFrame(self.time_page)
        self.time_graph.setObjectName(u"time_graph")
        self.time_graph.setFrameShape(QFrame.StyledPanel)
        self.time_graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.time_graph)

        self.time_download = QFrame(self.time_page)
        self.time_download.setObjectName(u"time_download")
        self.time_download.setMaximumSize(QSize(16777215, 80))
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(True)
        self.time_download.setFont(font11)
        self.time_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.time_download.setFrameShape(QFrame.StyledPanel)
        self.time_download.setFrameShadow(QFrame.Raised)
        self.time_download.setLineWidth(3)
        self.horizontalLayout_8 = QHBoxLayout(self.time_download)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.time_download)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
        self.pushButton.setMaximumSize(QSize(210, 16777215))
        font12 = QFont()
        font12.setBold(True)
        self.pushButton.setFont(font12)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius: 7px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"  padding: 17px;\n"
"  font-size:18px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/assets/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon10)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_6.addWidget(self.time_download)

        self.stackedWidget.addWidget(self.time_page)
        self.fourier_page = QWidget()
        self.fourier_page.setObjectName(u"fourier_page")
        self.verticalLayout_7 = QVBoxLayout(self.fourier_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.freq_nav = QFrame(self.fourier_page)
        self.freq_nav.setObjectName(u"freq_nav")
        self.freq_nav.setMinimumSize(QSize(0, 60))
        self.freq_nav.setMaximumSize(QSize(16777215, 60))
        self.freq_nav.setFrameShape(QFrame.StyledPanel)
        self.freq_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.freq_nav)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.freq_nav_1 = QFrame(self.freq_nav)
        self.freq_nav_1.setObjectName(u"freq_nav_1")
        self.freq_nav_1.setMinimumSize(QSize(0, 50))
        self.freq_nav_1.setMaximumSize(QSize(16777215, 50))
        self.freq_nav_1.setStyleSheet(u"QFrame{\n"
"border:2px solid #384d54;\n"
"border-radius:15px;\n"
"background-color:#0db7ed \n"
"}\n"
"")
        self.freq_nav_1.setFrameShape(QFrame.StyledPanel)
        self.freq_nav_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.freq_nav_1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.jan_2 = QPushButton(self.freq_nav_1)
        self.jan_2.setObjectName(u"jan_2")
        self.jan_2.setFont(font9)
        self.jan_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.jan_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.jan_2)

        self.feb_2 = QPushButton(self.freq_nav_1)
        self.feb_2.setObjectName(u"feb_2")
        self.feb_2.setFont(font10)
        self.feb_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.feb_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.feb_2)

        self.mar_2 = QPushButton(self.freq_nav_1)
        self.mar_2.setObjectName(u"mar_2")
        self.mar_2.setFont(font10)
        self.mar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.mar_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.mar_2)

        self.apr_2 = QPushButton(self.freq_nav_1)
        self.apr_2.setObjectName(u"apr_2")
        self.apr_2.setFont(font10)
        self.apr_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.apr_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.apr_2)

        self.mai_2 = QPushButton(self.freq_nav_1)
        self.mai_2.setObjectName(u"mai_2")
        self.mai_2.setFont(font10)
        self.mai_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.mai_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.mai_2)

        self.june_2 = QPushButton(self.freq_nav_1)
        self.june_2.setObjectName(u"june_2")
        self.june_2.setFont(font10)
        self.june_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.june_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.june_2)

        self.july_2 = QPushButton(self.freq_nav_1)
        self.july_2.setObjectName(u"july_2")
        self.july_2.setFont(font10)
        self.july_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.july_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.july_2)

        self.aug_2 = QPushButton(self.freq_nav_1)
        self.aug_2.setObjectName(u"aug_2")
        self.aug_2.setFont(font10)
        self.aug_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.aug_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.aug_2)

        self.sep_2 = QPushButton(self.freq_nav_1)
        self.sep_2.setObjectName(u"sep_2")
        self.sep_2.setFont(font10)
        self.sep_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.sep_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.sep_2)

        self.okt_2 = QPushButton(self.freq_nav_1)
        self.okt_2.setObjectName(u"okt_2")
        self.okt_2.setFont(font10)
        self.okt_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.okt_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.okt_2)

        self.novem_2 = QPushButton(self.freq_nav_1)
        self.novem_2.setObjectName(u"novem_2")
        self.novem_2.setFont(font10)
        self.novem_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.novem_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.novem_2)

        self.dec_2 = QPushButton(self.freq_nav_1)
        self.dec_2.setObjectName(u"dec_2")
        self.dec_2.setFont(font10)
        self.dec_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dec_2.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_12.addWidget(self.dec_2)


        self.horizontalLayout_10.addWidget(self.freq_nav_1)


        self.verticalLayout_7.addWidget(self.freq_nav)

        self.freq_graph = QFrame(self.fourier_page)
        self.freq_graph.setObjectName(u"freq_graph")
        self.freq_graph.setFrameShape(QFrame.StyledPanel)
        self.freq_graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.freq_graph)

        self.freq_download = QFrame(self.fourier_page)
        self.freq_download.setObjectName(u"freq_download")
        self.freq_download.setMaximumSize(QSize(16777215, 80))
        self.freq_download.setFrameShape(QFrame.StyledPanel)
        self.freq_download.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.freq_download)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_2 = QPushButton(self.freq_download)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy5)
        self.pushButton_2.setMaximumSize(QSize(210, 16777215))
        self.pushButton_2.setFont(font12)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius: 7px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"  padding: 17px;\n"
"  font-size:18px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}\n"
"")
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout_7.addWidget(self.freq_download)

        self.stackedWidget.addWidget(self.fourier_page)
        self.compare_page = QWidget()
        self.compare_page.setObjectName(u"compare_page")
        self.verticalLayout_8 = QVBoxLayout(self.compare_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.comp_nav = QFrame(self.compare_page)
        self.comp_nav.setObjectName(u"comp_nav")
        self.comp_nav.setMinimumSize(QSize(0, 70))
        self.comp_nav.setMaximumSize(QSize(16777215, 70))
        self.comp_nav.setFrameShape(QFrame.StyledPanel)
        self.comp_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.comp_nav)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comp_nav_1 = QFrame(self.comp_nav)
        self.comp_nav_1.setObjectName(u"comp_nav_1")
        self.comp_nav_1.setMinimumSize(QSize(0, 50))
        self.comp_nav_1.setMaximumSize(QSize(16777215, 50))
        self.comp_nav_1.setStyleSheet(u"QFrame{\n"
"border:2px solid #384d54;\n"
"border-radius:15px;\n"
"background-color:#0db7ed \n"
"}\n"
"")
        self.comp_nav_1.setFrameShape(QFrame.StyledPanel)
        self.comp_nav_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.comp_nav_1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.jan = QPushButton(self.comp_nav_1)
        self.jan.setObjectName(u"jan")
        self.jan.setFont(font9)
        self.jan.setCursor(QCursor(Qt.PointingHandCursor))
        self.jan.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.jan)

        self.feb = QPushButton(self.comp_nav_1)
        self.feb.setObjectName(u"feb")
        self.feb.setFont(font10)
        self.feb.setCursor(QCursor(Qt.PointingHandCursor))
        self.feb.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.feb)

        self.mar = QPushButton(self.comp_nav_1)
        self.mar.setObjectName(u"mar")
        self.mar.setFont(font10)
        self.mar.setCursor(QCursor(Qt.PointingHandCursor))
        self.mar.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.mar)

        self.apr = QPushButton(self.comp_nav_1)
        self.apr.setObjectName(u"apr")
        self.apr.setFont(font10)
        self.apr.setCursor(QCursor(Qt.PointingHandCursor))
        self.apr.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.apr)

        self.mai = QPushButton(self.comp_nav_1)
        self.mai.setObjectName(u"mai")
        self.mai.setFont(font10)
        self.mai.setCursor(QCursor(Qt.PointingHandCursor))
        self.mai.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.mai)

        self.june = QPushButton(self.comp_nav_1)
        self.june.setObjectName(u"june")
        self.june.setFont(font10)
        self.june.setCursor(QCursor(Qt.PointingHandCursor))
        self.june.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.june)

        self.july = QPushButton(self.comp_nav_1)
        self.july.setObjectName(u"july")
        self.july.setFont(font10)
        self.july.setCursor(QCursor(Qt.PointingHandCursor))
        self.july.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.july)

        self.aug = QPushButton(self.comp_nav_1)
        self.aug.setObjectName(u"aug")
        self.aug.setFont(font10)
        self.aug.setCursor(QCursor(Qt.PointingHandCursor))
        self.aug.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.aug)

        self.sep = QPushButton(self.comp_nav_1)
        self.sep.setObjectName(u"sep")
        self.sep.setFont(font10)
        self.sep.setCursor(QCursor(Qt.PointingHandCursor))
        self.sep.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.sep)

        self.okt = QPushButton(self.comp_nav_1)
        self.okt.setObjectName(u"okt")
        self.okt.setFont(font10)
        self.okt.setCursor(QCursor(Qt.PointingHandCursor))
        self.okt.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.okt)

        self.novem = QPushButton(self.comp_nav_1)
        self.novem.setObjectName(u"novem")
        self.novem.setFont(font10)
        self.novem.setCursor(QCursor(Qt.PointingHandCursor))
        self.novem.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.novem)

        self.dec = QPushButton(self.comp_nav_1)
        self.dec.setObjectName(u"dec")
        self.dec.setFont(font10)
        self.dec.setCursor(QCursor(Qt.PointingHandCursor))
        self.dec.setStyleSheet(u"QPushButton{\n"
"color: #FFF;\n"
"background-color:#0db7ed \n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")

        self.horizontalLayout_11.addWidget(self.dec)


        self.horizontalLayout_13.addWidget(self.comp_nav_1)


        self.verticalLayout_8.addWidget(self.comp_nav)

        self.comp_time = QFrame(self.compare_page)
        self.comp_time.setObjectName(u"comp_time")
        self.comp_time.setFrameShape(QFrame.StyledPanel)
        self.comp_time.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.comp_time)

        self.comp_freq = QFrame(self.compare_page)
        self.comp_freq.setObjectName(u"comp_freq")
        self.comp_freq.setFrameShape(QFrame.StyledPanel)
        self.comp_freq.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.comp_freq)

        self.stackedWidget.addWidget(self.compare_page)
        self.upload_page = QWidget()
        self.upload_page.setObjectName(u"upload_page")
        self.horizontalLayout_18 = QHBoxLayout(self.upload_page)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_2 = QFrame(self.upload_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(450, 391))
        font13 = QFont()
        font13.setPointSize(12)
        self.frame_2.setFont(font13)
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"border: 4px solid #414b56;\n"
"border-radius:35px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 16, -1, -1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 90))
        self.label_3.setMaximumSize(QSize(70, 70))
        self.label_3.setStyleSheet(u"margin-bottom:1px")
        self.label_3.setPixmap(QPixmap(u"icons/assets/upload_img.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_3)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.file_name = QLabel(self.frame_4)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setEnabled(False)
        self.file_name.setMinimumSize(QSize(300, 0))
        self.file_name.setStyleSheet(u"color: black;\n"
"font-size:15px;\n"
"padding-top:29px;\n"
"margin-left:25px")

        self.verticalLayout_10.addWidget(self.file_name, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(280, 55))
        self.pushButton_3.setMaximumSize(QSize(16777215, 40))
        font14 = QFont()
        self.pushButton_3.setFont(font14)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius: 13px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"\n"
"  font-size:25px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}\n"
"")
        self.pushButton_3.setIcon(icon8)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.pushButton_3)


        self.verticalLayout_9.addWidget(self.frame_4)


        self.horizontalLayout_18.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.upload_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.right_body)


        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.compare_button.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_img.setText("")
        self.logo_name.setText(QCoreApplication.translate("MainWindow", u"ANOM", None))
        self.open_close_side_bar.setText("")
        self.minimize.setText("")
        self.expand.setText("")
        self.out.setText("")
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.time_button.setText(QCoreApplication.translate("MainWindow", u" Time Domain", None))
        self.fourier_button.setText(QCoreApplication.translate("MainWindow", u" Fourier Domain", None))
        self.compare_button.setText(QCoreApplication.translate("MainWindow", u" Compare ", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"  Upload", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u" Exit", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" ANOM", None))
        self.jan_3.setText(QCoreApplication.translate("MainWindow", u"Jan", None))
        self.feb_3.setText(QCoreApplication.translate("MainWindow", u"Feb", None))
        self.mar_3.setText(QCoreApplication.translate("MainWindow", u"Mar", None))
        self.apr_3.setText(QCoreApplication.translate("MainWindow", u"Apr", None))
        self.mai_3.setText(QCoreApplication.translate("MainWindow", u"Mai", None))
        self.june_3.setText(QCoreApplication.translate("MainWindow", u"June", None))
        self.july_3.setText(QCoreApplication.translate("MainWindow", u"July", None))
        self.aug_3.setText(QCoreApplication.translate("MainWindow", u"Aug", None))
        self.sep_3.setText(QCoreApplication.translate("MainWindow", u"Sep", None))
        self.okt_3.setText(QCoreApplication.translate("MainWindow", u"Okt", None))
        self.novem_3.setText(QCoreApplication.translate("MainWindow", u"Nov", None))
        self.dec_3.setText(QCoreApplication.translate("MainWindow", u"Dec", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Download Graph", None))
        self.jan_2.setText(QCoreApplication.translate("MainWindow", u"Jan", None))
        self.feb_2.setText(QCoreApplication.translate("MainWindow", u"Feb", None))
        self.mar_2.setText(QCoreApplication.translate("MainWindow", u"Mar", None))
        self.apr_2.setText(QCoreApplication.translate("MainWindow", u"Apr", None))
        self.mai_2.setText(QCoreApplication.translate("MainWindow", u"Mai", None))
        self.june_2.setText(QCoreApplication.translate("MainWindow", u"June", None))
        self.july_2.setText(QCoreApplication.translate("MainWindow", u"July", None))
        self.aug_2.setText(QCoreApplication.translate("MainWindow", u"Aug", None))
        self.sep_2.setText(QCoreApplication.translate("MainWindow", u"Sep", None))
        self.okt_2.setText(QCoreApplication.translate("MainWindow", u"Okt", None))
        self.novem_2.setText(QCoreApplication.translate("MainWindow", u"Nov", None))
        self.dec_2.setText(QCoreApplication.translate("MainWindow", u"Dec", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Download Graph", None))
        self.jan.setText(QCoreApplication.translate("MainWindow", u"Jan", None))
        self.feb.setText(QCoreApplication.translate("MainWindow", u"Feb", None))
        self.mar.setText(QCoreApplication.translate("MainWindow", u"Mar", None))
        self.apr.setText(QCoreApplication.translate("MainWindow", u"Apr", None))
        self.mai.setText(QCoreApplication.translate("MainWindow", u"Mai", None))
        self.june.setText(QCoreApplication.translate("MainWindow", u"June", None))
        self.july.setText(QCoreApplication.translate("MainWindow", u"July", None))
        self.aug.setText(QCoreApplication.translate("MainWindow", u"Aug", None))
        self.sep.setText(QCoreApplication.translate("MainWindow", u"Sep", None))
        self.okt.setText(QCoreApplication.translate("MainWindow", u"Okt", None))
        self.novem.setText(QCoreApplication.translate("MainWindow", u"Nov", None))
        self.dec.setText(QCoreApplication.translate("MainWindow", u"Dec", None))
        self.label_3.setText("")
        self.file_name.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Upload", None))
    # retranslateUi

