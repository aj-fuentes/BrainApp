from PyQt4.QtGui import QMainWindow
from view.ui.main_window_ui import Ui_MainWindow

__author__ = 'Alvaro Javier'

class MainWindowWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowWidget, self).__init__(parent)
        self.ui = Ui_MainWindow()
        ui = self.ui
        ui.setupUi(self)

