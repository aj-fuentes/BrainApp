from PyQt4.QtGui import QWidget
from view.ui.slice_visualization_ui import Ui_Form


__author__ = 'Alvaro Javier'

class SliceVisualizationWidget(QWidget):
    def __init__(self, parent=None):
        super(SliceVisualizationWidget, self).__init__(parent)
        self.ui = Ui_Form()
        ui = self.ui
        ui.setupUi(self)


