from PyQt4.QtGui import *
from PyQt4.QtCore import *

from welcomeScreen import *

class outputScreen(QDialog):

    def __init__(self, ofName):
        super(outputScreen, self).__init__()
        self.initUi(ofName)

    def initUi(self, ofName):
        output = QPlainTextEdit()
        ofile = open(ofName)
        output.insertPlainText(ofile.read())
        output.setReadOnly(True)

        vLayout = QVBoxLayout()
        vLayout.setSpacing(10)
        vLayout.setMargin(20)

        closeButton = QPushButton('Close')
        closeButton.clicked.connect(self.closeClick)
        closeButton.setDefault(True)
        closeButton.setAutoDefault(True)

        hLayout = QHBoxLayout()
        hLayout.addStretch(1)
        hLayout.addWidget(closeButton)
        hLayout.addStretch(1)

        vLayout.addWidget(output)
        vLayout.addLayout(hLayout)

        self.setLayout(vLayout)
        self.setWindowTitle('Output')
        self.setMinimumSize(800,600)
        self.show()

    def closeClick(self):
        self.close()
