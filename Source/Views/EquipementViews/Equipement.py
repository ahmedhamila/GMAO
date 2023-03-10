from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import datetime
from Services import PieceRechangeServices,EquipementServices

class Ui_Dialog(object):
    def __init__(self,mainWindowSelf) -> None:
        self.mainWindowSelf=mainWindowSelf
    def addComposant(self):
        if self.comboBoxComposants.currentText().split(" ")[0] not in self.selectedComposantsCodes:
            self.selectedComposantsCodes.append(self.comboBoxComposants.currentText().split(" ")[0])

        self.selectedComposantsLabels.append(self.comboBoxComposants.currentText().split(" ")[1])
        self.labelListeComposants.setText(",".join(list(set(self.selectedComposantsLabels))))

    def addEquipement(self):
        reference=self.lineEditReference.text()
        designation=self.lineEditDesignation.text()
        role=self.lineEditRole.text()
        fabriquant=self.lineEditFabriquant.text()

        dateFabriquation=self.dateEditFabriquation.date().toString("yyyy-MM-dd")
        dateMiseEnMarche=self.dateEditMiseEnMarche.date().toString("yyyy-MM-dd")

        record=(reference,designation,role,fabriquant,dateFabriquation,dateMiseEnMarche)
        
        EquipementServices.addEquipement(record)
        for composant in self.selectedComposantsCodes:
            EquipementServices.addEquipementComposant((reference,composant))
        
        self.showDialog('Success',"Equipement ajouté avec succé",True)
        
        self.initialisationEquipement()

    def initialisationEquipement(self):
        self.lineEditReference.setText("")
        self.lineEditDesignation.setText("")
        self.lineEditRole.setText("")
        self.lineEditFabriquant.setText("")

        self.dateEditFabriquation.setDate(QDate(2020,1,1))
        self.dateEditMiseEnMarche.setDate(QDate(2020,1,1))

        status,record=PieceRechangeServices.getPieceRechange()
        if status:
            self.comboBoxComposants.clear()
            for rec in record:
                self.comboBoxComposants.addItem(rec[0]+" "+rec[1])

        self.selectedComposantsCodes=[]
        self.selectedComposantsLabels=[]
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
        Dialog.resize(702, 754)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
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
        self.labelRefEquip = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.labelRefEquip.setFont(font)
        self.labelRefEquip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelRefEquip.setObjectName("labelRefEquip")
        self.gridLayout.addWidget(self.labelRefEquip, 0, 2, 1, 1)
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
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditReference = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditReference.setFont(font)
        self.lineEditReference.setStyleSheet("border: 1px solid back;height:25px;margin-right:25px;")
        self.lineEditReference.setObjectName("lineEditReference")
        self.horizontalLayout_2.addWidget(self.lineEditReference)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEditDesignation = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditDesignation.setFont(font)
        self.lineEditDesignation.setStyleSheet("border: 1px solid back;height:25px;margin-right:25px;")
        self.lineEditDesignation.setObjectName("lineEditDesignation")
        self.horizontalLayout_7.addWidget(self.lineEditDesignation)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEditRole = QtWidgets.QLineEdit(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditRole.setFont(font)
        self.lineEditRole.setStyleSheet("border: 1px solid back;height:25px;margin-right:25px;")
        self.lineEditRole.setObjectName("lineEditRole")
        self.horizontalLayout_8.addWidget(self.lineEditRole)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEditFabriquant = QtWidgets.QLineEdit(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditFabriquant.setFont(font)
        self.lineEditFabriquant.setStyleSheet("border: 1px solid back;height:25px;margin-right:25px;")
        self.lineEditFabriquant.setObjectName("lineEditFabriquant")
        self.horizontalLayout_9.addWidget(self.lineEditFabriquant)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.frame_7)
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
        self.dateEditFabriquation = QtWidgets.QDateEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditFabriquation.setFont(font)
        self.dateEditFabriquation.setStyleSheet("border: 1px solid back;height:25px;")
        self.dateEditFabriquation.setObjectName("dateEditFabriquation")
        self.horizontalLayout_3.addWidget(self.dateEditFabriquation)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.dateEditMiseEnMarche = QtWidgets.QDateEdit(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditMiseEnMarche.setFont(font)
        self.dateEditMiseEnMarche.setStyleSheet("border: 1px solid back;height:25px;")
        self.dateEditMiseEnMarche.setObjectName("dateEditMiseEnMarche")
        self.horizontalLayout_4.addWidget(self.dateEditMiseEnMarche)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.frame_10)
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
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
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
        self.comboBoxComposants = QtWidgets.QComboBox(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxComposants.setFont(font)
        self.comboBoxComposants.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxComposants.setObjectName("comboBoxComposants")
        self.horizontalLayout_5.addWidget(self.comboBoxComposants)
        self.pushButtonAjoutComposant = QtWidgets.QPushButton(self.frame_11)
        self.pushButtonAjoutComposant.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAjoutComposant.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.pushButtonAjoutComposant.setObjectName("pushButtonAjoutComposant")
        self.horizontalLayout_5.addWidget(self.pushButtonAjoutComposant)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.labelListeComposants = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelListeComposants.setFont(font)
        self.labelListeComposants.setText("")
        self.labelListeComposants.setObjectName("labelListeComposants")
        self.horizontalLayout_10.addWidget(self.labelListeComposants)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.verticalLayout_3.addWidget(self.frame_14)
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
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.horizontalLayout_6.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.initialisationEquipement()
        self.buttonEnvoyer.clicked.connect(self.addEquipement)
        self.pushButtonAjoutComposant.clicked.connect(self.addComposant)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Manuel des Formulaires"))
        self.label.setText(_translate("Dialog", "FBC"))
        self.labelRefEquip.setText(_translate("Dialog", "FMS00101"))
        self.dateLiberation.setText(_translate("Dialog", "Date :"))
        self.label_4.setText(_translate("Dialog", "Equipement"))
        self.label_3.setText(_translate("Dialog", "Réference : "))
        self.label_5.setText(_translate("Dialog", "Designation : "))
        self.label_6.setText(_translate("Dialog", "Role : "))
        self.label_7.setText(_translate("Dialog", "Fabriquant : "))
        self.label_8.setText(_translate("Dialog", "Date Fabriquation"))
        self.dateEditFabriquation.setDisplayFormat(_translate("Dialog", "yyyy-M-d"))
        self.label_9.setText(_translate("Dialog", "Date Mise En Marche"))
        self.dateEditMiseEnMarche.setDisplayFormat(_translate("Dialog", "yyyy-M-d"))
        self.label_12.setText(_translate("Dialog", "Composants : "))
        self.pushButtonAjoutComposant.setText(_translate("Dialog", "Ajouter un Composant"))
        self.label_10.setText(_translate("Dialog", "Composants Ajoutées : "))
        self.buttonEnvoyer.setText(_translate("Dialog", "Envoyer"))
