from PyQt4.QtGui import QWidget
from view.ui.three_planes_ui import Ui_Form

__author__ = 'Alvaro Javier'

class ThreePlanesWidget(QWidget):
    def __init__(self, parent=None):
        super(ThreePlanesWidget, self).__init__(parent)
        self.ui = Ui_Form()
        ui = self.ui
        ui.setupUi(self)