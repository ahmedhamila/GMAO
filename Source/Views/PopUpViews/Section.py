from PyQt5 import QtCore, QtGui, QtWidgets
from Services import ChaineProductionServices
from PyQt5.QtWidgets import QMessageBox
class Ui_Dialog(object):
    def __init__(self,bonTravailSelf,mainWindowSelf,thisDialog) -> None:
        self.bonTravailSelf=bonTravailSelf
        self.mainWindowSelf=mainWindowSelf
        self.thisDialog=thisDialog
    def hideThisDialog(self):
        self.thisDialog.hide()
    def showParentWindow(self):
        self.mainWindowSelf.mainwindow.show()
        
    def addSection(self):
        refChaine = self.lineEditReference.text()
        nbEquipement = self.spinBoxNBEquipement.value()

        ChaineProductionServices.addChaineProduction((refChaine,nbEquipement))

        state,record = ChaineProductionServices.getChaineProduction()
        self.bonTravailSelf.comboBoxSection.clear()
        if state :
            for rec in record :
                self.bonTravailSelf.comboBoxSection.addItem("Reference Chaine-Production: " +rec[0])
        self.showDialog("Success","Section Ajoutée avec succé",True)

        self.hideThisDialog()
        self.showParentWindow()
        
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
        Dialog.resize(479, 436)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
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
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
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
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEditReference = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditReference.setFont(font)
        self.lineEditReference.setStyleSheet("border: 1px solid back;height:25px;")
        self.lineEditReference.setText("")
        self.lineEditReference.setObjectName("lineEditReference")
        self.verticalLayout_3.addWidget(self.lineEditReference)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.spinBoxNBEquipement = QtWidgets.QSpinBox(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxNBEquipement.setFont(font)
        self.spinBoxNBEquipement.setStyleSheet("border: 1px solid back;height:25px;")
        self.spinBoxNBEquipement.setObjectName("spinBoxNBEquipement")
        self.verticalLayout_2.addWidget(self.spinBoxNBEquipement)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.frame_7)
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
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_6.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.buttonEnvoyer.clicked.connect(self.addSection)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Section"))
        self.label_2.setText(_translate("Dialog", "Manuel des Formulaires"))
        self.label_3.setText(_translate("Dialog", "Référence De Chaine"))
        self.label_5.setText(_translate("Dialog", "Nombre Equipement : "))
        self.buttonEnvoyer.setText(_translate("Dialog", "Envoyer"))
