from PyQt4.QtGui import *
from PyQt4.QtCore import *

import editScreen
import loginScreen
import sqlOperations


class testerScreen(QDialog):

    def __init__(self, userName, title):
        super(testerScreen, self).__init__()
        self.userName = userName
        self.initUi(400, 350, 20)
        self.setWindowTitle(title)

    def initUi(self, winWidth, winHeight, winMargins):

        self.setMinimumSize(winWidth, winHeight)
        self.resize(winWidth, winHeight)

        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()

        self.listWidget = QListWidget()

        self.admins = QComboBox()
        self.admins.currentIndexChanged.connect(self.selectionChanged)
        admNames = sqlOperations.getAdmins()
        for nStr in admNames:
            self.admins.addItem(nStr)

        adminLabel = QLabel('Admin')

        comboBoxLayout = QHBoxLayout()
        comboBoxLayout.addWidget(adminLabel)
        comboBoxLayout.addWidget(self.admins)

        buttonLayout = QVBoxLayout()

        if(self.listWidget.count() > 0):
            self.listWidget.setCurrentRow(0)

        logoutButton = QPushButton('Logout')
        logoutButton.clicked.connect(self.logoutClick)

        welcomeLabel = QLabel('Welcome, ' + self.userName)

        userLogout = QHBoxLayout()
        userLogout.addWidget(welcomeLabel)
        userLogout.addStretch(1)
        userLogout.addWidget(logoutButton)

        removeButton = QPushButton('Edit')
        removeButton.clicked.connect(self.editClick)

        buttonLayout.addWidget(removeButton)
        buttonLayout.addStretch(1)
        buttonLayout.setContentsMargins(-1, winMargins, -1, -1)

        hLayout.addWidget(self.listWidget)
        hLayout.addLayout(buttonLayout)

        vLayout.addLayout(userLogout)
        vLayout.addWidget(self.admins)
        vLayout.addLayout(hLayout)

        self.setLayout(vLayout)

        self.show()

    def populateList(self):
        fstrings = sqlOperations.getStrings(self.fUser)

        for fstr in fstrings:
            item = QListWidgetItem(fstr)
            self.listWidget.addItem(item)

    def selectionChanged(self):
        self.listWidget.clear()
        self.fUser = str(self.admins.currentText())
        self.populateList()

    def editClick(self):
        item = self.listWidget.currentItem()

        text = ''

        if(not item):
            msgBox = QMessageBox()
            msgBox.setText('Unsuccessful')
            msgBox.setInformativeText('Please Select an item to edit')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
            return
        else:
            text = item.text()
            self.scrn2 = editScreen.editScreen(self.fUser,
                                               self.userName + " | Edit",
                                               str(text),
                                               self)

    def logoutClick(self):
        self.close()
        self.screen = loginScreen.loginScreen()
