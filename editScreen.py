from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlOperations


class editScreen(QDialog):

    def __init__(self, userName, title, oldStr, parent):
        super(editScreen, self).__init__()
        self.parent = parent
        self.oldStr = oldStr
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

        oldStringGroup = QGroupBox('Old String')
        newStringGroup = QGroupBox('New String')

        fStrVLayout = QVBoxLayout()
        oStrVLayout = QVBoxLayout()

        self.oString = QTextEdit(self.oldStr)
        self.oString.setReadOnly(True)

        oStrVLayout.addWidget(self.oString)

        oldStringGroup.setLayout(oStrVLayout)

        self.fmtString = QTextEdit()
        self.fmtString.setReadOnly(True)

        fStrBtnHLayout = QHBoxLayout()

        fStrBtnHLayout.addStretch(1)
        fStrBtnHLayout.addWidget(clearButton)
        fStrBtnHLayout.addWidget(deleteButton)

        fStrVLayout.addWidget(self.fmtString)
        fStrVLayout.addLayout(fStrBtnHLayout)

        newStringGroup.setLayout(fStrVLayout)

        submitButtonLayout = QHBoxLayout()

        submitButtonLayout.addStretch(1)
        submitButtonLayout.addWidget(submitButton)

        rVLayout.addWidget(oldStringGroup)
        rVLayout.addWidget(newStringGroup)
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

    def clearClick(self):
        self.fmtString.clear()

    def deleteClick(self):
        fmt = str(self.fmtString.toPlainText())
        idx = fmt.rfind('{')
        fmt = fmt[:idx]
        self.fmtString.setText(fmt)

    def submitClick(self):
        if(sqlOperations.editEntry(self.userName,
           str(self.oString.toPlainText()),
           str(self.fmtString.toPlainText()))):
            self.parent.listWidget.clear()
            self.parent.populateList()
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
