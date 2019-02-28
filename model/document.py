#! -*- coding: cp1252 -*-
import itk
from model.confidence_connected_pipe import ConfidenceConnectedPipe
from model.voting_pipe import VotingPipe
from model.cast_pipe import CastPipe
from model.segment_pipe import SegmentPipe
from model.smooth_pipe import SmoothPipe

__author__ = 'Alvaro Javier'

##Esta clase modela la informaci�n necesaria para la segmentaci�n de una imagen
#
# Esta clase existe para no guardar la informaci�n directamente en la clas Application y as�
# brindar la posibilidad de tener m�ltiples documentos en la misma aplicaci�n cada una con
# su propia imagen actual en un ambiente MDI. Por ahora la aplicaci�n est� restringida a SDI
# con una sola instancia de esta clase como docmento activo.
# En esta clase se almacenan las im�genes a procesar y la informaci�n del procesamiento (filtros
# a utilizar, par�metros, etc.)
#
# @yo
#
class Document(object):

    ##Inicializador
    # @selfdoc
    def __init__(self):
        ##@var _images
        # Diccionario con las im�genes de este documento, la llave es el id de la imagen
        self._images = {}
        ##@var _current_image_id
        # Id de la imagen que se est� usando en el procesamiento
        self._current_image_id = ""
        ##@var _processed_image
        # Imagen procesada
        self._processed_image           = None
        ##@var _up_cast_pipe
        # referencia a la tuber�a para convertir a tipo de pixel a itk.F (float)
        self._up_cast_pipe              = None
        ##@var _smooth_pipe
        # referencia a la tuber�a para suavizar la imagen
        self._smooth_pipe               = None
        ##@var _segment_pipe
        # referencia a la tuber�a para segmentar la imagen
        self._segment_pipe              = None
        ##@var _confidence_connected_pipe
        # referencia a la tuber�a para la segmentaci�n estad�stica de la imagen
        self._confidence_connected_pipe = None
        ##@var _down_cast_pipe
        # referencia a la tuber�a para convertir a tipo de pixel itk.UC (unsigend char)
        self._down_cast_pipe            = None
        ##@var _voting_pipe
        # referencia a la tuber�a para modificar la segmetaci�n dada una votaci�n basad en los p�xeles
        self._voting_pipe               = None
        ##Este diccionario indica cu�les tuber�as de la aplicaci�n se usar�n o no en el procesamiento
        # de la imagen
        self._used_pipes = dict(
        _up_cast_pipe               = True, #indica si la tuber�a para convertir la imagen se est� usando
        _smooth_pipe                = True, #indica si la tuber�a para quitar el ruido se est� usando
        _segment_pipe               = True, #indica si la tuber�a para segmentar la imagen se est� usando
        _confidence_connected_pipe  = True, #indica si la segmentaci�n estad�stica de la imagen se est� usando
        _down_cast_pipe             = True, #indica si la tuber�a para convertir la imagen se est� usando
        _voting_pipe                = True #indica si la tuber�a para votar se est� usando
        )
        ##Tuber�a de procesamiento, con todos los filtros seleccionados ya interconectados
        self._pipeline = []


    ## Devuelve si el filtro segmentaci�n estad�stica se est� usando
    # @selfdoc
    # @return True si se est� usando la votaci�n, si no False
    def usingConfidenceConnected(self):
        return self._used_pipes["_confidence_connected_pipe"]

    ##Cambia el uso del filtro segmentaci�n estad�stica
    # @selfdoc
    # @param value True si se va a usar, False si no
    def useConfidenceConnected(self,value):
        update = value != self._used_pipes["_confidence_connected_pipe"]
        self._used_pipes["_confidence_connected_pipe"] = value
        if update:
            self._updatePipes()

    ## Devuelve si el filtro de votaci�n se est� usando
    # @selfdoc
    # @return True si se est� usando la votaci�n, si no False
    def usingVoter(self):
        return self._used_pipes["_voting_pipe"]

    ##Cambia el uso del filtro de votaci�n
    # @selfdoc
    # @param value True si se va a usar, False si no
    def useVoter(self,value):
        update = value != self._used_pipes["_voting_pipe"]
        self._used_pipes["_voting_pipe"] = value
        if update:
            self._updatePipes()

    ## Devuelve si el filtro suavizador se est� usando
    # @selfdoc
    # @return True si se est� usando el suavizador, si no False
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

    ## Devuelve si el filtro segmentador se est� usando
    # @selfdoc
    # @return True si se est� usando el filtro segementador, si no False
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

    ##Devuelve las im�genes en este documento (un diccionario indexado por los id de las im�genes)
    # @selfdoc
    # @return el diccionario con las im�genes en este docuemnto (e la aplicaci�n en general, por ahora)
    @property
    def Images(self):
        return self._images

    ##Devuelve la tuber�a de procesamiento
    # @selfdoc
    # @return la tuber�a de procesamiento con los filtros que se van a usar interconectados
    @property
    def Pipes(self):
        return self._pipeline

    ##Devuelve la imagen actual
    # @selfdoc
    # @return la imagen actual que se usar� en el procesamiento
    @property
    def CurrentImage(self):
        img = None
        if self._current_image_id in self._images.keys():
            img = self._images[self._current_image_id]
        return img

    ##Devuelve el id de la imagen actual
    # @selfdoc
    # @return el id de la imagen actual que se usar� en el procesamiento
    @property
    def CurrentId(self):
        return self._current_image_id

    ##Cambia el id de la imagen actual (y consecuentemente la imagen actual)
    # @selfdoc
    # @param id el id de la imagen que se usar� en el procesamiento
    @CurrentId.setter
    def CurrentId(self,id):
        self._current_image_id = id
        self._updatePipes() #actualizar las tuber�as que se van a usar
        #conectar la entrada de la tuber�a
        self._pipeline[0].setInput(self.CurrentImage)

    ##Devuelve la imagen ya procesada
    # @selfdoc
    # @return la imagen que se obtiene como resultado del procesameinto de la imagen actual, None en caso de que no se
    # haya procesado la imagen
    @property
    def ProcessedImage(self):
        return self._processed_image

    ##Actualiza la conexi�n de filtros en la tuber�a
    #
    # Actualiza las conexiones de los filtros en la tuber�as de procesameinto para que cuando se
    # cambia el estado de uso de un filtro (si se usa en el procesamiento o no)
    # @selfdoc
    def _updateFixedPipes(self):
        self._processed_image = None #la imagen procesada anterior ya no es v�lida
        img = self.CurrentImage #imagen a procesar
        #verificar que haya una imagen seleccionada
        if img is None: return

        #verificar si ya est� creado o si hace falta volver a crearlo porque cambi� la dimensi�n de la imagen
        if self._smooth_pipe is None or self._smooth_pipe.Dimension != img.Dimension:
            self._smooth_pipe = SmoothPipe(itk.F,img.Dimension,itk.F)
        #conectar la tuber�a que quita el ruido
        if self._used_pipes["_smooth_pipe"]:
            self._smooth_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._smooth_pipe)

        if self._segment_pipe is None or self._segment_pipe.Dimension != img.Dimension:
            self._segment_pipe = SegmentPipe(itk.F,img.Dimension,itk.F)
        #conectar la tuber�a que segmenta
        if self._used_pipes["_segment_pipe"]:
            #verificar si ya est� creado o si hace falta volver a crearlo porque cambi� la dimensi�n de la imagen
            self._segment_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._segment_pipe)

        #verificar si ya est� creado o si hace falta volver a crearlo porque cambi� la dimensi�n de la imagen
        if self._confidence_connected_pipe is None or\
           self._confidence_connected_pipe.Dimension != img.Dimension:
            self._confidence_connected_pipe = ConfidenceConnectedPipe(itk.F,img.Dimension,itk.F)
        #conectar la tuber�a de segmentaci�n estad�stica
        if self._used_pipes["_confidence_connected_pipe"]:
            self._confidence_connected_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._confidence_connected_pipe)

        #verificar si ya est� creado o si hace falta volver a crearlo porque cambi� la dimensi�n de la imagen
        if self._voting_pipe is None or self._voting_pipe.Dimension != img.Dimension:
            self._voting_pipe = VotingPipe(itk.F,img.Dimension,itk.F)
        #conectar la tuber�a encargada de la votaci�n
        if self._used_pipes["_voting_pipe"]:
            self._voting_pipe.connect(self._pipeline[-1])
            self._pipeline.append(self._voting_pipe)

        #conectar la tuber�a encargada de convertir la imagen para tipo de pixel unsigned char
        self._down_cast_pipe.connect(self._pipeline[-1])
        self._pipeline.append(self._down_cast_pipe)


    ##Actualizar la tuber�a de entrada y de salida del procesamiento
    # @selfdoc
    def _updateInOutPipes(self):
        img = self.CurrentImage
        if img is None: return #si no hay imagen no hacer nada
        #verificar si el filtro de entrada no se ha creado todav�a
        if self._up_cast_pipe is None:
            self._up_cast_pipe = CastPipe(img.PixelType,img.Dimension,itk.F)
        #verificar que el tipo de la imagen es compatible con la entrada de la tuber�a
        elif img.ImageType != self._up_cast_pipe.InputImageType:
            self._up_cast_pipe = CastPipe(img.PixelType,img.Dimension,itk.F)

        #verificar si el filtro de entrada no se ha creado todav�a
        if self._down_cast_pipe is None:
            self._down_cast_pipe = CastPipe(itk.F,img.Dimension,itk.UC)
        #verificar que la dimansi�n de la imagen es compatible con la entrada de la tuber�a
        elif img.Dimension != self._down_cast_pipe.Dimension:
            self._down_cast_pipe = CastPipe(itk.F,img.Dimension,itk.UC)

        self._pipeline.append(self._up_cast_pipe) #agregar a la tuber�a (en el principio)

    ##Limpia la tuber�a eliminando todos los filtros en ella
    # @selfdoc
    def clean_pipes(self):
        self._confidence_connected_pipe = None
        self._down_cast_pipe            = None
        self._up_cast_pipe              = None
        self._voting_pipe               = None
        self._segment_pipe              = None
        self._smooth_pipe               = None

    ##Actualiza las tuber�as del procesamiento y las conexiones entre ellas
    # @param clean vuelve a crear la tuber�as desde cero, destruye las anterires
    # @selfdoc
    def _updatePipes(self):
        self._pipeline = [] #la tuber�a se crea desde cero!!!!
        self._updateInOutPipes() #actualizar el filtro de entrada
        self._updateFixedPipes() #actualizar los filtros fijos de la tuber�a
        img = self.CurrentImage #imagen actual
        if img is not None: #si hay una imagen actual
            self._pipeline[0].setInput(img) #conectarla a la tuber�a de procesamiento

    ##Procesa la imagen actual con la tuber�a de filtros
    # @selfdoc
    def processImage(self):
        for pipe in self._pipeline:
            pipe.update()
        self._processed_image = self._pipeline[-1].getOutput()
