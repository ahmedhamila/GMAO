from PyQt5 import QtCore, QtGui, QtWidgets
from Models import BonTravailServices,ResponsableMaintenanceServices,AgentMaintenanceServices,EquipementServices,DemandeInterventionServices
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):


    
    def __init__(self,mainWindowSelf,id,DemandeInterventionDLG,DemandeInterventionUI) -> None:
        self.id=id
        self.mainWindowSelf=mainWindowSelf
        self.DemandeInterventionDLG=DemandeInterventionDLG
        self.DemandeInterventionUI=DemandeInterventionUI

    def showDialog(self,title,str,bool):
        msgBox = QMessageBox()
        if bool==False:
            msgBox.setIcon(QMessageBox.Warning)
        else:
            msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()  
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(918, 840)
        Dialog.setStyleSheet("background-color : #22333B;\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setStyleSheet("background-color : #FEFDFC;")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fbc = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.fbc.setFont(font)
        self.fbc.setAlignment(QtCore.Qt.AlignCenter)
        self.fbc.setObjectName("fbc")
        self.horizontalLayout.addWidget(self.fbc)
        self.title = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Id = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Id.setFont(font)
        self.Id.setAlignment(QtCore.Qt.AlignCenter)
        self.Id.setObjectName("Id")
        self.verticalLayout_2.addWidget(self.Id)
        self.Date = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Date.setFont(font)
        self.Date.setAlignment(QtCore.Qt.AlignCenter)
        self.Date.setObjectName("Date")
        self.verticalLayout_2.addWidget(self.Date)
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.NomEmetteur = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NomEmetteur.setFont(font)
        self.NomEmetteur.setObjectName("NomEmetteur")
        self.horizontalLayout_3.addWidget(self.NomEmetteur)
        self.NumeroChaine = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumeroChaine.setFont(font)
        self.NumeroChaine.setObjectName("NumeroChaine")
        self.horizontalLayout_3.addWidget(self.NumeroChaine)
        self.verticalLayout_4.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setStyleSheet("QLineEdit{\n"
"    height : 25px;\n"
"}")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.widget_9)
        self.comboBox.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.label_7 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.Section = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Section.setFont(font)
        self.Section.setStyleSheet("border : 1px solid black;")
        self.Section.setObjectName("Section")
        self.horizontalLayout_4.addWidget(self.Section)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 2)
        self.verticalLayout_4.addWidget(self.widget_9)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("margin-left:6px;")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.ArretComplet = QtWidgets.QRadioButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ArretComplet.setFont(font)
        self.ArretComplet.setObjectName("ArretComplet")
        self.horizontalLayout_5.addWidget(self.ArretComplet)
        self.Anomalie = QtWidgets.QRadioButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Anomalie.setFont(font)
        self.Anomalie.setObjectName("Anomalie")
        self.horizontalLayout_5.addWidget(self.Anomalie)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.Observation = QtWidgets.QTextEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Observation.setFont(font)
        self.Observation.setStyleSheet("border : 1px solid black;")
        self.Observation.setObjectName("Observation")
        self.verticalLayout_5.addWidget(self.Observation)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setStyleSheet("background-color : #FEFDFC;")
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.Sumbit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Sumbit.setFont(font)
        self.Sumbit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sumbit.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.Sumbit.setObjectName("Sumbit")
        self.verticalLayout_6.addWidget(self.Sumbit)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.fbc.setText(_translate("Dialog", "FBC"))
        self.title.setText(_translate("Dialog", "Demande d\'Intervention Maintenance"))
        self.Id.setText(_translate("Dialog", "FMS00201"))
        self.Date.setText(_translate("Dialog", "06/06/2022"))
        self.widget_2.setStyleSheet(_translate("Dialog", "background-color : #FEFDFC;"))
        self.label_3.setText(_translate("Dialog", "Emetteur :"))
        self.NomEmetteur.setText(_translate("Dialog", "Nom :"))
        self.NumeroChaine.setText(_translate("Dialog", "Chaine :"))
        self.label_6.setText(_translate("Dialog", "Equipement :"))
        self.label_7.setText(_translate("Dialog", "Code : "))
        self.Section.setPlaceholderText(_translate("Dialog", "Section"))
        self.label.setText(_translate("Dialog", "Motif de l\'appel :"))
        self.ArretComplet.setText(_translate("Dialog", "Arret Complet"))
        self.Anomalie.setText(_translate("Dialog", "Anomalie Pouvant Entrainer une Panne"))
        self.label_2.setText(_translate("Dialog", "Constat (symptôme observés) / Observations :"))
        self.label_5.setText(_translate("Dialog", "Visa Production :"))
        self.label_4.setText(_translate("Dialog", "Nom : "))
        self.Sumbit.setText(_translate("Dialog", "Envoyer"))

