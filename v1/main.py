import sys
from PyQt4.QtGui import *

from startScreen import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	screen = startScreen()
	sys.exit(app.exec_())