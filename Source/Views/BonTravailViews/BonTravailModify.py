from PyQt5 import QtCore, QtGui, QtWidgets
from Services import BonTravailServices,ResponsableMaintenanceServices,AgentMaintenanceServices,EquipementServices,ChaineProductionServices,OperationServices
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from ..PopUpViews.Operation import Ui_Dialog as Operation_UI
from ..PopUpViews.Section import Ui_Dialog as Section_UI
class Ui_Dialog(object):
    def __init__(self,mainWindowSelf,id,BonTravailDLG,BonTravailUI) -> None:
        self.id=id
        self.mainWindowSelf=mainWindowSelf
        self.BonTravailDLG=BonTravailDLG
        self.BonTravailUI=BonTravailUI
    def comboChange(self):
        self.labelCodeEquipement.setText(str(self.codesEquipement[self.comboBoxEquipement.currentIndex()]))
    def initialiseBonTravail(self):
        status,record=BonTravailServices.getBonTravail(self.id)
        
        if status :
            self.type=record[0][7]
            self.dateLiberation.setText("Date : "+datetime.date(record[0][6]).__str__())

            state1,record1 = ResponsableMaintenanceServices.getResponsableMaintenance(self.mainWindowSelf.matricule)
            if state1:
                self.labelEmetteur.setText(record1[0][0]+" "+record1[0][1]+" "+record1[0][2])
            
            state2,record2 = AgentMaintenanceServices.getAgentMaintenance()
            self.comboBoxDestinateur.clear()
            index=0
            i=0
            #TODO:
            if state2:
                for rec in record2 :
                    if rec[0]==record[0][3] :
                        index = i
                    self.comboBoxDestinateur.addItem(rec[0]+" "+rec[1]+" "+rec[2])
                    i+=1
            self.comboBoxDestinateur.setCurrentIndex(index)

            state3,record3 = EquipementServices.getEquipements()
            self.comboBoxEquipement.clear()
            self.codesEquipement=[rec[0] for rec in record3]
            index=0
            i=0
            if state3:
                for rec in record3 :
                    self.comboBoxEquipement.addItem(rec[1]+" "+rec[2])

            self.comboBoxEquipement.setCurrentIndex(self.codesEquipement.index(record[0][8]))
            self.labelCodeEquipement.setText(str(record3[self.codesEquipement.index(record[0][8])][0]))
                
            if self.type == "Curatif":
                self.comboBoxEquipement.setDisabled(True)
                
            state4,record4 = ChaineProductionServices.getChaineProduction()
            self.comboBoxSection.clear()
            self.codesSection=[rec[0] for rec in record4]
            
            if state4:
                for rec in record4 :
                    self.comboBoxSection.addItem("Reference Chaine-Production: " +rec[0])

            self.comboBoxSection.setCurrentIndex(self.codesSection.index(record[0][5]))

            state5,record5 = OperationServices.getOperation()
            self.comboBoxOperation.clear()
            self.codesOperation=[rec[0] for rec in record5]
            if state5 :
                for rec in record5 :
                    self.comboBoxOperation.addItem("OperationID: " +str(rec[0])+" "+rec[1])

            self.comboBoxOperation.setCurrentIndex(self.codesOperation.index(record[0][4]))
            
            if self.type == "Curatif":
                self.comboBoxSection.setDisabled(True)

            
            
            self.textEditDescription.setText(str(record[0][3]))

            if self.type == "Preventif" :
                self.label_3.setText("Pr??ventif ( fr??quence :")
                self.lineEditPreventifCuratif.setText(str(record[0][10]))
                self.checkBoxActive.setChecked(False if record[0][11]==0 else True)
                self.checkBoxActive.setVisible(True)
            else :
                self.label_3.setText("Curatif ( refDIM :")
                self.label_5.setVisible(False)
                self.lineEditPreventifCuratif.setText(str(record[0][9]))
                self.lineEditPreventifCuratif.setReadOnly(True)
                self.checkBoxActive.setChecked(False)
                self.checkBoxActive.setVisible(False)
                
    def modifierBonTravail(self):
        
        
        frequence="NULL"
        active="0"
        if self.type=="Preventif" :
            frequence = self.lineEditPreventifCuratif.text()
            active = self.checkBoxActive.isChecked()
        else:
            print("error")

            
        matriculeRM=self.labelEmetteur.text().split(" ")[0]
        matriculeAM=self.comboBoxDestinateur.currentText().split(" ")[0]
        
        codeEquipement=self.labelCodeEquipement.text()
        
        section=self.comboBoxSection.currentText().split(" ")[2]
        
        description=self.textEditDescription.toPlainText()
        

        operation=self.comboBoxOperation.currentText().split(" ")[1]
        
        
        record = (matriculeRM,matriculeAM,description,operation,section,self.type,codeEquipement,frequence,1 if active else 0,self.id)
        
        BonTravailServices.updateBonTravail(record)
        
        self.showDialog('Success',"Bon de travail Modifi?? avec succ??",True)
        self.BonTravailUI.fetchRows()
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.BonTravailDLG)
    def displayPopUpOperation(self):
        self.dialogOperation = QtWidgets.QDialog()
        self.uiOperation = Operation_UI(self,self.mainWindowSelf,self.dialogOperation)
        self.uiOperation.setupUi(self.dialogOperation)
        self.mainWindowSelf.mainwindow.hide()
        self.dialogOperation.show()
        
    def displayPopUpSection(self):
        self.dialogSection = QtWidgets.QDialog()
        self.uiSection = Section_UI(self,self.mainWindowSelf,self.dialogSection)
        self.uiSection.setupUi(self.dialogSection)
        self.mainWindowSelf.mainwindow.hide()
        self.dialogSection.show()    
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
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditPreventifCuratif = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPreventifCuratif.setFont(font)
        self.lineEditPreventifCuratif.setStyleSheet("border: 1px solid back;")
        self.lineEditPreventifCuratif.setObjectName("lineEditPreventifCuratif")
        self.horizontalLayout_2.addWidget(self.lineEditPreventifCuratif)
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
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
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 1)
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
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
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
        self.comboBoxDestinateur.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxDestinateur.setObjectName("comboBoxDestinateur")
        self.gridLayout_3.addWidget(self.comboBoxDestinateur, 1, 1, 1, 2)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("background-color : #FEFDFC;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.comboBoxEquipement = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxEquipement.setFont(font)
        self.comboBoxEquipement.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxEquipement.setObjectName("comboBoxEquipement")
        self.horizontalLayout_3.addWidget(self.comboBoxEquipement)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.labelCodeEquipement = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCodeEquipement.setFont(font)
        self.labelCodeEquipement.setText("")
        self.labelCodeEquipement.setObjectName("labelCodeEquipement")
        self.horizontalLayout_3.addWidget(self.labelCodeEquipement)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.comboBoxSection = QtWidgets.QComboBox(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSection.setFont(font)
        self.comboBoxSection.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxSection.setObjectName("comboBoxSection")
        self.horizontalLayout_4.addWidget(self.comboBoxSection)
        self.pushButtonAjoutSection = QtWidgets.QPushButton(self.frame_10)
        self.pushButtonAjoutSection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAjoutSection.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.pushButtonAjoutSection.setObjectName("pushButtonAjoutSection")
        self.horizontalLayout_4.addWidget(self.pushButtonAjoutSection)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.comboBoxOperation = QtWidgets.QComboBox(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxOperation.setFont(font)
        self.comboBoxOperation.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxOperation.setObjectName("comboBoxOperation")
        self.horizontalLayout_5.addWidget(self.comboBoxOperation)
        self.pushButtonAjoutOperation = QtWidgets.QPushButton(self.frame_11)
        self.pushButtonAjoutOperation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAjoutOperation.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.pushButtonAjoutOperation.setObjectName("pushButtonAjoutOperation")
        self.horizontalLayout_5.addWidget(self.pushButtonAjoutOperation)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
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
        font.setPointSize(12)
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
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 3)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.initialiseBonTravail()
        
        self.buttonEnvoyer.clicked.connect(self.modifierBonTravail)
        
        self.comboBoxEquipement.currentTextChanged.connect(self.comboChange)

        self.pushButtonAjoutOperation.clicked.connect(self.displayPopUpOperation)
        self.pushButtonAjoutSection.clicked.connect(self.displayPopUpSection)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Manuel des Formulaires"))
        self.label.setText(_translate("Dialog", "FBC"))
        self.labelRefBon.setText(_translate("Dialog", "FMS00101"))
        self.dateLiberation.setText(_translate("Dialog", "Date :"))
        self.label_4.setText(_translate("Dialog", "Bon de travail"))
        self.label_3.setText(_translate("Dialog", "Pr??ventif ( fr??quence :"))
        self.label_5.setText(_translate("Dialog", "Heures"))
        self.checkBoxActive.setText(_translate("Dialog", "Active"))
        self.label_7.setText(_translate("Dialog", "Intervenant :"))
        self.label_6.setText(_translate("Dialog", "Emeteur :"))
        self.label_8.setText(_translate("Dialog", "Equipement { D??signation :"))
        self.label_9.setText(_translate("Dialog", "Code :"))
        self.label_10.setText(_translate("Dialog", "Section :"))
        self.pushButtonAjoutSection.setText(_translate("Dialog", "Ajouter une section"))
        self.label_12.setText(_translate("Dialog", "Operation :"))
        self.pushButtonAjoutOperation.setText(_translate("Dialog", "Ajouter une operation"))
        self.label_11.setText(_translate("Dialog", "Travaux ?? ex??cuter ( voir fiche d\'action) :"))
        self.buttonEnvoyer.setText(_translate("Dialog", "Envoyer"))
