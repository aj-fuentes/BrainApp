from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from view.ui.wait_ui import Ui_Dialog

__author__ = 'Alvaro Javier'

class WaitDialog(QDialog):
    def __init__(self, parent=None):
        super(WaitDialog, self).__init__(parent,Qt.CustomizeWindowHint)
        self.ui = Ui_Dialog()
        ui = self.ui
        ui.setupUi(self)

