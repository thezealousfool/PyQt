from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlOperations


class manageScreen(QDialog):

    def __init__(self, userName, title):
        super(manageScreen, self).__init__()
        self.userName = userName
        self.initUi(400, 350, 20)
        self.setWindowTitle(title)

    def initUi(self, winWidth, winHeight, winMargins):

        self.setMinimumSize(winWidth, winHeight)
        self.resize(winWidth, winHeight)

        vLayout = QVBoxLayout()

        buttonLayout = QHBoxLayout()

        self.listWidget = QListWidget()

        self.populateList()
        if(self.listWidget.count() > 0):
            self.listWidget.setCurrentRow(0)

        removeButton = QPushButton('Remove')
        removeButton.clicked.connect(self.removeClick)

        closeButton = QPushButton('Close')
        closeButton.clicked.connect(self.closeClick)

        buttonLayout.addStretch(1)
        buttonLayout.addWidget(removeButton)
        buttonLayout.addWidget(closeButton)
        buttonLayout.addStretch(1)

        vLayout.addWidget(self.listWidget)
        vLayout.addLayout(buttonLayout)

        self.setLayout(vLayout)

        self.show()

    def populateList(self):
        fstrings = sqlOperations.getStrings(self.userName)

        for fstr in fstrings:
            item = QListWidgetItem(fstr)
            self.listWidget.addItem(item)

    def removeClick(self):
        item = self.listWidget.currentItem()

        if(not item):
            text = ''
        else:
            text = item.text()

        if(sqlOperations.delEntry(self.userName, str(text))):
            self.listWidget.takeItem(self.listWidget.row(item))
        else:
            msgBox = QMessageBox()
            msgBox.setText('Unsuccessful')
            msgBox.setInformativeText('Entry deletion unsuccessful')
            msgBox.setWindowTitle('Fail')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def closeClick(self):
        self.close()
