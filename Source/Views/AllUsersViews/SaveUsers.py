from PyQt5 import QtCore, QtGui, QtWidgets
from Models.ConnectionServices import Registration
from PyQt5.QtWidgets import *

class Ui_Dialog(object):

    def showDialog(self,str,bool):
        msgBox = QMessageBox()
        if bool==False:
                msgBox.setIcon(QMessageBox.Warning)
        else:
                msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Advertissement")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def resetAll(self):
        self.e1.setText("")
        self.e2.setText("")
        self.e3.setText("")
        self.e4.setText("")
        self.e5.setText("")
        self.lineEdit.setText("")


    def adminInter(self):

        self.l4.setVisible(True)
        self.e4.setVisible(True)
        self.l4.setText("Mot de Passe")
        self.l5.setVisible(False)
        self.s1.setVisible(False)
        self.l6.setVisible(False)
        self.c1.setVisible(False)
        self.l7.setVisible(False)
        self.e5.setVisible(False)
        self.l8.setVisible(False)
        self.s2.setVisible(False)
        self.label_3.setVisible(False)
        self.lineEdit.setVisible(False)

    def ResponsInter(self):
        self.l4.setText("Réf Chaine")
        self.l4.setVisible(True)
        self.e4.setVisible(True)
        self.l5.setVisible(False)
        self.s1.setVisible(False)
        self.l6.setVisible(False)
        self.c1.setVisible(False)
        self.l7.setVisible(True)
        self.e5.setVisible(True)
        self.l7.setText("Mot de Passe")
        self.l8.setVisible(False)
        self.s2.setVisible(False)
        self.label_3.setVisible(False)
        self.lineEdit.setVisible(False)

    def AgentInter(self):
        self.l4.setVisible(True)
        self.e4.setVisible(True)
        self.l4.setText("Mot de Passe")
        self.l5.setVisible(True)
        self.s1.setVisible(True)
        self.l6.setVisible(True)
        self.c1.setVisible(True)
        self.l7.setVisible(True)
        self.e5.setVisible(True)
        self.l8.setVisible(True)
        self.s2.setVisible(True)
        self.label_3.setVisible(True)
        self.lineEdit.setVisible(True)
    

    def roleChanged(self):
        r=str(self.comboBox.currentText())
        if r=="Administrateur" or r=="Magasinier" or r=="Responsable Production":
                self.adminInter()
        if r=="Agent Maintenance":
                self.AgentInter()
        if r=="Responsable Maintenance" or r=="Responsable Chaine Production":
                self.ResponsInter()
   
    def addHim(self):
        #ordre: matricule-nom-prenom-role-MotDePasse-refchaine\specialite-age-sexe-niveaEsu-expProf
        r=str(self.comboBox.currentText())
        if r=="Administrateur":
            if self.e1.text()=="" or self.e2.text()=="" or self.e3.text()=="" or self.e4.text()=="":
                self.showDialog("Le remplissage de tout les champs est nécessaire !",False)
                return
            if len(self.e4.text())<8:
                self.showDialog("Mot De Passe Insuffisant !(8 Caracteres au minimum)",False)
                return    
            else:
                Registration(self.e1.text(),self.e2.text(),self.e3.text(),"Administrateur",self.e4.text())
                self.resetAll()
                self.showDialog("Enregistrement effectuée avec succées",True)
                return
        if r=="Magasinier":
           if self.e1.text()=="" or self.e2.text()=="" or self.e3.text()=="" or self.e4.text()=="":
                self.showDialog("Le remplissage de tout les champs est nécessaire !",False)
                return
           if len(self.e4.text())<8:
                self.showDialog("Mot De Passe Insuffisant !(8 Caracteres au minimum)",False)
                return     
           else:
                Registration(self.e1.text(),self.e2.text(),self.e3.text(),"Magasinier",self.e4.text())
                self.resetAll()
                self.showDialog("Enregistrement effectuée avec succées",True)
                return
        if r=="Responsable Production":
            if self.e1.text()=="" or self.e2.text()=="" or self.e3.text()=="" or self.e4.text()=="":
                self.showDialog("Le remplissage de tout les champs est nécessaire !",False)
                return
            if len(self.e4.text())<8:
                self.showDialog("Mot De Passe Insuffisant !(8 Caracteres au minimum)",False)
                return    
            else:
                Registration(self.e1.text(),self.e2.text(),self.e3.text(),"Responsable Production",self.e4.text())
                self.resetAll()
                self.showDialog("Enregistrement effectuée avec succées",True)
                return   
        if r=="Responsable Chaine Production":
            if self.e1.text()=="" or self.e2.text()=="" or self.e3.text()=="" or self.e4.text()=="" or self.e5.text()=="" :
                self.showDialog("Le remplissage de tout les champs est nécessaire !",False)
                return
            if len(self.e5.text())<8:
                self.showDialog("Mot De Passe Insuffisant !(8 Caracteres au minimum)",False)
                return
            else:
                x=Registration(self.e1.text(),self.e2.text(),self.e3.text(),"Responsable Chaine Production",self.e5.text(),self.e4.text())
                if x==0:
                        self.showDialog("Attention La chaine indiquée n'existe pas !",False)
                elif x==1:
                        self.resetAll()
                        self.showDialog("Enregistrement effectuée avec succées",True)
                        return 
        if r=="Responsable Maintenance":
            if self.e1.text()=="" or self.e2.text()=="" or self.e3.text()=="" or self.e4.text()=="" or self.e5.text()=="" :
                self.showDialog("Le remplissage de tout les champs est nécessaire !",False)
                return
            if len(self.e5.text())<8:
                self.showDialog("Mot De Passe Insuffisant !(8 Caracteres au minimum)",False)
                return
            else:
                x=Registration(self.e1.text(),self.e2.text(),self.e3.text(),"Responsable Maintenance",self.e5.text(),self.e4.text())
                if x==0:
                        self.showDialog("Attention La chaine indiquée n'existe pas !",False)
                else:
                        self.resetAll()
                        self.showDialog("Enregistrement effectuée avec succées",True)
                        return
        if r=="Agent Maintenance":
            if self.e1.text()=="" or self.e2.text()=="" or self.e3.text()=="" or self.e4.text()=="" or self.e5.text()=="":
                self.showDialog("Le remplissage de tout les champs est nécessaire !",False)
                return
            if self.s1.value()<18:
                self.showDialog("Age invalide !",False)
                return
            if len(self.e4.text())<8:
                self.showDialog("Mot De pAsse Insuffisant !(8 Caracteres au minimum)",False)
                return
            else:
                Registration(self.e1.text(),self.e2.text(),self.e3.text(),"Agent Maintenance",self.e4.text(),self.lineEdit.text(),self.s1.value(),self.c1.currentText(),self.e5.text(),self.s2.value())
                self.resetAll()
                self.showDialog("Enregistrement effectuée avec succées",True)
                return

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1111, 672)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color :#00A8E8;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(22)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("height:30")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        
        
       
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        
        self.l8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l8.setFont(font)
        self.l8.setObjectName("l8")
        self.gridLayout.addWidget(self.l8, 1, 6, 1, 1)
        self.l1 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)
        self.l2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 0, 2, 1, 1)
        self.l3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 0, 4, 1, 1)
        self.l5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.gridLayout.addWidget(self.l5, 1, 0, 1, 1)
        
        
        self.l4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.gridLayout.addWidget(self.l4, 0, 6, 1, 1)

        ###################Ordering####################
        self.e1 = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.e1.setFont(font)
        self.e1.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}\n"
"")
        self.e1.setObjectName("e1")
        self.gridLayout.addWidget(self.e1, 0, 1, 1, 1)
        ##########
        self.e2 = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.e2.setFont(font)
        self.e2.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}\n"
"")
        self.e2.setObjectName("e2")
        self.gridLayout.addWidget(self.e2, 0, 3, 1, 1)
        ##########
        self.e3 = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.e3.setFont(font)
        self.e3.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}\n"
"")
        self.e3.setObjectName("e3")
        self.gridLayout.addWidget(self.e3, 0, 5, 1, 1)
        ##########
        self.e4 = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.e4.setFont(font)
        self.e4.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}\n"
"")
        self.e4.setObjectName("e4")
        self.gridLayout.addWidget(self.e4, 0, 7, 1, 1)
        ##########
        self.s1 = QtWidgets.QSpinBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.s1.setFont(font)
        self.s1.setStyleSheet("QSpinBox,QComboBox{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QSpinBox:focus{\n"
"border:1.5px solid\n"
"}")
        self.s1.setObjectName("s1")
        self.gridLayout.addWidget(self.s1, 1, 1, 1, 1)
        ##########
        self.c1 = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.c1.setFont(font)
        self.c1.setStyleSheet("QSpinBox,QComboBox{\n"
"border-style: outset;\n"
"background-color:white;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QSpinBox:focus{\n"
"border:1.5px solid\n"
"}\n"
"QComboBox:focus{\n"
"border:1.5px solid\n"
"}")
        self.c1.setObjectName("c1")
        self.c1.addItem("")
        self.c1.addItem("")
        self.gridLayout.addWidget(self.c1, 1, 3, 1, 1)
        ##########
        self.e5 = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.e5.setFont(font)
        self.e5.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}")
        self.e5.setObjectName("e5")
        self.gridLayout.addWidget(self.e5, 1, 5, 1, 1)
        ##########
        self.s2 = QtWidgets.QSpinBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.s2.setFont(font)
        self.s2.setStyleSheet("QSpinBox,QComboBox{\n"
"border-style: outset;\n"
"background-color:white;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QSpinBox:focus{\n"
"border:1.5px solid\n"
"}\n"
"QComboBox:focus{\n"
"border:1.5px solid\n"
"}")
        self.s2.setObjectName("s2")
        self.gridLayout.addWidget(self.s2, 1, 7, 1, 1)
        ##########
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-style: outset;\n"
"background-color:white;\n"
"border-radius: 7px;\n"
"height:30;\n"
"border:0.5px solid\n"
"}\n"
"QLineEdit:focus{\n"
"border:1.5px solid\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        ##########
        self.l6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l6.setFont(font)
        self.l6.setObjectName("l6")
        self.gridLayout.addWidget(self.l6, 1, 2, 1, 1)
        
        self.l7 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l7.setFont(font)
        self.l7.setObjectName("l7")
        self.gridLayout.addWidget(self.l7, 1, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.l4.setVisible(True)
        self.e4.setVisible(True)
        self.l5.setVisible(False)
        self.s1.setVisible(False)
        self.l6.setVisible(False)
        self.c1.setVisible(False)
        self.l7.setVisible(False)
        self.e5.setVisible(False)
        self.l8.setVisible(False)
        self.s2.setVisible(False)
        self.label_3.setVisible(False)
        self.lineEdit.setVisible(False)
        self.comboBox.currentTextChanged.connect(self.roleChanged)
        self.pushButton.clicked.connect(self.addHim)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enregistrement"))
        self.label_2.setText(_translate("Dialog", "Rôle"))
        self.comboBox.setItemText(0, _translate("Dialog", "Administrateur"))
        self.comboBox.setItemText(1, _translate("Dialog", "Responsable Production"))
        self.comboBox.setItemText(2, _translate("Dialog", "Responsable Chaine Production"))
        self.comboBox.setItemText(3, _translate("Dialog", "Responsable Maintenance"))
        self.comboBox.setItemText(4, _translate("Dialog", "Agent Maintenance"))
        self.comboBox.setItemText(5, _translate("Dialog", "Magasinier"))
        self.label_3.setText(_translate("Dialog", "Spécialité"))
        self.l8.setText(_translate("Dialog", "  Expérience Prof"))
        self.l1.setText(_translate("Dialog", "Matricule"))
        self.l2.setText(_translate("Dialog", "Nom    "))
        self.l3.setText(_translate("Dialog", "Prenom"))
        self.l5.setText(_translate("Dialog", "Age"))
        self.l4.setText(_translate("Dialog", "Mot de Passe"))
        self.l6.setText(_translate("Dialog", "Sexe"))
        self.c1.setItemText(0, _translate("Dialog", "Mâle"))
        self.c1.setItemText(1, _translate("Dialog", "Femelle"))
        self.l7.setText(_translate("Dialog", "Niv. éducation"))
        self.pushButton.setText(_translate("Dialog", "Valider"))
