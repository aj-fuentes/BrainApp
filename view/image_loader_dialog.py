from PyQt4.QtGui import QDialog, QIntValidator
from view.ui.image_loader_ui import Ui_Dialog

__author__ = 'Alvaro Javier'

class ImageLoaderDialog(QDialog):
    def __init__(self, parent=None):
        super(ImageLoaderDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        ui = self.ui
        ui.setupUi(self)



