# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demandeInterventionConsulter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1014, 811)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setPixmap(QPixmap(u":/icons/icons/request.png"))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color:transparent;\n"
"border : none;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.ButtonConsulter = QPushButton(self.frame_4)
        self.ButtonConsulter.setObjectName(u"ButtonConsulter")
        self.ButtonConsulter.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonConsulter.setStyleSheet(u"QPushButton{\n"
"height : 20px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.horizontalLayout_2.addWidget(self.ButtonConsulter)

        self.ButtonImprimer = QPushButton(self.frame_4)
        self.ButtonImprimer.setObjectName(u"ButtonImprimer")
        self.ButtonImprimer.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonImprimer.setStyleSheet(u"QPushButton{\n"
"height : 20px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"};")

        self.horizontalLayout_2.addWidget(self.ButtonImprimer)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.tableViewDemandeIntervention = QTableView(self.frame)
        self.tableViewDemandeIntervention.setObjectName(u"tableViewDemandeIntervention")

        self.verticalLayout_3.addWidget(self.tableViewDemandeIntervention)


        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma,Calibri,Helvetica'; font-size:10pt; font-weight:600; color:#888888;\">Les pi\u00e8ces sont une liste non seulement de ce que vous avez, mais aussi de ce que vous devriez avoir.\u00a0Pour mettre les choses en perspective, vous pourriez avoir une entr\u00e9e pour des ampoules de 60 watts, mais n'en avoir aucune en stock.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma,Calibri,Helvetica'; font-size"
                        ":10pt; font-weight:600; color:#888888;\">Garder une liste exhaustive des pi\u00e8ces servira son objectif lorsque vous devrez passer des commandes.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Actions :", None))
        self.ButtonConsulter.setText(QCoreApplication.translate("Dialog", u"Consulter en d\u00e9taille", None))
        self.ButtonImprimer.setText(QCoreApplication.translate("Dialog", u"Imprimer", None))
    # retranslateUi

