from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from .MainWindow import Ui_MainWindow
from Models.ConnectionServices import UserConnection



class Ui_Dialog(object):
    def handleClick(self):
        matricule = self.lineEdit.text()
        password=self.lineEdit_2.text()

        Connection,record = UserConnection(matricule,password)

        if(Connection):
            self.window=QMainWindow()
            self.ui=Ui_MainWindow(record[0][0],record[0][2],self.d,self.window)
            self.ui.setupUi(self.window)
            self.resize()
            self.center()
            self.window.show()
            self.d.hide()
            self.ErrorLabel.setVisible(False)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            self.ErrorLabel.setVisible(True)
    def center(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
    def resize(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry()
        self.window.setMinimumSize(int(cp.width()*0.7),int(cp.height()*0.8))
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 640)
        Dialog.setStyleSheet("background-color : #22333B;\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color : #FEFDFC;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.Matricule = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.Matricule.setFont(font)
        self.Matricule.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Matricule.setObjectName("Matricule")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.Matricule)
        self.Password = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Password)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("width : 250px;height : 25px;\n"
"border: 1px solid back;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setStyleSheet("width : 250px;height : 25px;\n"
"border: 1px solid back;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ErrorLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("color : rgb(255, 0, 0);")
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.verticalLayout_4.addWidget(self.ErrorLabel)
        self.LogIn = QtWidgets.QPushButton(self.frame_2)
        self.LogIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LogIn.setStyleSheet("QPushButton{\n"
"height : 25px;\n"
"background-color :#00A8E8;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"};")
        self.LogIn.setObjectName("LogIn")
        self.verticalLayout_4.addWidget(self.LogIn)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMaximumSize(QtCore.QSize(769, 677))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/two-colleagues-factory.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frame_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.ErrorLabel.setVisible(False)
        self.d=Dialog
        self.LogIn.clicked.connect(self.handleClick)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log In"))
        self.label.setText(_translate("Dialog", "GMAO"))
        self.label_2.setText(_translate("Dialog", "Log In"))
        self.Matricule.setText(_translate("Dialog", "Matricule"))
        self.Password.setText(_translate("Dialog", "Password"))
        self.ErrorLabel.setText(_translate("Dialog", "Informations Incorrectes"))
        self.LogIn.setText(_translate("Dialog", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
