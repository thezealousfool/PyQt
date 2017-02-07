import sys
from PyQt4.QtGui import *

import loginScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = loginScreen.loginScreen()
    sys.exit(app.exec_())
