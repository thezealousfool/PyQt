from PyQt4.QtGui import *
from PyQt4.QtCore import *

from sqlVerify import *
from welcomeScreen import *


class startScreen(QDialog):

    def __init__(self):
        super(startScreen, self).__init__()
        self.initUi()

    def initUi(self):

        idLabel = QLabel('User ID')
        passLabel = QLabel('Password')

        self.idField = QLineEdit()

        self.passField = QLineEdit()
        self.passField.setEchoMode(QLineEdit.Password)

        loginButton = QPushButton('Login')
        loginButton.clicked.connect(self.loginClick)
        loginButton.setDefault(True)
        loginButton.setAutoDefault(True)

        cancelButton = QPushButton('Cancel')
        cancelButton.clicked.connect(self.cancelClick)
        cancelButton.setDefault(False)
        cancelButton.setAutoDefault(True)

        vLayout = QVBoxLayout()
        vLayout.setSpacing(20)
        vLayout.setMargin(60)

        grid = QGridLayout()
        grid.setSpacing(20)
        grid.setVerticalSpacing(10)

        grid.addWidget(idLabel, 1, 0)
        grid.addWidget(self.idField, 1, 1)
        grid.addWidget(passLabel, 2, 0)
        grid.addWidget(self.passField, 2, 1)

        hLayout = QHBoxLayout()
        hLayout.setSpacing(20)
        hLayout.addStretch(1)
        hLayout.addWidget(cancelButton)
        hLayout.addWidget(loginButton)

        vLayout.addStretch(1)
        vLayout.addLayout(grid)
        vLayout.addLayout(hLayout)
        vLayout.addStretch(1)

        self.setLayout(vLayout)
        self.setWindowTitle('Login')
        self.setMinimumSize(800, 600)
        self.show()

    def loginClick(self):
        status = verifyUser(self.idField.text(), self.passField.text())

        if(status):
            self.close()
            self.screen = welcomeScreen()
        else:
            msgBox = QMessageBox()
            msgBox.setText('Login Failed.')
            msgBox.setInformativeText('User ID and/or Password do not match')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def cancelClick(self):
        self.close()
