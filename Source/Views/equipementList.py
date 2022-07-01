from PyQt5 import QtCore, QtGui, QtWidgets
#from .Equipement import Equipement_UI

class Ui_Dialog(object):
    '''def RedirectEquipement(self):
        self.dialogEquipement = QtWidgets.QDialog()
        self.uiEquipement = Equipement_UI()
        self.uiEquipement.setupUi(self.dialogEquipement)
        self.mainWindowSelf.stackedWidget.addWidget(self.dialogEquipement)
        self.mainWindowSelf.stackedWidget.setCurrentWidget(self.dialogEquipement)'''
    def __init__(self,mainWindowSelf) -> None:
        self.mainWindowSelf=mainWindowSelf
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1018, 810)
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
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/service.png"))
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
        self.ButtonCreerEquipement = QtWidgets.QPushButton(self.frame_3)
        self.ButtonCreerEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonCreerEquipement.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.ButtonCreerEquipement.setObjectName("ButtonCreerEquipement")
        self.verticalLayout_2.addWidget(self.ButtonCreerEquipement)
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
        self.verticalLayout_3.addWidget(self.frame_4)
        self.tableViewEquipement = QtWidgets.QTableView(self.frame)
        self.tableViewEquipement.setObjectName("tableViewEquipement")
        self.verticalLayout_3.addWidget(self.tableViewEquipement)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Calibri,Helvetica\'; font-size:12pt; font-weight:600; color:#888888;\">Les équipements sont au cœur de toute GMAO. Sans équipements, vous n\'avez rien sur quoi exécuter la maintenance ! Vous pouvez créer des actifs individuellement ou les importer à partir d\'un fichier de feuille de calcul.</span></p></body></html>"))
        self.ButtonCreerEquipement.setText(_translate("Dialog", "Ajouter un Equipement"))
        self.label.setText(_translate("Dialog", "Actions :"))
        self.ButtonModifier.setText(_translate("Dialog", "Modifier"))
        self.ButtonSupprimer.setText(_translate("Dialog", "Supprimer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
