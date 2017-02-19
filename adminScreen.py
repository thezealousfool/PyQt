from PyQt4.QtGui import *
from PyQt4.QtCore import *

import loginScreen
import manageScreen
import sqlOperations


class adminScreen(QDialog):

    def __init__(self, userName, title):
        super(adminScreen, self).__init__()
        self.userName = userName
        self.initUi(400, 350, 20)
        self.setWindowTitle(title)

    def initUi(self, winWidth, winHeight, winMargins):

        self.setMinimumSize(winWidth, winHeight)
        self.resize(winWidth, winHeight)

        submitButton = QPushButton('Submit')
        submitButton.clicked.connect(self.submitClick)

        deleteButton = QPushButton('Delete')
        deleteButton.clicked.connect(self.deleteClick)

        clearButton = QPushButton('Clear')
        clearButton.clicked.connect(self.clearClick)

        logoutButton = QPushButton('Logout')
        logoutButton.clicked.connect(self.logoutClick)

        manageButton = QPushButton('Manage')
        manageButton.clicked.connect(self.manageClick)

        date = QPushButton('Date')
        date.clicked.connect(self.dateClick)

        time = QPushButton('Time')
        time.clicked.connect(self.timeClick)

        string = QPushButton('String')
        string.clicked.connect(self.stringClick)

        number = QPushButton('Number')
        number.clicked.connect(self.numberClick)

        delimeter = QPushButton('Delimeter')
        delimeter.clicked.connect(self.delimeterClick)

        hLayout = QHBoxLayout()

        splitter = QSplitter(Qt.Horizontal)

        sideScroll = QScrollArea()

        rVLayout = QVBoxLayout()
        rVLayout.setMargin(winMargins)

        welcomeLabel = QLabel('Welcome, ' + self.userName)

        userButtonGroup = QVBoxLayout()
        userButtonGroup.addWidget(manageButton)
        userButtonGroup.addWidget(logoutButton)

        userLogout = QHBoxLayout()
        userLogout.addWidget(welcomeLabel)
        userLogout.addStretch(1)
        userLogout.addLayout(userButtonGroup)

        formattedStringGroup = QGroupBox('Formatted String')

        fStrVLayout = QVBoxLayout()

        self.fmtString = QTextEdit()
        self.fmtString.setReadOnly(True)

        fStrBtnHLayout = QHBoxLayout()

        fStrBtnHLayout.addStretch(1)
        fStrBtnHLayout.addWidget(clearButton)
        fStrBtnHLayout.addWidget(deleteButton)

        fStrVLayout.addWidget(self.fmtString)
        fStrVLayout.addLayout(fStrBtnHLayout)

        formattedStringGroup.setLayout(fStrVLayout)

        submitButtonLayout = QHBoxLayout()

        submitButtonLayout.addStretch(1)
        submitButtonLayout.addWidget(submitButton)

        rVLayout.addLayout(userLogout)
        rVLayout.addStretch(1)
        rVLayout.addWidget(formattedStringGroup)
        rVLayout.addStretch(1)
        rVLayout.addLayout(submitButtonLayout)

        groupBox = QGroupBox('Add Field')
        groupBox.setAlignment(Qt.AlignHCenter)

        vLayout = QFormLayout()
        vLayout.addRow(date)
        vLayout.addRow(time)
        vLayout.addRow(string)
        vLayout.addRow(number)
        vLayout.addRow(delimeter)

        groupBox.setLayout(vLayout)

        rightLayout = QWidget()
        rightLayout.setLayout(rVLayout)

        sideScroll.setWidget(groupBox)
        sideScroll.setWidgetResizable(True)
        sideScroll.setMinimumWidth(winWidth * 0.2)

        splitter.addWidget(sideScroll)
        splitter.addWidget(rightLayout)
        splitter.setSizes([winWidth * 0.4, winWidth * 0.7])

        hLayout.addWidget(splitter)

        self.setLayout(hLayout)

        self.show()

    def logoutClick(self):
        self.close()
        self.screen = loginScreen.loginScreen()

    def manageClick(self):
        self.screen2 = manageScreen.manageScreen(self.userName, self.userName + ' | Manage')

    def clearClick(self):
        self.fmtString.clear()

    def deleteClick(self):
        fmt = str(self.fmtString.toPlainText())
        idx = fmt.rfind('{')
        fmt = fmt[:idx]
        self.fmtString.setText(fmt)

    def submitClick(self):
        if(sqlOperations.addEntry(self.userName, str(self.fmtString.toPlainText()))):
            msgBox = QMessageBox()
            msgBox.setText('Successful')
            msgBox.setInformativeText('Entry successfully added to database')
            msgBox.setWindowTitle('Successful')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setText('Error')
            msgBox.setInformativeText('Entry could not be added to database')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def dateClick(self):
        self.fmtString.moveCursor(QTextCursor.End)
        if(self.checkLastTokenDelem()):
            self.fmtString.insertPlainText('{d/m/y}')
        else:
            msgBox = QMessageBox()
            msgBox.setText('Input Error.')
            msgBox.setInformativeText('Please insert a delimeter between two tokens')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def timeClick(self):
        self.fmtString.moveCursor(QTextCursor.End)
        if(self.checkLastTokenDelem()):
            self.fmtString.insertPlainText('{h:m}')
        else:
            msgBox = QMessageBox()
            msgBox.setText('Input Error.')
            msgBox.setInformativeText('Please insert a delimeter between two tokens')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def numberClick(self):
        self.fmtString.moveCursor(QTextCursor.End)
        if(self.checkLastTokenDelem()):
            self.fmtString.insertPlainText('{d}')
        else:
            msgBox = QMessageBox()
            msgBox.setText('Input Error.')
            msgBox.setInformativeText('Please insert a delimeter between two tokens')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def stringClick(self):
        self.fmtString.moveCursor(QTextCursor.End)
        if(self.checkLastTokenDelem()):
            self.fmtString.insertPlainText('{s}')
        else:
            msgBox = QMessageBox()
            msgBox.setText('Input Error.')
            msgBox.setInformativeText('Please insert a delimeter between two tokens')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def delimeterClick(self):
        self.fmtString.moveCursor(QTextCursor.End)
        self.fmtString.insertPlainText(',')

    def checkLastTokenDelem(self):
        fmt = str(self.fmtString.toPlainText())
        if(fmt.endswith('}')):
            return False
        return True
