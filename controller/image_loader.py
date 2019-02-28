#! -*- coding: cp1252 -*-
from PyQt4.QtGui import QDialog, QFileDialog, QMessageBox
from controller.wait_process import WaitProcess
from model.image import Image
from view.image_loader_dialog import ImageLoaderDialog
from PyQt4.QtCore import pyqtSlot
import itk

__author__ = 'Alvaro Javier'

##Esta clase es la encargada de cargar una imagen 3D
#
# Para cargar la imagen se debe conocer el tipo de pixel y en caso de que sea una imagen RAW, las dimensiones
# de la misma. Si la imagen es de un formato conocido ITK debería ser capaz de cargarla aunque ITK no carga
# todos los formatos con todas las combinaciones de píxeles.
#
# @yo
class ImageLoader(object):
    ##Diccionario que mapea los tipos de pixel según C++ hacia los tipos de itk, las llaves
    # son los tipos de pixeles según C++ en forma de cadena
    _pixel_mapper = {
        "unsigned char (8bits)"     : itk.UC,
        "signed char (8bits)"       : itk.SC,
        "unsigned short (16bits)"   : itk.US,
        "signed short (16bits)"     : itk.SS,
        "unsigned int (32bits)"     : itk.UI,
        "signed int (32bits)"       : itk.SI,
        "float"                     : itk.F
    }

    Canceled = 1 ##Indica que la acción que cerró el diálogo fue 'Cancelar'
    OK = 0 ##Indica que la acción que cerró el diálogo fue 'OK'

    ##Inicializador
    # @selfdoc
    def __init__(self):
        ##@var _img
        # Imagen que se carga
        self._img = None
        ##@var _dialog
        # Diálogo encargado de obtener los datos para la carga de la imagen
        self._dialog = ImageLoaderDialog()
        ##@var _file_dialog
        # Diálogo encargado de obtener los datos del fichero de la imagen
        self._file_dialog = QFileDialog(self._dialog)
        #configuración del fileDialog de Qt
        self._file_dialog.setAcceptMode(QFileDialog.AcceptOpen) #Sólo se capta abrir fichero
        self._file_dialog.setFileMode(QFileDialog.ExistingFile) #Sólo se aceptan ficheros que existan
        self._file_dialog.setViewMode(QFileDialog.Detail) #La vista se muestra en detalles
        ui = self._dialog.ui
        #poner los tipos de píxeles en la interfaz
        ui.pixelType.addItems(sorted(self._pixel_mapper.keys()))
        #ui.pixelType.setCurrentIndex(4) #seleccionar unsigned char por defecto
        #conectar las señales de Qt
        ui.findFile.clicked.connect(self._file_dialog.exec_)
        self._file_dialog.fileSelected.connect(ui.fileName.setText)

    ##Realizar el proceso de carga de la imagen
    # @selfdoc
    def _process(self):
        wt = WaitProcess #para manipular el diálogo de espera
        ui = self._dialog.ui
        pt = self._pixel_mapper[str(ui.pixelType.currentText())] #tipo de pixel formato ITK
        dim = 3 #dimensión (siempre es 3D en este cargador)
        fileName = unicode(ui.fileName.text()) #nombre del fichero
        is_raw = ui.rawImage.isChecked() #para saber si la imagen es raw
        width = ui.widthValue.value() #anchoa de la imagen, si raw
        height = ui.heightValue.value() #alato de la imagen, si raw
        depth = ui.depthValue.value() #profundidad de la imagen, si raw y si 3D

        wt.change_info("Inicializando el cargador")

        ImageType = itk.Image[pt,dim] #tipo ITK de la imagen
        reader = itk.ImageFileReader[ImageType].New() #creamos el reader
        rawIO = None #imageIO para una imgen raw

        wt.change_value(10)
        if is_raw:
            wt.change_info("Inicializando el cargador RAW")
            rawIO = itk.RawImageIO[pt,dim].New() #crear el rawIO
            rawIO.SetFileDimensionality(dim) #poenrle dimensión 3D
            rawIO.SetDimensions(0,width) #ancho
            rawIO.SetDimensions(1,height) #alto
            rawIO.Setdimensions(2,depth) #profundidad
            reader.SetImageIO(rawIO.GetPointer()) #especificar al Reader que el ImageIO que debe usar es RawIO
        wt.change_info("Cargando imagen")
        wt.change_value(20)
        reader.SetFileName(fileName) #especificar el nombre del fichero a leer
        reader.Update() #cargar la imagen
        wt.change_value(90)
        wt.change_info("Preparando la salida")

        uCharImageType = itk.Image[itk.UC,dim]
        toCharPixel = itk.RescaleIntensityImageFilter[ImageType,uCharImageType].New()
        toCharPixel.SetOutputMaximum(255)
        toCharPixel.SetOutputMinimum(0)
        toCharPixel.SetInput(reader.GetOutput())
        toCharPixel.Update()

        name = fileName.split("/")[-1] #obtener el nombre
        format = ""
        if name.rfind(".") != -1:
            format = name[name.rfind("."):] #obtner el formato
            name = name[:name.rfind(".")] #quitarle al nombre lo que está después del punto
        #Crear la imagen que se va a devolver
        self._img = Image(itk.UC,dim, displayName=name,originalFile=fileName,originalFormat=format.upper())
        self._img.InternalImage = toCharPixel.GetOutput() #para la imagen a devolver esta es la imagen interna de ITK
        wt.stop()

    ##Ejecuta el diálogo para cargar una imagen
    # @selfdoc
    # @return una tupla (@<resultado@>,@<imagen@>)
    #   - donde @<resultado@> es uno de:
    #       - ImageLoader.OK
    #       - ImageLoader.Canceled
    #   - @<imagen@> es un objeto de tipo Image o None en caso de que la respuesta sea ImageLoader.Canceled
    def run(self):
        try:
            res = self._dialog.exec_() #ejecutar el diálogo para obtener los datos de la imagen a cargar
            wt = WaitProcess #mostrar el diálogo de espera
            if res == QDialog.Rejected:
                wt.stop() #terminar el diálogo de espera
                return self.Canceled,None
            else:
                wt.run() #incializar el diálogo de espera
                self._process() #realizar la carga de a imagen
                wt.stop() #terminar el diálogo de espera
                return self.OK,self._img
        except Exception as e:
            QMessageBox.critical(None, "Error al cargar el fichero",
                        "Ha ocurrido un error al intentar cargar el fichero.\n"
                        "Verfique que el nombre está escrito correctamente y que todos los caracteres del nombre son "
                        "ASCII (incluyendo el camino), BrainApp actualmente no soporta UNICODE en el nombre del fichero. "
                        "En caso de que el fichero tenga caracteres UNICODE en el nombre por favor muévalo de lugar o cámbiele "
                        "el nombre.\n"
                        "Disculpe las molestias que esto le pueda ocasionar, este error se corregirá en futuras versiones."
                        , QMessageBox.Ok,
                                 QMessageBox.NoButton)
            return self.Canceled,None
        finally:
            wt.stop() #terminar el diálogo de espera










