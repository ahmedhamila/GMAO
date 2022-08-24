from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from Models import AgentMaintenanceServices,ResponsableMaintenanceServices,EquipementServices,BonTravailServices,DemandeInterventionServices
class Ui_Dialog(object):
    def __init__(self,mainWindowSelf,redirectFrom,refDIM=None,returnTo=None) -> None:
        self.mainWindowSelf=mainWindowSelf
        self.redirectFrom=redirectFrom
        self.refDIM=refDIM
        self.returnTo=returnTo
    def radioButtonClicked(self):
        if self.radioButtonPreventif.isChecked() :
            self.lineEditPreventif.setVisible(True)
            self.checkBoxActive.setVisible(True)
            self.lineEditCorrectif.setVisible(False)
        if self.radioButtonCorrectif.isChecked() :
            self.lineEditPreventif.setVisible(False)
            self.checkBoxActive.setVisible(False)
            self.lineEditCorrectif.setVisible(True)
    def comboChange(self):
        self.labelCodeEquipement.setText(self.codes[self.comboBoxEquipement.currentIndex()])
    def addBonTravail(self):
        refDIM=""
        frequence=""
        active=""
        if self.radioButtonPreventif.isChecked() :
            frequence = self.lineEditPreventif.text()
            active = self.checkBoxActive.isChecked()
            type="Preventif"
        elif self.radioButtonCorrectif.isChecked():
            type="Correctif"
            refDIM = self.lineEditCorrectif.text()
            
        else:
            print("error")
        matriculeRM=self.labelEmetteur.text().split(" ")[0]
        matriculeAM=self.comboBoxDestinateur.currentText().split(" ")[0]
        codeEquipement=self.labelCodeEquipement.text()
        section=self.lineEditSection.text()
        description=self.textEditDescription.toPlainText()
        print("---------------",refDIM,'-',frequence,'-',active)
        dateLiberation=datetime.now().__str__()
        record = (matriculeRM,matriculeAM,description,section,dateLiberation,type,codeEquipement,refDIM,frequence if len(frequence)>0 else 'NULL',1 if active else 0)
        BonTravailServices.addBonTravail(record)
        self.showDialog('Success',"Bon de travail ajouté avec succé",True)
        if self.redirectFrom == "DemandeInterventionConsulterDetaille":
            DemandeInterventionServices.setTraiteeDemandeIntervention(self.refDIM)
            self.returnTo[0].fetchRows()
            self.mainWindowSelf.stackedWidget.setCurrentWidget(self.returnTo[1])
        self.initialiseBonTravail()
    def initialiseBonTravail(self):
        #Initialization
        self.dateLiberation.setText("Date : "+datetime.date(datetime.now()).__str__())
        state,record = ResponsableMaintenanceServices.getResponsableMaintenance(self.mainWindowSelf.matricule)
        if state:
            self.labelEmetteur.setText(record[0][0]+" "+record[0][1]+" "+record[0][2])
        
        state,record = AgentMaintenanceServices.getAgentMaintenance()
        self.comboBoxDestinateur.clear()
        if state:
            for rec in record :
                self.comboBoxDestinateur.addItem(rec[0]+" "+rec[1]+" "+rec[2])

        state,record = EquipementServices.getEquipements()
        self.comboBoxEquipement.clear()
        self.codes=[rec[0] for rec in record]
        
        if state:
            self.labelCodeEquipement.setText(record[0][0])
            for rec in record :
                self.comboBoxEquipement.addItem(rec[1]+" "+rec[2])
        
        self.lineEditSection.setText("")
        self.textEditDescription.setText("")

        self.lineEditCorrectif.setText("")
        self.lineEditPreventif.setText("")
        self.checkBoxActive.setChecked(False)
        self.lineEditCorrectif.setVisible(False)
        self.lineEditPreventif.setVisible(False)
        self.checkBoxActive.setVisible(False)
        
        if self.redirectFrom =="BonTravailList":
            self.radioButtonCorrectif.setEnabled(False)
            
        elif self.redirectFrom == "DemandeInterventionConsulterDetaille":
            self.radioButtonPreventif.setEnabled(False)
            self.lineEditCorrectif.setText(self.refDIM)
            self.lineEditCorrectif.setEnabled(False)

        self.radioButtonCorrectif.setChecked(False)
        self.radioButtonPreventif.setChecked(False)

        
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
        Dialog.resize(850, 825)
        Dialog.setMinimumSize(QtCore.QSize(500, 0))
        Dialog.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: #1A2930;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("background-color : #FEFDFC;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.labelRefBon = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.labelRefBon.setFont(font)
        self.labelRefBon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelRefBon.setObjectName("labelRefBon")
        self.gridLayout.addWidget(self.labelRefBon, 0, 2, 1, 1)
        self.dateLiberation = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.dateLiberation.setFont(font)
        self.dateLiberation.setObjectName("dateLiberation")
        self.gridLayout.addWidget(self.dateLiberation, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setStyleSheet("background-color : #FEFDFC;height:25px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_10 = QtWidgets.QFrame(self.frame_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButtonCorrectif = QtWidgets.QRadioButton(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.radioButtonCorrectif.setFont(font)
        self.radioButtonCorrectif.setObjectName("radioButtonCorrectif")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonCorrectif)
        self.horizontalLayout_3.addWidget(self.radioButtonCorrectif)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.lineEditCorrectif = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditCorrectif.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditCorrectif.setFont(font)
        self.lineEditCorrectif.setStyleSheet("border: 1px solid back;")
        self.lineEditCorrectif.setObjectName("lineEditCorrectif")
        self.verticalLayout_4.addWidget(self.lineEditCorrectif)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonPreventif = QtWidgets.QRadioButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.radioButtonPreventif.setFont(font)
        self.radioButtonPreventif.setObjectName("radioButtonPreventif")
        self.buttonGroup.addButton(self.radioButtonPreventif)
        self.horizontalLayout_2.addWidget(self.radioButtonPreventif)
        self.checkBoxActive = QtWidgets.QCheckBox(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.checkBoxActive.setFont(font)
        self.checkBoxActive.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxActive.setTristate(False)
        self.checkBoxActive.setObjectName("checkBoxActive")
        self.horizontalLayout_2.addWidget(self.checkBoxActive)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.lineEditPreventif = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPreventif.setFont(font)
        self.lineEditPreventif.setStyleSheet("border: 1px solid back;")
        self.lineEditPreventif.setObjectName("lineEditPreventif")
        self.verticalLayout_5.addWidget(self.lineEditPreventif)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setStyleSheet("background-color : #FEFDFC;height:25px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.labelEmetteur = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.labelEmetteur.setFont(font)
        self.labelEmetteur.setStyleSheet("height:25px;")
        self.labelEmetteur.setText("")
        self.labelEmetteur.setObjectName("labelEmetteur")
        self.gridLayout_3.addWidget(self.labelEmetteur, 0, 1, 1, 2)
        self.comboBoxDestinateur = QtWidgets.QComboBox(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxDestinateur.setFont(font)
        self.comboBoxDestinateur.setObjectName("comboBoxDestinateur")
        self.gridLayout_3.addWidget(self.comboBoxDestinateur, 1, 1, 1, 2)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("background-color : #FEFDFC;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBoxEquipement = QtWidgets.QComboBox(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxEquipement.setFont(font)
        self.comboBoxEquipement.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxEquipement.setObjectName("comboBoxEquipement")
        self.gridLayout_4.addWidget(self.comboBoxEquipement, 0, 1, 1, 1)
        self.lineEditSection = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditSection.setFont(font)
        self.lineEditSection.setStyleSheet("border: 1px solid back;height:25px;")
        self.lineEditSection.setObjectName("lineEditSection")
        self.gridLayout_4.addWidget(self.lineEditSection, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.labelCodeEquipement = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.labelCodeEquipement.setFont(font)
        self.labelCodeEquipement.setText("")
        self.labelCodeEquipement.setObjectName("labelCodeEquipement")
        self.gridLayout_4.addWidget(self.labelCodeEquipement, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color : #FEFDFC;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color : #FEFDFC;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.textEditDescription = QtWidgets.QTextEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEditDescription.setFont(font)
        self.textEditDescription.setStyleSheet("border: 1px solid back;")
        self.textEditDescription.setObjectName("textEditDescription")
        self.verticalLayout_3.addWidget(self.textEditDescription)
        self.verticalLayout.addWidget(self.frame_4)
        self.buttonEnvoyer = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(18)
        self.buttonEnvoyer.setFont(font)
        self.buttonEnvoyer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEnvoyer.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.buttonEnvoyer.setObjectName("buttonEnvoyer")
        self.verticalLayout.addWidget(self.buttonEnvoyer)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.initialiseBonTravail()

        self.comboBoxEquipement.currentTextChanged.connect(self.comboChange)
        self.radioButtonCorrectif.clicked.connect(self.radioButtonClicked)
        self.radioButtonPreventif.clicked.connect(self.radioButtonClicked)

        self.buttonEnvoyer.clicked.connect(self.addBonTravail)
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Manuel des Formulaires"))
        self.label.setText(_translate("Dialog", "FBC"))
        self.labelRefBon.setText(_translate("Dialog", "FMS00101"))
        self.dateLiberation.setText(_translate("Dialog", "Date :"))
        self.label_4.setText(_translate("Dialog", "Bon de travail"))
        self.radioButtonCorrectif.setText(_translate("Dialog", "Correctif ( réf.DIM N° :"))
        self.radioButtonPreventif.setText(_translate("Dialog", "Préventif ( fréquence :"))
        self.checkBoxActive.setText(_translate("Dialog", "Active"))
        self.label_7.setText(_translate("Dialog", "Destinateur :"))
        self.label_6.setText(_translate("Dialog", "Emeteur :"))
        self.label_8.setText(_translate("Dialog", "Equipement { Désignation :"))
        self.label_10.setText(_translate("Dialog", "Section :"))
        self.label_9.setText(_translate("Dialog", "Code :"))
        self.label_11.setText(_translate("Dialog", "Travaux à exécuter ( voir fiche d\'action) :"))
        self.buttonEnvoyer.setText(_translate("Dialog", "Envoyer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
