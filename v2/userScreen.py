from PyQt4.QtGui import *
from PyQt4.QtCore import *

import loginScreen
import sqlOperations


class userScreen(QDialog):

    def __init__(self, userName, title):
        super(userScreen, self).__init__()
        self.userName = userName
        self.initUi(400, 350, 20)
        self.setWindowTitle(title)

    def initUi(self, winWidth, winHeight, winMargins):

        self.setMinimumSize(winWidth, winHeight)
        self.resize(winWidth, winHeight)

        vLayout = QVBoxLayout()

        logoutButton = QPushButton('Logout')
        logoutButton.clicked.connect(self.logoutClick)

        welcomeLabel = QLabel('Welcome, ' + self.userName)

        userLogout = QHBoxLayout()
        userLogout.addWidget(welcomeLabel)
        userLogout.addStretch(1)
        userLogout.addWidget(logoutButton)

        self.listWidget = QListWidget()

        self.admins = QComboBox()
        self.admins.currentIndexChanged.connect(self.adminChanged)

        for admName in sqlOperations.getAdmins():
            self.admins.addItem(admName)

        if(self.listWidget.count() > 0):
            self.listWidget.setCurrentRow(0)

        fileLabel = QLabel('File')
        self.fileName = QLineEdit()
        browseButton = QPushButton('Browse')
        browseButton.clicked.connect(self.browseClick)

        fileLayout = QHBoxLayout()
        fileLayout.addWidget(fileLabel)
        fileLayout.addWidget(self.fileName)
        fileLayout.addWidget(browseButton)

        analyseButton = QPushButton('Analyse')
        analyseButton.clicked.connect(self.analyseClick)

        analyseLayout = QHBoxLayout()
        analyseLayout.addStretch(1)
        analyseLayout.addWidget(analyseButton)
        analyseLayout.addStretch(1)

        vLayout.addLayout(userLogout)
        vLayout.addWidget(self.admins)
        vLayout.addWidget(self.listWidget)
        vLayout.addLayout(fileLayout)
        vLayout.addLayout(analyseLayout)

        self.setLayout(vLayout)

        self.show()

    def analyseClick(self):
        print "analyse"

    def browseClick(self):
        openfile = QFileDialog.getOpenFileName()
        self.fileName.setText(openfile)

    def populateList(self):
        fstrings = sqlOperations.getStrings(self.fUser)

        for fstr in fstrings:
            item = QListWidgetItem(fstr)
            self.listWidget.addItem(item)

    def adminChanged(self):
        self.listWidget.clear()
        self.fUser = str(self.admins.currentText())
        self.populateList()

    def logoutClick(self):
        self.close()
        self.screen = loginScreen.loginScreen()
