from PyQt4.QtGui import QDialog
from view.ui.series_loader_ui import Ui_Dialog

__author__ = 'Alvaro Javier'

class SeriesLoaderDialog(QDialog):
    def __init__(self, parent=None):
        super(SeriesLoaderDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        ui = self.ui
        ui.setupUi(self)