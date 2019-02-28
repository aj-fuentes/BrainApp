#! -*- coding: cp1252 -*-
from PyQt4.QtGui import QFileDialog, QMessageBox
import itk
from model.image import Image

__author__ = 'Alvaro Javier'
##Esta clase se usa para salvar la imagen obtenida en el procesamiento de la imagen actual
# @yo
class ImageSaver(object):

    ##Incializador
    # @selfdoc
    def __init__(self):
        ##@var _file_dialog
        # Diálogo de Qt para salvar un fichero
        self._file_dialog = QFileDialog()
        #configuración del fileDialog de Qt
        self._file_dialog.setAcceptMode(QFileDialog.AcceptSave) #Sólo se acepta salvar fichero
        self._file_dialog.setViewMode(QFileDialog.Detail) #La vista se muestra en detalles

    ##Salvar una imagen
    #
    # Salva una imagen a un fichero, debe salvarse a un formato que ITK soporte!!
    # @selfdoc
    # @param img la imagen a salvar, si es None se muestra un cuadro de error.
    def saveImage(self,img):
        try:
            if img is None: #si la imagen no está
                QMessageBox.critical(None, "Imagen no procesada",
                    "La imagen actual no ha sido procesada o no se ha realizado una actualización de la misma luego de "
                    "procesarla. Para guardar la imagen procesada por favor haga click en 'Procesar imagen' y luego "
                    "guardéla", QMessageBox.Ok,
                    QMessageBox.NoButton) #mostrar este cuadro
                return
            res = self._file_dialog.exec_() #ejecutar el diálogo para obtener el nombre del fichero
            if res == QFileDialog.Rejected: #se canceló la salva
                return
            file_name = str(self._file_dialog.selectedFiles()[0]) #obtener el nombre del fichero
            writer = itk.ImageFileWriter[img.ImageType].New() #crear el writer de ITK
            writer.SetFileName(file_name) #ponerle el nombre seleccionado
            writer.SetInput(img.InternalImage) #conectar la imagen a guardar
            writer.Update() #guardar la imagen!
        except Exception as e:
            return
