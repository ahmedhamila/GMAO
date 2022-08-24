from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from .DemandeIntervention import Ui_Dialog as DemandeIntervention_UI
from PyQt5.QtWidgets import QMessageBox
from .DemandeInterventionModify import Ui_Dialog as DemandeIntervention_Modif_UI
from Services.DemandeInterventionServices import getDemandeInterventionListRCP,deleteDemandeIntervention

class Ui_Dialog(object):
    def setColortoRow(self,table, rowIndex, color):
        for j in range(table.columnCount()):
                table.item(rowIndex, j).setBackground(color)
    def getSelectedRow(self):
        rows=[]
        for row in range(self.tableWidgetDemandeIntervention.rowCount()):
                if self.tableWidgetDemandeIntervention.item(row,0).checkState()==QtCore.Qt.CheckState.Checked:
                        rows.append(self.tableWidgetDemandeIntervention.item(row,0).text())
        return rows
    def modifierDemandeIntervention(self):
        ids=self.getSelectedRow()
        if len(ids)>1:
                self.showDialog("Error","Impossible d'effectuer cette action sur plus d'une ligne",False)
                return 
        if len(ids)<1:
                self.showDialog("Error","Il faut selectionner une ligne",False)
                return 
        self.RedirectDemandeInterventionModify(ids[0])
    def RedirectDemandeInterventionModify(self,id):
        self.dialogDemandeIntervention = QtWidgets.QDialog()
        self.uiDemandeIntervention = DemandeIntervention_Modif_UI(self.mainWindowSelf,id,self.DemandeInterventionDLG,self)
        self.uiDemandeIntervention.setupUi(self.dialogDemandeIntervention)
        self.mainWindowSelf.stackedWidget.addWidget(self.dialogDemandeIntervention)
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.dialogDemandeIntervention)

    def supprimerDemandeIntervention(self):
        ids=self.getSelectedRow()
        if len(ids)<1:
                self.showDialog("Error","Il faut selectionner au moins une ligne",False)
                return 
        deleteDemandeIntervention(ids)
        self.fetchRows()

    def imprimerDemandeIntervention(self):
        ids=self.getSelectedRow()
        if len(ids)<1:
                self.showDialog("Error","Il faut selectionner au moins une ligne",False)
                return 

    def fetchRows(self):
        status,record = getDemandeInterventionListRCP(self.mainWindowSelf.matricule)
        if status :
                self.tableWidgetDemandeIntervention.setColumnCount(9)
                self.tableWidgetDemandeIntervention.setHorizontalHeaderLabels(['Id','Matricule de Responsable Chaine Production',"Matricule de Responsable Maintenance","Code Equipement","Section","Date","Motif","Description","Status"])
                self.tableWidgetDemandeIntervention.setRowCount(len(record))

                self.horizontal_header = self.tableWidgetDemandeIntervention.horizontalHeader()     
                self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
                self.horizontal_header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
                self.horizontal_header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
                
                for row in range(len(record)):
                        for col in range(9):
                                item=QtWidgets.QTableWidgetItem(str(record[row][col]))
                                self.tableWidgetDemandeIntervention.setItem(row,col,item)
                                if col ==0:
                                        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                                        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                        if str(record[row][8])=="Traitee":
                                self.setColortoRow(self.tableWidgetDemandeIntervention,row,QColor(202,225,183))
                        if str(record[row][8])=="NonTraitee":
                                self.setColortoRow(self.tableWidgetDemandeIntervention,row,QColor(246,173,158))



    def RedirectDemandeIntervention(self):
        self.dialogDemandeIntervention = QtWidgets.QDialog()
        self.uiDemandeIntervention = DemandeIntervention_UI(self.mainWindowSelf)
        self.uiDemandeIntervention.setupUi(self.dialogDemandeIntervention)
        self.mainWindowSelf.stackedWidget.addWidget(self.dialogDemandeIntervention)
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.dialogDemandeIntervention)
    def __init__(self,mainWindowSelf,DemandeInterventionDLG) -> None:
        self.mainWindowSelf=mainWindowSelf
        self.DemandeInterventionDLG=DemandeInterventionDLG
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
        Dialog.resize(1014, 813)
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
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/request.png"))
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
        self.ButtonCreerDemandeIntervention = QtWidgets.QPushButton(self.frame_3)
        self.ButtonCreerDemandeIntervention.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonCreerDemandeIntervention.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonCreerDemandeIntervention.setObjectName("ButtonCreerDemandeIntervention")
        self.verticalLayout_2.addWidget(self.ButtonCreerDemandeIntervention)
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
        self.tableWidgetDemandeIntervention = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetDemandeIntervention.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetDemandeIntervention.setRowCount(0)
        self.tableWidgetDemandeIntervention.setColumnCount(0)
        self.tableWidgetDemandeIntervention.setObjectName("tableWidgetDemandeIntervention")
        self.verticalLayout_3.addWidget(self.tableWidgetDemandeIntervention)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.ButtonCreerDemandeIntervention.clicked.connect(self.RedirectDemandeIntervention)
        self.fetchRows()
        self.ButtonModifier.clicked.connect(self.modifierDemandeIntervention)
        self.ButtonSupprimer.clicked.connect(self.supprimerDemandeIntervention)
        self.ButtonImprimer.clicked.connect(self.imprimerDemandeIntervention)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:10pt; font-weight:600; color:#888888;\">Les pièces sont une liste non seulement de ce que vous avez, mais aussi de ce que vous devriez avoir. Pour mettre les choses en perspective, vous pourriez avoir une entrée pour des ampoules de 60 watts, mais n\'en avoir aucune en stock.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:10pt; font-weight:600; color:#888888;\">Garder une liste exhaustive des pièces servira son objectif lorsque vous devrez passer des commandes.</span></p></body></html>"))
        self.ButtonCreerDemandeIntervention.setText(_translate("Dialog", "Créer une Demande d\'Intervention"))
        self.label.setText(_translate("Dialog", "Actions :"))
        self.ButtonModifier.setText(_translate("Dialog", "Modifier"))
        self.ButtonSupprimer.setText(_translate("Dialog", "Supprimer"))
        self.ButtonImprimer.setText(_translate("Dialog", "Imprimer"))

