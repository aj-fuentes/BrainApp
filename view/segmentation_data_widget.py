from PyQt4.QtGui import QDockWidget
from view.ui.segmentation_data_ui import Ui_DockWidget

__author__ = 'Alvaro Javier'

class SegmentationDataWidget(QDockWidget):
    def __init__(self, parent=None):
        super(SegmentationDataWidget, self).__init__(parent)
        self.ui = Ui_DockWidget()
        ui = self.ui
        ui.setupUi(self)

