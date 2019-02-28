from PyQt4.QtGui import QApplication
from view.wait_dialog import WaitDialog

__author__ = 'Alvaro Javier'

class WaitProcess(object):
    _dialog = None

    @classmethod
    def init(cls):
        cls._dialog = WaitDialog()

    @classmethod
    def change_info(cls,info):
        cls._dialog.ui.info.setText(cls._dialog.tr(info+"..."))
        QApplication.processEvents()

    @classmethod
    def change_value(cls,value):
        cls._dialog.ui.progreso.setValue(value)
        QApplication.processEvents()

    @classmethod
    def run(cls):
        cls._dialog.setModal(True)
        cls._dialog.show()

    @classmethod
    def stop(cls):
        cls.change_info("Terminando")
        cls.change_value(100)
        cls._dialog.hide()


