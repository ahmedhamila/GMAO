# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DemandeIntervention.ui'
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
        Dialog.resize(918, 840)
        Dialog.setStyleSheet(u"background-color : #22333B;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color : #FEFDFC;")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fbc = QLabel(self.widget_3)
        self.fbc.setObjectName(u"fbc")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.fbc.setFont(font)
        self.fbc.setAlignment(Qt.AlignCenter)
        self.fbc.setMargin(0)

        self.horizontalLayout.addWidget(self.fbc)

        self.title = QLabel(self.widget_3)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(20)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Id = QLabel(self.widget_4)
        self.Id.setObjectName(u"Id")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.Id.setFont(font2)
        self.Id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Id)

        self.Date = QLabel(self.widget_4)
        self.Date.setObjectName(u"Date")
        self.Date.setFont(font2)
        self.Date.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Date)


        self.horizontalLayout.addWidget(self.widget_4)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.NomEmetteur = QLabel(self.widget_8)
        self.NomEmetteur.setObjectName(u"NomEmetteur")
        self.NomEmetteur.setFont(font2)

        self.horizontalLayout_3.addWidget(self.NomEmetteur)

        self.NumeroChaine = QLabel(self.widget_8)
        self.NumeroChaine.setObjectName(u"NumeroChaine")
        self.NumeroChaine.setFont(font2)

        self.horizontalLayout_3.addWidget(self.NumeroChaine)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"QLineEdit{\n"
"	height : 25px;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setMargin(0)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.comboBox = QComboBox(self.widget_9)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.Section = QLineEdit(self.widget_9)
        self.Section.setObjectName(u"Section")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.Section.setFont(font3)
        self.Section.setStyleSheet(u"border : 1px solid black;")

        self.horizontalLayout_4.addWidget(self.Section)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 2)

        self.verticalLayout_4.addWidget(self.widget_9)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"margin-left:6px;")

        self.horizontalLayout_5.addWidget(self.label)

        self.ArretComplet = QRadioButton(self.widget_5)
        self.ArretComplet.setObjectName(u"ArretComplet")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.ArretComplet.setFont(font4)

        self.horizontalLayout_5.addWidget(self.ArretComplet)

        self.Anomalie = QRadioButton(self.widget_5)
        self.Anomalie.setObjectName(u"Anomalie")
        self.Anomalie.setFont(font4)

        self.horizontalLayout_5.addWidget(self.Anomalie)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_2)

        self.Observation = QTextEdit(self.widget_6)
        self.Observation.setObjectName(u"Observation")
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.Observation.setFont(font5)
        self.Observation.setStyleSheet(u"border : 1px solid black;")

        self.verticalLayout_5.addWidget(self.Observation)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color : #FEFDFC;")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.widget_10)

        self.Sumbit = QPushButton(self.widget)
        self.Sumbit.setObjectName(u"Sumbit")
        self.Sumbit.setFont(font2)
        self.Sumbit.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sumbit.setStyleSheet(u"QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.verticalLayout_6.addWidget(self.Sumbit)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.fbc.setText(QCoreApplication.translate("Dialog", u"FBC", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Demande d'Intervention Maintenance", None))
        self.Id.setText(QCoreApplication.translate("Dialog", u"FMS00201", None))
        self.Date.setText(QCoreApplication.translate("Dialog", u"06/06/2022", None))
        self.widget_2.setStyleSheet(QCoreApplication.translate("Dialog", u"background-color : #FEFDFC;", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Emetteur :", None))
        self.NomEmetteur.setText(QCoreApplication.translate("Dialog", u"Nom :", None))
        self.NumeroChaine.setText(QCoreApplication.translate("Dialog", u"Chaine :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Equipement :", None))
        self.comboBox.setCurrentText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Code : ", None))
        self.Section.setPlaceholderText(QCoreApplication.translate("Dialog", u"Section", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Motif de l'appel :", None))
        self.ArretComplet.setText(QCoreApplication.translate("Dialog", u"Arret Complet", None))
        self.Anomalie.setText(QCoreApplication.translate("Dialog", u"Anomalie Pouvant Entrainer une Panne", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Constat (sympt\u00f4me observ\u00e9s) / Observations :", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Visa Production :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Nom : ", None))
        self.Sumbit.setText(QCoreApplication.translate("Dialog", u"Envoyer", None))
    # retranslateUi

