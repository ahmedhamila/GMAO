# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterventionMecanicien.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1036, 846)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #1A2930;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Modern No. 20")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(14)
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"border: 1px solid back;\n"
"height:25px;")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet(u"border: 1px solid back;height:25px;")

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 3, 1, 1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color : #FEFDFC;")

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color : #FEFDFC;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout.addWidget(self.label_12)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Manuel des formulaires", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"FBC", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Document : FMS00702", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Fiche d'intervention pour M\u00e9canicien", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"    Date :", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Pr\u00e9nom :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Nom :", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Matricule :", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Date : ", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"R\u00e9daction : Mlle Laagab Soumaya", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"V\u00e9rification : Responsable du Service", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Approbation : Le g\u00e9rant", None))
    # retranslateUi

