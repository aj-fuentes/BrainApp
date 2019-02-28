#! -*- coding: cp1252 -*-
import itk
from model.confidence_connected_pipe import ConfidenceConnectedPipe
from model.voting_pipe import VotingPipe
from model.cast_pipe import CastPipe
from model.segment_pipe import SegmentPipe
from model.smooth_pipe import SmoothPipe

__author__ = 'Alvaro Javier'

##Esta clase modela la información necesaria para la segmentación de una imagen
#
# Esta clase existe para no guardar la información directamente en la clas Application y así
# brindar la posibilidad de tener múltiples documentos en la misma aplicación cada una con
# su propia imagen actual en un ambiente MDI. Por ahora la aplicación está restringida a SDI
# con una sola instancia de esta clase como docmento activo.
# En esta clase se almacenan las imágenes a procesar y la información del procesamiento (filtros
# a utilizar, parámetros, etc.)
#
# @yo
#
class Document(object):

    ##Inicializador
    # @selfdoc
    def __init__(self):
        ##@var _images
        # Diccionario con las imágenes de este documento, la llave es el id de la imagen
        self._images = {}
        ##@var _current_image_id
        # Id de la imagen que se está usando en el procesamiento
        self._current_image_id = ""
        ##@var _processed_image
        # Imagen procesada
        self._processed_image           = None
        ##@var _up_cast_pipe
        # referencia a la tubería para convertir a tipo de pixel a itk.F (float)
        self._up_cast_pipe              = None
        ##@var _smooth_pipe
        # referencia a la tubería para suavizar la imagen
        self._smooth_pipe               = None
        ##@var _segment_pipe
        # referencia a la tubería para segmentar la imagen
        self._segment_pipe              = None
        ##@var _confidence_connected_pipe
        # referencia a la tubería para la segmentación estadística de la imagen
        self._confidence_connected_pipe = None
        ##@var _down_cast_pipe
        # referencia a la tubería para convertir a tipo de pixel itk.UC (unsigend char)
        self._down_cast_pipe            = None
        ##@var _voting_pipe
        # referencia a la tubería para modificar la segmetación dada una votación basad en los píxeles
        self._voting_pipe               = None
        ##Este diccionario indica cuáles tuberías de la aplicación se usarán o no en el procesamiento
        # de la imagen
        self._used_pipes = dict(
        _up_cast_pipe               = True, #indica si la tubería para convertir la imagen se está usando
        _smooth_pipe                = True, #indica si la tubería para quitar el ruido se está usando
        _segment_pipe               = True, #indica si la tubería para segmentar la imagen se está usando
        _confidence_connected_pipe  = True, #indica si la segmentación estadística de la imagen se está usando
        _down_cast_pipe             = True, #indica si la tubería para convertir la imagen se está usando
        _voting_pipe                = True #indica si la tubería para votar se está usando
        )
        ##Tubería de procesamiento, con todos los filtros seleccionados ya interconectados
        self._pipeline = []


    ## Devuelve si el filtro segmentación estadística se está usando
    # @selfdoc
    # @return True si se está usando la votación, si no False
    def usingConfidenceConnected(self):
        return self._used_pipes["_confidence_connected_pipe"]

    ##Cambia el uso del filtro segmentación estadística
    # @selfdoc
    # @param value True si se va a usar, False si no
    def useConfidenceConnected(self,value):
        update = value != self._used_pipes["_confidence_connected_pipe"]
        self._used_pipes["_confidence_connected_pipe"] = value
        if update:
            self._updatePipes()

    ## Devuelve si el filtro de votación se está usando
    # @selfdoc
    # @return True si se está usando la votación, si no False
    def usingVoter(self):
        return self._used_pipes["_voting_pipe"]

    ##Cambia el uso del filtro de votación
    # @selfdoc
    # @param value True si se va a usar, False si no
    def useVoter(self,value):
        update = value != self._used_pipes["_voting_pipe"]
        self._used_pipes["_voting_pipe"] = value
        if update:
            self._updatePipes()

    ## Devuelve si el filtro suavizador se está usando
    # @selfdoc
    # @return True si se está usando el suavizador, si no False
    def usingSmoother(self):
        return self._used_pipes["_smooth_pipe"]

    ##Cambia el uso del filtro suavizador
    # @selfdoc
    # @param value True si se va a usar, False si no
    def useSmoother(self,value):
        update = value != self._used_pipes["_smooth_pipe"]
        self._used_pipes["_smooth_pipe"] = value
        if update:
            self._updatePipes()

    ## Devuelve si el filtro segmentador se está usando
    # @selfdoc
    # @return True si se está usando el filtro segementador, si no False
    def usingSegmentor(self):
        return self._used_pipes["_segment_pipe"]

    ##Cambia el uso del filtro segmentador
    # @selfdoc
    # @param value True si se va a usar, False si no
    def useSegmentor(self,value):
        update = value != self._used_pipes["_segment_pipe"]
        self._used_pipes["_segment_pipe"] = value
        if update:
            self._updatePipes()

    ##Devuelve las imágenes en este documento (un diccionario indexado por los id de las imágenes)
    # @selfdoc
    # @return el diccionario con las imágenes en este docuemnto (e la aplicación en general, por ahora)
    @property
    def Images(self):
        return self._images

    ##Devuelve la tubería de procesamiento
    # @selfdoc
    # @return la tubería de procesamiento con los filtros que se van a usar interconectados
    @property
    def Pipes(self):
        return self._pipeline

    ##Devuelve la imagen actual
    # @selfdoc
    # @return la imagen actual que se usará en el procesamiento
    @property
    def CurrentImage(self):
        img = None
        if self._current_image_id in self._images.keys():
            img = self._images[self._current_image_id]
        return img

    ##Devuelve el id de la imagen actual
    # @selfdoc
    # @return el id de la imagen actual que se usará en el procesamiento
    @property
    def CurrentId(self):
        return self._current_image_id

    ##Cambia el id de la imagen actual (y consecuentemente la imagen actual)
    # @selfdoc
    # @param id el id de la imagen que se usará en el procesamiento
    @CurrentId.setter
    def CurrentId(self,id):
        self._current_image_id = id
        self._updatePipes() #actualizar las tuberías que se van a usar
        #conectar la entrada de la tubería
        self._pipeline[0].setInput(self.CurrentImage)

    ##Devuelve la imagen ya procesada
    # @selfdoc
    # @return la imagen que se obtiene como resultado del procesameinto de la imagen actual, None en caso de que no se
    # haya procesado la imagen
    @property
    def ProcessedImage(self):
        return self._processed_image

    ##Actualiza la conexión de filtros en la tubería
    #
    # Actualiza las conexiones de los filtros en la tuberías de procesameinto para que cuando se
    # cambia el estado de uso de un filtro (si se usa en el procesamiento o no)
    # @selfdoc
    def _updateFixedPipes(self):
        self._processed_image = None #la imagen procesada anterior ya no es válida
        img = self.CurrentImage #imagen a procesar
        #verificar que haya una imagen seleccionada
        if img is None: return

        #verificar si ya está creado o si hace falta volver a crearlo porque cambió la dimensión de la imagen
        if self._smooth_pipe is None or self._smooth_pipe.Dimension != img.Dimension:
            self._smooth_pipe = SmoothPipe(itk.F,img.Dimension,itk.F)
        #conectar la tubería que quita el ruido
        if self._used_pipes["_smooth_pipe"]:
            self._smooth_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._smooth_pipe)

        if self._segment_pipe is None or self._segment_pipe.Dimension != img.Dimension:
            self._segment_pipe = SegmentPipe(itk.F,img.Dimension,itk.F)
        #conectar la tubería que segmenta
        if self._used_pipes["_segment_pipe"]:
            #verificar si ya está creado o si hace falta volver a crearlo porque cambió la dimensión de la imagen
            self._segment_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._segment_pipe)

        #verificar si ya está creado o si hace falta volver a crearlo porque cambió la dimensión de la imagen
        if self._confidence_connected_pipe is None or\
           self._confidence_connected_pipe.Dimension != img.Dimension:
            self._confidence_connected_pipe = ConfidenceConnectedPipe(itk.F,img.Dimension,itk.F)
        #conectar la tubería de segmentación estadística
        if self._used_pipes["_confidence_connected_pipe"]:
            self._confidence_connected_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._confidence_connected_pipe)

        #verificar si ya está creado o si hace falta volver a crearlo porque cambió la dimensión de la imagen
        if self._voting_pipe is None or self._voting_pipe.Dimension != img.Dimension:
            self._voting_pipe = VotingPipe(itk.F,img.Dimension,itk.F)
        #conectar la tubería encargada de la votación
        if self._used_pipes["_voting_pipe"]:
            self._voting_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._voting_pipe)

        #conectar la tubería encargada de convertir la imagen para tipo de pixel unsigned char
        self._down_cast_pipe.connect(self._pipeline[-1])
        self._pipeline.append(self._down_cast_pipe)


    ##Actualizar la tubería de entrada y de salida del procesamiento
    # @selfdoc
    def _updateInOutPipes(self):
        img = self.CurrentImage
        if img is None: return #si no hay imagen no hacer nada
        #verificar si el filtro de entrada no se ha creado todavía
        if self._up_cast_pipe is None:
            self._up_cast_pipe = CastPipe(img.PixelType,img.Dimension,itk.F)
        #verificar que el tipo de la imagen es compatible con la entrada de la tubería
        elif img.ImageType != self._up_cast_pipe.InputImageType:
            self._up_cast_pipe = CastPipe(img.PixelType,img.Dimension,itk.F)

        #verificar si el filtro de entrada no se ha creado todavía
        if self._down_cast_pipe is None:
            self._down_cast_pipe = CastPipe(itk.F,img.Dimension,itk.UC)
        #verificar que la dimansión de la imagen es compatible con la entrada de la tubería
        elif img.Dimension != self._down_cast_pipe.Dimension:
            self._down_cast_pipe = CastPipe(itk.F,img.Dimension,itk.UC)

        self._pipeline.append(self._up_cast_pipe) #agregar a la tubería (en el principio)

    ##Limpia la tubería eliminando todos los filtros en ella
    # @selfdoc
    def clean_pipes(self):
        self._confidence_connected_pipe = None
        self._down_cast_pipe            = None
        self._up_cast_pipe              = None
        self._voting_pipe               = None
        self._segment_pipe              = None
        self._smooth_pipe               = None

    ##Actualiza las tuberías del procesamiento y las conexiones entre ellas
    # @param clean vuelve a crear la tuberías desde cero, destruye las anterires
    # @selfdoc
    def _updatePipes(self):
        self._pipeline = [] #la tubería se crea desde cero!!!!
        self._updateInOutPipes() #actualizar el filtro de entrada
        self._updateFixedPipes() #actualizar los filtros fijos de la tubería
        img = self.CurrentImage #imagen actual
        if img is not None: #si hay una imagen actual
            self._pipeline[0].setInput(img) #conectarla a la tubería de procesamiento

    ##Procesa la imagen actual con la tubería de filtros
    # @selfdoc
    def processImage(self):
        for pipe in self._pipeline:
            pipe.update()
        self._processed_image = self._pipeline[-1].getOutput()
