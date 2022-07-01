# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogIn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(341, 622)
        Dialog.setStyleSheet(u"background-color : #22333B;\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Modern No. 20")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(24)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.Matricule = QLabel(self.frame_3)
        self.Matricule.setObjectName(u"Matricule")
        font2 = QFont()
        font2.setFamily(u"Modern No. 20")
        font2.setPointSize(16)
        self.Matricule.setFont(font2)
        self.Matricule.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.Matricule)

        self.Password = QLabel(self.frame_3)
        self.Password.setObjectName(u"Password")
        self.Password.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Password)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"width : 250px;height : 25px;\n"
"border: 1px solid back;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_2)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setStyleSheet(u"width : 250px;height : 25px;\n"
"border: 1px solid back;")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ErrorLabel = QLabel(self.frame_2)
        self.ErrorLabel.setObjectName(u"ErrorLabel")
        font3 = QFont()
        font3.setFamily(u"Modern No. 20")
        font3.setPointSize(14)
        self.ErrorLabel.setFont(font3)
        self.ErrorLabel.setStyleSheet(u"color : rgb(255, 0, 0);")
        self.ErrorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.ErrorLabel)

        self.LogIn = QPushButton(self.frame_2)
        self.LogIn.setObjectName(u"LogIn")
        self.LogIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.LogIn.setStyleSheet(u"QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.verticalLayout_4.addWidget(self.LogIn)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"GMAO", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.Matricule.setText(QCoreApplication.translate("Dialog", u"Matricule", None))
        self.Password.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.ErrorLabel.setText(QCoreApplication.translate("Dialog", u"Informations Incorrectes", None))
        self.LogIn.setText(QCoreApplication.translate("Dialog", u"Log In", None))
    # retranslateUi

