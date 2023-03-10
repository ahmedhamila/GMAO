from PyQt5 import QtCore, QtGui, QtWidgets

from Services.BonApproServices import getBonApproList
from .BonApprovisionnement import Ui_Dialog as BonApprovisionment_UI
class Ui_Dialog(object):

    def setColortoRow(self,table, rowIndex, color):
        for j in range(table.columnCount()):
                table.item(rowIndex, j).setBackground(color)
    def getSelectedRow(self):
        rows=[]
        for row in range(self.tableWidgetBonTravail.rowCount()):
                if self.tableWidgetBonTravail.item(row,0).checkState()==QtCore.Qt.CheckState.Checked:
                        rows.append(self.tableWidgetBonTravail.item(row,0).text())
        return rows
    def fetchRows(self):
        status,record = getBonApproList()
        if status :
                self.tableWidgetBonTravail.setColumnCount(5)
                self.tableWidgetBonTravail.setHorizontalHeaderLabels(['Id','Matricule de Responsable Maintenance',"Matricule de Magasinier","Date Liberation","Description"])
                self.tableWidgetBonTravail.setRowCount(len(record))
                self.horizontal_header = self.tableWidgetBonTravail.horizontalHeader()     
                self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

                for row in range(len(record)):
                        for col in range(12):
                                item=QtWidgets.QTableWidgetItem(str(record[row][col]))
                                self.tableWidgetBonTravail.setItem(row,col,item)
                                if col ==0:
                                        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                                        item.setCheckState(QtCore.Qt.CheckState.Unchecked) 
                        if str(record[row][11])=="Traitee":
                                self.setColortoRow(self.tableWidgetBonTravail,row,QColor(202,225,183))
                        if str(record[row][11])=="NonTraitee":
                                self.setColortoRow(self.tableWidgetBonTravail,row,QColor(246,173,158))

    def RedirectBonApprovisionment(self):
        self.dialogBonApprovisionment = QtWidgets.QDialog()
        self.uiBonApprovisionment = BonApprovisionment_UI()
        self.uiBonApprovisionment.setupUi(self.dialogBonApprovisionment)
        self.mainWindowSelf.stackedWidget.addWidget(self.dialogBonApprovisionment)
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.dialogBonApprovisionment)
    def __init__(self,mainWindowSelf) -> None:
        self.mainWindowSelf=mainWindowSelf
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1014, 811)
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
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/cargo.png"))
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
        self.ButtonCreerBonApprovisonnement = QtWidgets.QPushButton(self.frame_3)
        self.ButtonCreerBonApprovisonnement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonCreerBonApprovisonnement.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonCreerBonApprovisonnement.setObjectName("ButtonCreerBonApprovisonnement")
        self.verticalLayout_2.addWidget(self.ButtonCreerBonApprovisonnement)
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
        self.tableViewBonTravail = QtWidgets.QTableView(self.frame)
        self.tableViewBonTravail.setObjectName("tableViewBonTravail")
        self.verticalLayout_3.addWidget(self.tableViewBonTravail)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.ButtonCreerBonApprovisonnement.clicked.connect(self.RedirectBonApprovisionment)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:10pt; font-weight:600; color:#888888;\">Les pi??ces sont une liste non seulement de ce que vous avez, mais aussi de ce que vous devriez avoir.??Pour mettre les choses en perspective, vous pourriez avoir une entr??e pour des ampoules de 60 watts, mais n\'en avoir aucune en stock.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:10pt; font-weight:600; color:#888888;\">Garder une liste exhaustive des pi??ces servira son objectif lorsque vous devrez passer des commandes.</span></p></body></html>"))
        self.ButtonCreerBonApprovisonnement.setText(_translate("Dialog", "Cr??er un Bon d\'Approvisionnement"))
        self.label.setText(_translate("Dialog", "Actions :"))
        self.ButtonModifier.setText(_translate("Dialog", "Modifier"))
        self.ButtonSupprimer.setText(_translate("Dialog", "Supprimer"))
        self.ButtonImprimer.setText(_translate("Dialog", "Imprimer"))

