
        self.window=QDialog()
        self.ui=LogIn()
        self.ui.setupUi(self.window)
        self.resize()
        self.center()
        self.window.show()    
        
    def center(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
    def resize(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry()
        self.window.setMinimumSize(int(cp.width()*0.6),int(cp.height()*0.7))

app=QtWidgets.QApplication(sys.argv)
window=Main()
app.exec_()