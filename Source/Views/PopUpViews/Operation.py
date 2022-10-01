from PyQt5 import QtCore, QtGui, QtWidgets
from Services import OperationServices,PieceRechangeServices,LubrificationServices
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
    def initialiseOperation(self):
        state,record = PieceRechangeServices.getPieceRechange()
        self.comboBoxPieceRechange.clear()
        if state :
            for rec in record :
                self.comboBoxPieceRechange.addItem(rec[0]+" "+rec[1])

        state,record = LubrificationServices.getLubrification()
        self.comboBoxLubrification.clear()
        if state :
            for rec in record :
                self.comboBoxLubrification.addItem(rec[0]+" "+rec[1])
        
        self.selectedPieceRechangeCodes=[]
        self.selectedLubrificationCodes=[]

        self.selectedPieceRechangeLabels=[]
        self.selectedLubrificationLabels=[]
    def addPieceRechange(self):
        self.selectedPieceRechangeCodes.append(self.comboBoxPieceRechange.currentText().split(" ")[0])

        self.selectedPieceRechangeLabels.append(self.comboBoxPieceRechange.currentText().split(" ")[1])
        self.labelListePiecesRechanges.setText(",".join(list(set(self.selectedPieceRechangeLabels))))

    def addLubrification(self):
        self.selectedLubrificationCodes.append(self.comboBoxLubrification.currentText().split(" ")[0])

        self.selectedLubrificationLabels.append(self.comboBoxLubrification.currentText().split(" ")[1])
        self.labelListeLubrifications.setText(",".join(list(set(self.selectedLubrificationLabels))))

    def addOperation(self):
        titre=self.lineEditTitre.text()
        mode=self.textEdiModeOperatoire.toPlainText()


        OperationServices.addOperation((titre,mode))



        state,record = OperationServices.getOperation()
        self.bonTravailSelf.comboBoxOperation.clear()
        if state :
            for rec in record :
                self.bonTravailSelf.comboBoxOperation.addItem("Titre d'Operation: " +rec[1])

        status,record=OperationServices.getOperationRec((titre,mode))
        for lubri in self.selectedLubrificationCodes :
                LubrificationServices.addLubrificationOper((record[0][0],lubri))
        for piece in self.selectedPieceRechangeCodes :
                PieceRechangeServices.addPieceRechangeOper((record[0][0],piece))

        self.showDialog("Success","Operation Ajoutée avec succé",True)

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
        Dialog.resize(776, 752)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditTitre = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditTitre.setFont(font)
        self.lineEditTitre.setStyleSheet("border: 1px solid back;height:25px;margin-right:25px;")
        self.lineEditTitre.setText("")
        self.lineEditTitre.setObjectName("lineEditTitre")
        self.horizontalLayout_2.addWidget(self.lineEditTitre)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
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
        self.textEdiModeOperatoire = QtWidgets.QTextEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdiModeOperatoire.setFont(font)
        self.textEdiModeOperatoire.setStyleSheet("border : 1px solid black;")
        self.textEdiModeOperatoire.setObjectName("textEdiModeOperatoire")
        self.verticalLayout_2.addWidget(self.textEdiModeOperatoire)
        self.verticalLayout_5.addWidget(self.frame_9)
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
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.comboBoxPieceRechange = QtWidgets.QComboBox(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxPieceRechange.setFont(font)
        self.comboBoxPieceRechange.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxPieceRechange.setObjectName("comboBoxPieceRechange")
        self.horizontalLayout_7.addWidget(self.comboBoxPieceRechange)
        self.pushButtonAjoutPieceRechange = QtWidgets.QPushButton(self.frame_12)
        self.pushButtonAjoutPieceRechange.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAjoutPieceRechange.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.pushButtonAjoutPieceRechange.setObjectName("pushButtonAjoutPieceRechange")
        self.horizontalLayout_7.addWidget(self.pushButtonAjoutPieceRechange)
        self.horizontalLayout_7.setStretch(1, 3)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_15 = QtWidgets.QFrame(self.frame_5)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.labelListePiecesRechanges = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelListePiecesRechanges.setFont(font)
        self.labelListePiecesRechanges.setText("")
        self.labelListePiecesRechanges.setObjectName("labelListePiecesRechanges")
        self.horizontalLayout_11.addWidget(self.labelListePiecesRechanges)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.verticalLayout_4.addWidget(self.frame_15)
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
        self.comboBoxLubrification = QtWidgets.QComboBox(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxLubrification.setFont(font)
        self.comboBoxLubrification.setStyleSheet("border: 1px solid back;height:25px;")
        self.comboBoxLubrification.setObjectName("comboBoxLubrification")
        self.horizontalLayout_5.addWidget(self.comboBoxLubrification)
        self.pushButtonAjoutLubrification = QtWidgets.QPushButton(self.frame_11)
        self.pushButtonAjoutLubrification.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAjoutLubrification.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.pushButtonAjoutLubrification.setObjectName("pushButtonAjoutLubrification")
        self.horizontalLayout_5.addWidget(self.pushButtonAjoutLubrification)
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
        self.labelListeLubrifications = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelListeLubrifications.setFont(font)
        self.labelListeLubrifications.setText("")
        self.labelListeLubrifications.setObjectName("labelListeLubrifications")
        self.horizontalLayout_10.addWidget(self.labelListeLubrifications)
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
        self.verticalLayout.setStretch(4, 2)
        self.horizontalLayout_6.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.initialiseOperation()
        self.buttonEnvoyer.clicked.connect(self.addOperation)
        self.pushButtonAjoutPieceRechange.clicked.connect(self.addPieceRechange)
        self.pushButtonAjoutLubrification.clicked.connect(self.addLubrification)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Opération"))
        self.label_2.setText(_translate("Dialog", "Manuel des Formulaires"))
        self.label_3.setText(_translate("Dialog", "Titre : "))
        self.label_5.setText(_translate("Dialog", "Mode opératoire : "))
        self.label_13.setText(_translate("Dialog", "Pièces De Rechanges : "))
        self.pushButtonAjoutPieceRechange.setText(_translate("Dialog", "Ajouter une pièce"))
        self.label_11.setText(_translate("Dialog", "Pièces De Rechanges Ajoutées : "))
        self.label_12.setText(_translate("Dialog", "Lubrifications : "))
        self.pushButtonAjoutLubrification.setText(_translate("Dialog", "Ajouter une lubrification"))
        self.label_10.setText(_translate("Dialog", "Lubrifications Ajoutées : "))
        self.buttonEnvoyer.setText(_translate("Dialog", "Envoyer"))
