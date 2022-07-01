# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bonApprovisionnement.ui'
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
        Dialog.resize(783, 699)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #1A2930;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Modern No. 20")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 5)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(16)
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"Modern No. 20")
        font2.setPointSize(12)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.comboBoxDemandeur = QComboBox(self.frame_4)
        self.comboBoxDemandeur.setObjectName(u"comboBoxDemandeur")
        self.comboBoxDemandeur.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.gridLayout.addWidget(self.comboBoxDemandeur, 5, 1, 1, 1)

        self.comboBoxDestinataire = QComboBox(self.frame_4)
        self.comboBoxDestinataire.setObjectName(u"comboBoxDestinataire")
        self.comboBoxDestinataire.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.gridLayout.addWidget(self.comboBoxDestinataire, 5, 3, 1, 2)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        font3 = QFont()
        font3.setFamily(u"Modern No. 20")
        font3.setPointSize(18)
        self.label_11.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBoxQuantite = QSpinBox(self.frame_6)
        self.spinBoxQuantite.setObjectName(u"spinBoxQuantite")
        self.spinBoxQuantite.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.horizontalLayout_3.addWidget(self.spinBoxQuantite)

        self.comboBoxDesignation = QComboBox(self.frame_6)
        self.comboBoxDesignation.setObjectName(u"comboBoxDesignation")
        self.comboBoxDesignation.setLayoutDirection(Qt.LeftToRight)
        self.comboBoxDesignation.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.horizontalLayout_3.addWidget(self.comboBoxDesignation)

        self.pushButtonAjout = QPushButton(self.frame_6)
        self.pushButtonAjout.setObjectName(u"pushButtonAjout")
        self.pushButtonAjout.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonAjout.setStyleSheet(u"QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.horizontalLayout_3.addWidget(self.pushButtonAjout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout.addWidget(self.label_12)

        self.textEditObservation = QTextEdit(self.frame_5)
        self.textEditObservation.setObjectName(u"textEditObservation")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.textEditObservation.setFont(font4)
        self.textEditObservation.setStyleSheet(u"border: 1px solid back;")

        self.horizontalLayout.addWidget(self.textEditObservation)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButtonEnvoyer = QPushButton(self.frame_2)
        self.pushButtonEnvoyer.setObjectName(u"pushButtonEnvoyer")
        self.pushButtonEnvoyer.setFont(font3)
        self.pushButtonEnvoyer.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonEnvoyer.setStyleSheet(u"QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.gridLayout_3.addWidget(self.pushButtonEnvoyer, 0, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 1)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"BON D'APPROVISIONNEMENT INTERNE", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"   FMS00301", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Manuel des Formulaires", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Service Demandeur :", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"FBC", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Service Destinataire :", None))
        self.label_2.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Date le  :", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Quantit\u00e9", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"D\u00e9signation", None))
        self.pushButtonAjout.setText(QCoreApplication.translate("Dialog", u"ADD +", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"OBSERVATION :", None))
        self.pushButtonEnvoyer.setText(QCoreApplication.translate("Dialog", u"Envoyer", None))
    # retranslateUi

