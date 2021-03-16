from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.setWindowTitle("Knightbearr Browser")
        self.browser = QWebView()
        self.browser.setUrl( QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
app.setApplicationName("Knightbearr Browser")
app.setOrganizationName("Knightbearr")
app.setOrganizationDomain("knightbearr.org")

window = MainWindow()
window.show()

app.exec_()