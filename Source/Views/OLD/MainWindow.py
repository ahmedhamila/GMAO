from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
from PyQt5 import QtCore



class Ui_MainWindow(object):
    def slideLeftMenu(self):
        width=self.left_side_menu.width()
        if width ==50:
                newwidth=250
        else:
                newwidth=50
        self.animation=QtCore.QPropertyAnimation(self.left_side_menu,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: #22333B;\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(self.main_header)
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #00A8E8;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_menu_toggle_btn = QtWidgets.QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.left_menu_toggle_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_toggle_btn.setStyleSheet("background-image: url(:/icons/icons/menu.png);\n"
"background-size : 50px 50px;\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center ;")
        self.left_menu_toggle_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QtCore.QSize(24, 24))
        self.left_menu_toggle_btn.setObjectName("left_menu_toggle_btn")
        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(self.tittle_bar_container)
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"    background-color: #22333B;\n"
"}\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #00A8E8;\n"
"    color: white;\n"
"    margin : 10px 5px; \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_menu_top_buttons = QtWidgets.QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.Maintenance = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.Maintenance.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Maintenance.setFont(font)
        self.Maintenance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Maintenance.setStyleSheet("background-image: url(:/icons/icons/tools.png);\n"
"background-repeat: none;\n"
"padding-left:60px;\n"
"background-position: center left;")
        self.Maintenance.setObjectName("Maintenance")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.Maintenance)
        self.Dashboard = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.Dashboard.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Dashboard.setFont(font)
        self.Dashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dashboard.setStyleSheet("background-image: url(:/icons/icons/dashboard.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center left;")
        self.Dashboard.setObjectName("Dashboard")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.Dashboard)
        self.Equipement = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.Equipement.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Equipement.setFont(font)
        self.Equipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Equipement.setStyleSheet("background-image: url(:/icons/icons/truck.png);\n"
"background-repeat: none;\n"
"padding-left: 75px;\n"
"background-position: center left;")
        self.Equipement.setObjectName("Equipement")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.Equipement)
        self.Notification = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.Notification.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Notification.setFont(font)
        self.Notification.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Notification.setStyleSheet("background-image: url(:/icons/icons/notification.png);\n"
"background-repeat: none;\n"
"padding-left: 65px;\n"
"background-position: center left;")
        self.Notification.setObjectName("Notification")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.Notification)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)
        self.SingOut = QtWidgets.QPushButton(self.left_side_menu)
        self.SingOut.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SingOut.setFont(font)
        self.SingOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SingOut.setStyleSheet("background-image: url(:/icons/icons/sign-out.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center left;")
        self.SingOut.setObjectName("SingOut")
        self.verticalLayout_3.addWidget(self.SingOut)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setStyleSheet("background-color: #FEFDFC;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame{\n"
"    background-color: grey;\n"
"}")
        self.main_footer.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.left_menu_toggle_btn.clicked.connect(self.slideLeftMenu)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.Maintenance.setText(_translate("MainWindow", "Maintenance"))
        self.Dashboard.setText(_translate("MainWindow", "Dashboard"))
        self.Equipement.setText(_translate("MainWindow", "Equipements"))
        self.Notification.setText(_translate("MainWindow", "Notifications"))
        self.SingOut.setText(_translate("MainWindow", "Sign out"))


from .. import icons_rc