# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bonTravail.ui'
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
        Dialog.resize(719, 825)
        Dialog.setMinimumSize(QSize(500, 0))
        Dialog.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #1A2930;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Modern No. 20")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(22)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.labelRefBon = QLabel(self.frame_8)
        self.labelRefBon.setObjectName(u"labelRefBon")
        font2 = QFont()
        font2.setFamily(u"Modern No. 20")
        font2.setPointSize(16)
        self.labelRefBon.setFont(font2)
        self.labelRefBon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelRefBon, 0, 2, 1, 1)

        self.dateLiberation = QLabel(self.frame_8)
        self.dateLiberation.setObjectName(u"dateLiberation")
        font3 = QFont()
        font3.setFamily(u"Modern No. 20")
        font3.setPointSize(14)
        self.dateLiberation.setFont(font3)

        self.gridLayout.addWidget(self.dateLiberation, 1, 2, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color : #FEFDFC;height:25px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEditCorrectif = QLineEdit(self.frame_7)
        self.lineEditCorrectif.setObjectName(u"lineEditCorrectif")
        self.lineEditCorrectif.setMaximumSize(QSize(1000, 16777215))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.lineEditCorrectif.setFont(font4)
        self.lineEditCorrectif.setStyleSheet(u"border: 1px solid back;")

        self.gridLayout_2.addWidget(self.lineEditCorrectif, 1, 0, 1, 1)

        self.radioButtonCorrectif = QRadioButton(self.frame_7)
        self.radioButtonCorrectif.setObjectName(u"radioButtonCorrectif")
        font5 = QFont()
        font5.setFamily(u"Modern No. 20")
        font5.setPointSize(12)
        self.radioButtonCorrectif.setFont(font5)

        self.gridLayout_2.addWidget(self.radioButtonCorrectif, 0, 0, 1, 1)

        self.radioButtonPreventif = QRadioButton(self.frame_7)
        self.radioButtonPreventif.setObjectName(u"radioButtonPreventif")
        self.radioButtonPreventif.setFont(font5)

        self.gridLayout_2.addWidget(self.radioButtonPreventif, 0, 1, 1, 1)

        self.lineEditPreventif = QLineEdit(self.frame_7)
        self.lineEditPreventif.setObjectName(u"lineEditPreventif")
        self.lineEditPreventif.setFont(font4)
        self.lineEditPreventif.setStyleSheet(u"border: 1px solid back;")

        self.gridLayout_2.addWidget(self.lineEditPreventif, 1, 1, 1, 1)

        self.checkBoxActive = QCheckBox(self.frame_7)
        self.checkBoxActive.setObjectName(u"checkBoxActive")
        self.checkBoxActive.setFont(font3)

        self.gridLayout_2.addWidget(self.checkBoxActive, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color : #FEFDFC;height:25px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.labelEmetteur = QLabel(self.frame_6)
        self.labelEmetteur.setObjectName(u"labelEmetteur")
        self.labelEmetteur.setFont(font5)
        self.labelEmetteur.setStyleSheet(u"height:25px;")

        self.gridLayout_3.addWidget(self.labelEmetteur, 0, 1, 1, 2)

        self.comboBoxDestinateur = QComboBox(self.frame_6)
        self.comboBoxDestinateur.setObjectName(u"comboBoxDestinateur")

        self.gridLayout_3.addWidget(self.comboBoxDestinateur, 1, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBoxEquipement = QComboBox(self.frame_5)
        self.comboBoxEquipement.setObjectName(u"comboBoxEquipement")
        self.comboBoxEquipement.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.gridLayout_4.addWidget(self.comboBoxEquipement, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.lineEditSection = QLineEdit(self.frame_5)
        self.lineEditSection.setObjectName(u"lineEditSection")
        self.lineEditSection.setFont(font4)
        self.lineEditSection.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.gridLayout_4.addWidget(self.lineEditSection, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)

        self.labelCodeEquipement = QLabel(self.frame_5)
        self.labelCodeEquipement.setObjectName(u"labelCodeEquipement")
        self.labelCodeEquipement.setFont(font5)

        self.gridLayout_4.addWidget(self.labelCodeEquipement, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color : #FEFDFC;")

        self.verticalLayout_3.addWidget(self.label_11)

        self.textEditDescription = QTextEdit(self.frame_4)
        self.textEditDescription.setObjectName(u"textEditDescription")
        self.textEditDescription.setFont(font4)
        self.textEditDescription.setStyleSheet(u"border: 1px solid back;")

        self.verticalLayout_3.addWidget(self.textEditDescription)


        self.verticalLayout.addWidget(self.frame_4)

        self.buttonEnvoyer = QPushButton(self.frame)
        self.buttonEnvoyer.setObjectName(u"buttonEnvoyer")
        font6 = QFont()
        font6.setFamily(u"Modern No. 20")
        font6.setPointSize(18)
        self.buttonEnvoyer.setFont(font6)
        self.buttonEnvoyer.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonEnvoyer.setStyleSheet(u"QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.verticalLayout.addWidget(self.buttonEnvoyer)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)

        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Manuel des Formulaires", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"FBC", None))
        self.labelRefBon.setText(QCoreApplication.translate("Dialog", u"FMS00101", None))
        self.dateLiberation.setText(QCoreApplication.translate("Dialog", u"Date :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Bon de travail", None))
        self.radioButtonCorrectif.setText(QCoreApplication.translate("Dialog", u"Correctif ( r\u00e9f.DIM N\u00b0 :", None))
        self.radioButtonPreventif.setText(QCoreApplication.translate("Dialog", u"Pr\u00e9ventif ( fr\u00e9quence :", None))
        self.checkBoxActive.setText(QCoreApplication.translate("Dialog", u"Active", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Emeteur :", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Destinateur :", None))
        self.labelEmetteur.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Equipement { D\u00e9signation :", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Section :", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Code :", None))
        self.labelCodeEquipement.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Travaux \u00e0 ex\u00e9cuter ( voir fiche d'action) :", None))
        self.buttonEnvoyer.setText(QCoreApplication.translate("Dialog", u"Envoyer", None))
    # retranslateUi

