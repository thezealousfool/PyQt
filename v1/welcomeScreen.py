from PyQt4.QtGui import *
from PyQt4.QtCore import *

import startScreen
from outputScreen import *
from delimeter import *

class welcomeScreen(QDialog):

    def __init__(self):
        super(welcomeScreen, self).__init__()
        self.initUi()

    def initUi(self):

        vLayout = QVBoxLayout()
        vLayout.setSpacing(20)
        vLayout.setMargin(50)

        inputFileLabel = QLabel('Input File')
        outputFileLabel = QLabel('Output File')
        delimeterLabel = QLabel('Delimeter')

        self.inputFileField = QLineEdit()
        self.inputFileField.returnPressed.connect(self.analyseClick)

        self.outputFileField = QLineEdit()
        self.outputFileField.returnPressed.connect(self.analyseClick)

        self.delimeterField = QLineEdit()
        self.delimeterField.returnPressed.connect(self.analyseClick)

        inputBrowseButton = QPushButton('Browse')
        inputBrowseButton.clicked.connect(self.inputBrowseClick)
        inputBrowseButton.setDefault(True)
        inputBrowseButton.setAutoDefault(True)

        outputBrowseButton = QPushButton('Browse')
        outputBrowseButton.clicked.connect(self.outputBrowseClick)
        outputBrowseButton.setDefault(False)
        outputBrowseButton.setAutoDefault(True)

        analyseButton = QPushButton('Analyse')
        analyseButton.clicked.connect(self.analyseClick)
        analyseButton.setDefault(False)
        analyseButton.setAutoDefault(True)

        logoutButton = QPushButton('Logout')
        logoutButton.clicked.connect(self.logoutClick)
        logoutButton.setDefault(False)
        logoutButton.setAutoDefault(True)

        hLayout0 = QHBoxLayout()
        hLayout0.setContentsMargins(-1,-1,-1,20)
        hLayout0.addStretch(1)
        hLayout0.addWidget(logoutButton)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.setVerticalSpacing(10)

        grid.addWidget(inputFileLabel, 1, 0)
        grid.addWidget(self.inputFileField, 1, 1)
        grid.addWidget(inputBrowseButton, 1, 2)
        grid.addWidget(outputFileLabel, 2, 0)
        grid.addWidget(self.outputFileField, 2, 1)
        grid.addWidget(outputBrowseButton, 2, 2)
        grid.addWidget(delimeterLabel, 3, 0)
        grid.addWidget(self.delimeterField, 3, 1)

        hLayout1 = QHBoxLayout()
        hLayout1.addStretch(1)
        hLayout1.addWidget(analyseButton)
        hLayout1.addStretch(1)

        vLayout.addStretch(1)
        vLayout.addLayout(hLayout0)
        vLayout.addLayout(grid)
        vLayout.addLayout(hLayout1)
        vLayout.addStretch(1)

        self.setLayout(vLayout)
        self.setWindowTitle('Welcome')
        self.setMinimumSize(800,600)
        self.show()

    def inputBrowseClick(self):
        openfile = QFileDialog.getOpenFileName()
        self.inputFileField.setText(openfile)

    def outputBrowseClick(self):
        openfile = QFileDialog.getSaveFileName()
        self.outputFileField.setText(openfile)

    def analyseClick(self):
        ifName = self.inputFileField.text()
        ofName = self.outputFileField.text()
        delim = self.delimeterField.text()
        if (not ifName): 
            msgBox = QMessageBox()
            msgBox.setText('Supply Input File')
            msgBox.setInformativeText('Please supply path to an input file')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
        elif (not ofName): 
            msgBox = QMessageBox()
            msgBox.setText('Supply Output File')
            msgBox.setInformativeText('Please supply path to an input file')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
        elif (not delim): 
            msgBox = QMessageBox()
            msgBox.setText('Supply Delimeter')
            msgBox.setInformativeText('Please supply a delimeter')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
        elif (split(ifName, ofName, delim)):
            self.screen = outputScreen(ofName)
        else:
            msgBox = QMessageBox()
            msgBox.setText('Supply Valid Input File')
            msgBox.setInformativeText('Please supply a valid path to an input file')
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def logoutClick(self):
        self.close()
        self.screen = startScreen.startScreen()


