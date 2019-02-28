#! -*- coding: cp1252 -*-
from PyQt4.QtCore import QLocale, QTranslator
from PyQt4.QtGui import QApplication, QIcon, QPixmap
from controller.wait_process import WaitProcess

__author__ = 'Alvaro Javier'

class InterfaceRunner(object):
    ##Aplicación de Qt
    _qapp = None

    @classmethod
    def init(cls):
        if cls._qapp is None:
            qapp = QApplication(["","-style","Cleanlooks"]) #crear la aplicación con el estilo que va a usar
            cls._qapp = qapp #fijar la aplicación de Qt global
            cls._qtTranslator = QTranslator() #crear un traductor de QT
            if cls._qtTranslator.load("qt_es"): # para los diálogos estándares
                qapp.installTranslator(cls._qtTranslator) #instalar el traductor
            qapp.setApplicationName("BrainApp")
            qapp.setApplicationVersion("0.1")
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icons/seleccion/main_icon.png"), QIcon.Normal,
                           QIcon.Off)
            qapp.setWindowIcon(icon)
            WaitProcess.init()

    ##Inicia la aplicación
    # @clsdoc
    # @param main_window controlador de la ventana principal de la aplicación (de tipo MainWindow)
    # @see [MainWindow](@ref BrainApp.controller.main_window.MainWindow)
    @classmethod
    def start_even_loop(cls,main_window):
        if cls._qapp is not None:
            main_window.run()
            cls._qapp.exec_()
