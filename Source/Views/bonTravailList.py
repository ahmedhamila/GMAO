from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from .BonTravail import Ui_Dialog as Bontravail_UI
from .BonTravailModify import Ui_Dialog as BonTravail_Modif_UI
from Models.BonTravailServices import getBonTravailList,deleteBonTravail
class Ui_Dialog(object):
    def getSelectedRow(self):
        rows=[]
        for row in range(self.tableWidgetBonTravail.rowCount()):
                if self.tableWidgetBonTravail.item(row,0).checkState()==QtCore.Qt.CheckState.Checked:
                        rows.append(self.tableWidgetBonTravail.item(row,0).text())
        return rows
    def modifierBonTravial(self):
        ids=self.getSelectedRow()
        if len(ids)>1:
                self.showDialog("Error","Impossible d'effectuer cette action sur plus d'une ligne",False)
                return 
        if len(ids)<1:
                self.showDialog("Error","Il faut selectionner une ligne",False)
                return 
        self.RedirectBonTravailModify(ids[0])
    def RedirectBonTravailModify(self,id):
        self.dialogBonTravail = QtWidgets.QDialog()
        self.uiBonTravail = BonTravail_Modif_UI(self.mainWindowSelf,id,self.BonTravailDLG,self)
        self.uiBonTravail.setupUi(self.dialogBonTravail)
        self.mainWindowSelf.stackedWidget.addWidget(self.dialogBonTravail)
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.dialogBonTravail)
    def supprimerbonTravail(self):
        ids=self.getSelectedRow()
        if len(ids)<1:
                self.showDialog("Error","Il faut selectionner au moins une ligne",False)
                return 
        deleteBonTravail(ids)
        self.fetchRows()
    def imprimerBonTravail(self):
        ids=self.getSelectedRow()
        if len(ids)<1:
                self.showDialog("Error","Il faut selectionner au moins une ligne",False)
                return 
    def fetchRows(self):
        status,record = getBonTravailList(self.mainWindowSelf.matricule)
        if status :
                self.tableWidgetBonTravail.setColumnCount(11)
                self.tableWidgetBonTravail.setHorizontalHeaderLabels(['Id','Matricule de Responsable',"Matricule de l'agent","Description","Section","Date","Type","Code equipement","RefDIM","Frequence","Active"])
                self.tableWidgetBonTravail.setRowCount(len(record))

                self.horizontal_header = self.tableWidgetBonTravail.horizontalHeader()     
                self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
                for row in range(len(record)):
                        for col in range(11):
                                if col==10 :
                                        item=QtWidgets.QTableWidgetItem('False' if record[row][col]==0 else 'True')
                                        self.tableWidgetBonTravail.setItem(row,col,item)
                                else :
                                        item=QtWidgets.QTableWidgetItem(str(record[row][col]))
                                        self.tableWidgetBonTravail.setItem(row,col,item)
                                if col ==0:
                                        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                                        item.setCheckState(QtCore.Qt.CheckState.Unchecked) 

    def RedirectBonTravail(self):
        self.dialogBonTravail = QtWidgets.QDialog()
        self.uiBonTravail = Bontravail_UI(self.mainWindowSelf)
        self.uiBonTravail.setupUi(self.dialogBonTravail)
        self.mainWindowSelf.stackedWidget.addWidget(self.dialogBonTravail)
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.dialogBonTravail)

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

    def __init__(self,mainWindowSelf,bontravdlg) -> None:
        self.mainWindowSelf=mainWindowSelf
        self.BonTravailDLG=bontravdlg
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1015, 811)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/pencil.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setStyleSheet("background-color:transparent;\n"
"border : none;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.ButtonCreerBonTravail = QtWidgets.QPushButton(self.frame_3)
        self.ButtonCreerBonTravail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonCreerBonTravail.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonCreerBonTravail.setObjectName("ButtonCreerBonTravail")
        self.verticalLayout_2.addWidget(self.ButtonCreerBonTravail)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ButtonModifier = QtWidgets.QPushButton(self.frame_4)
        self.ButtonModifier.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonModifier.setStyleSheet("QPushButton{\n"
"height : 20px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonModifier.setObjectName("ButtonModifier")
        self.horizontalLayout_2.addWidget(self.ButtonModifier)
        self.ButtonSupprimer = QtWidgets.QPushButton(self.frame_4)
        self.ButtonSupprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonSupprimer.setStyleSheet("QPushButton{\n"
"height : 20px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonSupprimer.setObjectName("ButtonSupprimer")
        self.horizontalLayout_2.addWidget(self.ButtonSupprimer)
        self.ButtonImprimer = QtWidgets.QPushButton(self.frame_4)
        self.ButtonImprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonImprimer.setStyleSheet("QPushButton{\n"
"height : 20px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonImprimer.setObjectName("ButtonImprimer")
        self.horizontalLayout_2.addWidget(self.ButtonImprimer)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.tableWidgetBonTravail = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetBonTravail.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetBonTravail.setRowCount(0)
        self.tableWidgetBonTravail.setColumnCount(0)
        self.tableWidgetBonTravail.setObjectName("tableWidgetBonTravail")
        self.verticalLayout_3.addWidget(self.tableWidgetBonTravail)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        self.ButtonCreerBonTravail.clicked.connect(self.RedirectBonTravail)

        self.fetchRows()
        self.ButtonModifier.clicked.connect(self.modifierBonTravial)
        self.ButtonSupprimer.clicked.connect(self.supprimerbonTravail)
        self.ButtonImprimer.clicked.connect(self.imprimerBonTravail)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:12pt; font-weight:600; color:#888888;\">Les ordres de travail sont utilisés pour suivre l\'activité de maintenance. Contrairement à la maintenance planifiée, les ordres de travail sont généralement destinés à la maintenance réactive, c\'est-à-dire à réparer quelque chose qui s\'est mal passé de manière inattendue. (demo text à changer)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:12pt; font-weight:600; color:#888888;\">Si vous suivez l\'ensemble de votre maintenance, même les travaux qui semblent insignifiants, vous serez surpris de l\'utilité de ces informations sur toute la ligne.</span></p></body></html>"))
        self.ButtonCreerBonTravail.setText(_translate("Dialog", "Créer un Bon de Travail"))
        self.label.setText(_translate("Dialog", "Actions :"))
        self.ButtonModifier.setText(_translate("Dialog", "Modifier"))
        self.ButtonSupprimer.setText(_translate("Dialog", "Supprimer"))
        self.ButtonImprimer.setText(_translate("Dialog", "Imprimer"))

