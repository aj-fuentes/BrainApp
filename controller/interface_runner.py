#! -*- coding: cp1252 -*-
from PyQt4.QtCore import QLocale, QTranslator
from PyQt4.QtGui import QApplication, QIcon, QPixmap
from controller.wait_process import WaitProcess

__author__ = 'Alvaro Javier'

class InterfaceRunner(object):
    ##Aplicaci�n de Qt
    _qapp = None

    @classmethod
    def init(cls):
        if cls._qapp is None:
            qapp = QApplication(["","-style","Cleanlooks"]) #crear la aplicaci�n con el estilo que va a usar
            cls._qapp = qapp #fijar la aplicaci�n de Qt global
            cls._qtTranslator = QTranslator() #crear un traductor de QT
            if cls._qtTranslator.load("qt_es"): # para los di�logos est�ndares
                qapp.installTranslator(cls._qtTranslator) #instalar el traductor
            qapp.setApplicationName("BrainApp")
            qapp.setApplicationVersion("0.1")
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icons/seleccion/main_icon.png"), QIcon.Normal,
                           QIcon.Off)
            qapp.setWindowIcon(icon)
            WaitProcess.init()

    ##Inicia la aplicaci�n
    # @clsdoc
    # @param main_window controlador de la ventana principal de la aplicaci�n (de tipo MainWindow)
    # @see [MainWindow](@ref BrainApp.controller.main_window.MainWindow)
    @classmethod
    def start_even_loop(cls,main_window):
        if cls._qapp is not None:
            main_window.run()
            cls._qapp.exec_()
