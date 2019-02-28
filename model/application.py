#! -*- coding: cp1252 -*-
import vtk
from model.document import Document
__author__ = 'Alvaro Javier'

##Clase que contiene el modelo de la aplicación
#
# Esta clase es el punto de entrada al modelo de la aplicación. Todos sus métodos son
# métodos de clase ya que esta clase simula al patrón singleton.
# A través de esta clase se puede obtener el documento actual, la imagen actual, etc.
# También contiene la QApplication y es la que inicia el ciclo principal de eventos de Qt.
#
# @yo
#
class Application(object):
    ##Documento actual (por ahora es único, pero podrían haber más en un futuro)
    _current_document = None

    ##Inicializador de la aplicación
    #
    # Este método se encarga de inicializar lo necesario para lanzar la aplicación:
    # - Incializa la aplicación de Qt (_qapp) con el estilo deseado
    # - Fija que vtk escriba todos sus mensajes en un fichero y no los muestre en una ventana
    # - Inicializa la clase WaitProcess
    #
    # @clsdoc
    @classmethod
    def init(cls):
        cls._current_document = Document()
        log = vtk.vtkFileOutputWindow() #para guardar los mensajes de vtk
        log.SetFileName("logs/vtk.log") #fichero donde se guardan
        log.SetInstance(log) #usar este fichero

    ##Devuelve el documento actual
    # @clsdoc
    # @return el documento usado actualmente por la aplciación (por ahora es único)
    @classmethod
    def get_current_document(cls):
        return cls._current_document

    ##Devuelve las imágenes cargadas en la aplicación
    # @clsdoc
    # @return un diccionario con todas las imágenes indexadas por su id
    @classmethod
    def get_images(cls):
        return cls.get_current_document().Images

    ##Devuelve la imagen actual
    # @clsdoc
    # @return la imagen actual usada en la aplicación
    @classmethod
    def get_current_image(cls):
        return cls.get_current_document().CurrentImage

    ##Agrega una imagen a la aplicación
    # @clsdoc
    # @param img nueva image a añadir
    @classmethod
    def add_image(cls,img):
        cls.get_current_document().Images[img.Id] = img

    ##Devuelve los filtros (tuberías) de la apicación
    # @clsdoc
    # @return unalista de tuberías
    @classmethod
    def get_pipes(cls):
        return cls.get_current_document().Pipes()

    ##Cambia la imagen actual de la aplicación
    # @clsdoc
    # @param id id de la nueva imagen actual(tiene que estar ya cargada)
    @classmethod
    def set_current_image_id(cls,id):
        cls.get_current_document().CurrentId = id

    ##Devuelve el id de la imagen actual
    # @clsdoc
    # @return id de la imagen actual
    @classmethod
    def get_current_image_id(cls):
        return cls.get_current_document().CurrentId

    ##Devuelve la imagen luego de ser procesada
    # @clsdoc
    # @return la imagen ya procesada
    @classmethod
    def get_processed_image(cls):
        return cls.get_current_document().ProcessedImage

    ##Ejecuta el procesamiento de la imagen acual
    # @clsdoc
    @classmethod
    def processImage(cls):
        cls.get_current_document().processImage()



