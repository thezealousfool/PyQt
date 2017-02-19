import sys
from PyQt4.QtGui import *

import userScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    name = 'tester'
    screen = userScreen.userScreen(name, name + ' | Analyse')
    sys.exit(app.exec_())
