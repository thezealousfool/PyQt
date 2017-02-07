from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlOperations
import adminScreen


class loginScreen(QDialog):

    def __init__(self):
        super(loginScreen, self).__init__()
        self.initUi(400, 350, 20)

    def initUi(self, winWidth, winHeight, winMargins):

        self.setWindowTitle('Login')
        self.setMinimumSize(winWidth, winHeight)
        self.resize(winWidth, winHeight)

        vLayout = QVBoxLayout()
        vLayout.setSpacing(winMargins)
        vLayout.setMargin(2 * winMargins)

        logo = QLabel('')
        logoPixmap = QPixmap('logo.png')
        logoPixmap = logoPixmap.scaledToWidth(self.width() - 4 * winMargins)
        logo.setPixmap(logoPixmap)

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

        grid = QGridLayout()
        grid.setSpacing(winMargins)

        grid.addWidget(idLabel, 1, 0)
        grid.addWidget(self.idField, 1, 1)
        grid.addWidget(passLabel, 2, 0)
        grid.addWidget(self.passField, 2, 1)

        buttonGroup = QHBoxLayout()
        buttonGroup.setSpacing(winMargins)
        buttonGroup.addStretch(1)
        buttonGroup.addWidget(cancelButton)
        buttonGroup.addWidget(loginButton)

        logoLayout = QHBoxLayout()
        logoLayout.addStretch(1)
        logoLayout.addWidget(logo)
        logoLayout.addStretch(1)

        vLayout.addStretch(1)
        vLayout.addLayout(logoLayout)
        vLayout.addStretch(1)
        vLayout.addLayout(grid)
        vLayout.addStretch(1)
        vLayout.addLayout(buttonGroup)
        vLayout.addStretch(1)

        self.setLayout(vLayout)
        self.show()

    def loginClick(self):
        status = sqlOperations.verifyUser(str(self.idField.text()), str(self.passField.text()))

        if(status == -1):
            msgBox = QMessageBox()
            msgBox.setText('Login Failed.')
            msgBox.setInformativeText('User ID and/or Password do not match')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
        elif(status == 1):
            self.close()
            name = str(self.idField.text())
            self.screen = adminScreen.adminScreen(name, name + ' | Add Field')

    def cancelClick(self):
        self.close()
