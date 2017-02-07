import sys
from PyQt4.QtGui import *

import adminScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    name = 'vivek'
    screen = adminScreen.adminScreen(name, name + ' | Add Field')
    sys.exit(app.exec_())
