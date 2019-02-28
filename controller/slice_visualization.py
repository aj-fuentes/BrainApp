#! -*- coding: cp1252 -*-

from PyQt4.QtCore import pyqtSlot, QSignalMapper, SIGNAL
import vtk
from model.canonical_slice_view import CanonicalSliceView
from controller.visualization import Visualization
from view.slice_visualization_widget import SliceVisualizationWidget

__author__ = 'Alvaro Javier'

class SliceVisualization(Visualization):
    """
    Esta clase visauliza una vista de corte canónico
    """
    def __init__(self,widget=None):
        """
        Nueva visuaización de corte
        @param widget: el widget donde se muestra la visualizición, si es None se crea uno nuevo
        """
        if widget is None:
            widget = SliceVisualizationWidget()
        super(SliceVisualization,self).__init__(widget)

        self._image = None #imagen que se muesta en la visualización
        self._view = CanonicalSliceView() #esta es la vista de esta visualización
        self._ui = self._widget.ui #interfaz del widget
        ui = self._ui
        #conexión de señales de Qt
        ui.sliceSelector.valueChanged.connect(self._setSliceNumLabel)
        ui.sliceNum.editingFinished.connect(self._setSliceNumSlider)
        #cambiar el evento 'resize' del widget de esta visualización para agregarle el reseteo de la cámara
        widget.resizeEvent = self._widget_resized

        #propiedad para definir el color de las líneas
        self._lines_color_prop = vtk.vtkProperty()
        self._lines_color_prop.SetColor(1,1,0) #amarillo por defecto

        #líneas que muestran un pick point
        #línea vertical
        self._vLine = vtk.vtkLineSource()
        vLineMapper = vtk.vtkPolyDataMapper()
        vLineMapper.SetInput(self._vLine.GetOutput())
        self._vLineActor = vtk.vtkActor() #actor de la línea vertical
        self._vLineActor.SetMapper(vLineMapper)
        self._vLineActor.SetProperty(self._lines_color_prop) #esta línea se verá de color rojo
        self._vLineActor.VisibilityOff() #por defecto esta línea no se muestra
        #línea horizontal
        self._hLine = vtk.vtkLineSource()
        hLineMapper = vtk.vtkPolyDataMapper()
        hLineMapper.SetInput(self._hLine.GetOutput())
        self._hLineActor = vtk.vtkActor() #actor de la línea horizontal
        self._hLineActor.SetMapper(hLineMapper)
        self._hLineActor.SetProperty(self._lines_color_prop) #esta línea se verá de color rojo
        self._hLineActor.VisibilityOff() #por defecto esta línea no se muestra

        #posición seleccionada
        self._selected_position = (0,0,0) #valor por defecto
        self._selected_value = 0 #valor del punto seleccionado
        self._picked_position = (0,0,0)

        #texto a mostrar en el widget
        self._textActor = vtk.vtkTextActor()
        self._text_color_prop = vtk.vtkTextProperty() #propiedad que maneja el color del texto
        self._text_color_prop.SetColor(1,1,0) #azul por defecto
        self._textActor.SetTextProperty(self._text_color_prop) #el texto se verá amarillo
        self._textActor.VisibilityOff() #por defecto el texto no se ve

        axises = ["X", "Y", "Z"] #letras de los ejes
        #conexión de las señales de Qt relativas a los botones de cambio de ejes verticales
        #self._signalMapper = QSignalMapper(self._widget)
        #self._signalMapper.connect(self._signalMapper, SIGNAL("mapped(QString)"), self._setVerticalAxis)

        self._ui.XButton.clicked.connect(self._setXVerticalAxis)
        self._ui.YButton.clicked.connect(self._setYVerticalAxis)
        self._ui.ZButton.clicked.connect(self._setZVerticalAxis)

        #for button, axis in zip(self._getButtons()[:3], axises):
        #    button.clicked.connect(self._signalMapper.map)
        #    self._signalMapper.setMapping(button, axis)

        #conexión de las señales de Qt relativas a los botones de cambio de ejes horizontales
        #self._signalMapper_2 = QSignalMapper(self._widget)
        #self._signalMapper_2.connect(self._signalMapper_2, SIGNAL("mapped(QString)"), self._setHorizontalAxis)

        self._ui.XButton_2.clicked.connect(self._setXHorizontalAxis)
        self._ui.YButton_2.clicked.connect(self._setYHorizontalAxis)
        self._ui.ZButton_2.clicked.connect(self._setZHorizontalAxis)

        #for button, axis in zip(self._getButtons()[3:], axises):
        #    button.clicked.connect(self._signalMapper_2.map)
        #    self._signalMapper_2.setMapping(button, axis)

        #estados de la inversión de los ejes
        self._HInvert = False #por defecto no se invierte
        self._VInvert = False #por defecto no se invierte
        ui.invert.stateChanged.connect(self._setVInvert)
        ui.invert_2.stateChanged.connect(self._setHInvert)

        self._horizontalAxis = "X" #eje representado horizontalmente
        self._verticalAxis = "Y" #eje representado verticalmente

        #selector usado en esta visalización
        self._picker = vtk.vtkPointPicker() #de tipo vtkPointPicker para seleccionar puntos
        #para observar el evento de selección con prioridad 9
        self._picker.AddObserver("EndPickEvent",self._onPickEvent,9)

        self._iren = ui.visualization #el Interactor es el que esta en la interfaz del widget
        self._init_interactor() #incializar la visualización
        #agregar los actores de las líneas
        self._render.AddActor(self._vLineActor)
        self._render.AddActor(self._hLineActor)
        #agregar el actor del texto
        self._render.AddActor(self._textActor)
        #fijar el selector del interactor
        self._iren.SetPicker(self._picker)
        #el  estilo del interactor es de tipo imagen
        self._iren.SetInteractorStyle(vtk.vtkInteractorStyleImage())
        #observar el vento de click iz\quiero para lanzar el evento de selección
        self._iren.AddObserver("LeftButtonPressEvent",self._raisePickEvent)
        #quitar los observadores de eventos de teclado.
        #para eliminar los siguientes observadores indeseados:
        #  - pick event con p
        #  - cambiar el estilo del interactor con j o t
        #  -y otros pesaitos como w,e,f,s etc.
        # (ver cometarios de QVTKRenderWindowInteractor para más información)
        self._iren.RemoveObservers("KeyPressEvent")
        self._iren.RemoveObservers("CharEvent")

    def _getButtons(self):
        """
        Devuelve los botones de cambio de ejes
        @return: una lista con lso botones verticales primero y los horizontales después
        """
        return [self._ui.XButton, self._ui.YButton, self._ui.ZButton,
                self._ui.XButton_2, self._ui.YButton_2, self._ui.ZButton_2]

    def _getInverters(self):
        """
        Devuelve los checkboxs que se usan para invertir los ejes
        @return: unalista con el checkbox vertical y l horizontal
        """
        return [self._ui.invert, self._ui.invert_2]

    def setFixedCanonicalSlice(self):
        """
        Oculta los botonoes y checkboxes para que no se puedan acmbiar las direcciones de los cortes
        """
        for item in self._getButtons() + self._getInverters():
            item.hide()

    def setCanonicalSliceOrientation(self,hDir,vDir):
        """
        Cambia la horientacion de los cortes de manera que coincida con un corte canónico
        @param hDir: dirección horizontal
        @param vDir: dirección vertical
        las direcciones hDir y dDir deben ser una de X,Y,Z,NegX,NegY o NegZ
        """
        #cambiamos los ejes
        self._horizontalAxis = hDir.replace("Neg","")
        self._verticalAxis = vDir.replace("Neg","")
        #aquí se desabilitan los botones de manera que no se pueda poner el mismo eje en los dos cortes
        self._widget.ui.__getattribute__(self._horizontalAxis+"Button_2").setEnabled(True)
        self._widget.ui.__getattribute__(self._horizontalAxis+"Button_2").click()
        self._widget.ui.__getattribute__(self._verticalAxis+"Button").setEnabled(True)
        self._widget.ui.__getattribute__(self._verticalAxis+"Button").click()

        #nuevo estado de los inversores
        self._HInvert = (hDir.find("Neg") != -1)
        self._VInvert = (vDir.find("Neg") != -1)

        #actualización del inversor horizontal
        hInverter = self._widget.ui.invert_2
        hInverter.blockSignals(True)
        hInverter.setChecked(self._HInvert)
        hInverter.blockSignals(False)
        #actualización del inversor vertical
        vInverter = self._widget.ui.invert
        vInverter.blockSignals(True)
        vInverter.setChecked(self._VInvert)
        vInverter.blockSignals(False)
        #actualizar los ejes en la imagen
        self._updateAxis()

    def _updateAxis(self):
        """
        Actualiza la imagen que se ve
        """
        axis = "" #esta cadena representará el corte, ejemplo 'XNegY'
        if self._HInvert:
            axis += "Neg"
        axis += self._horizontalAxis
        if self._VInvert:
            axis += "Neg"
        axis += self._verticalAxis
        #llamada al método correspondiente para posicionar el slice, ejemplo setXNegYSlice()
        self._view.__getattribute__("set" + axis + "Slice").__call__()
        self._iren.update() #actualizar el interactor que sirve de visulizador
        self._ui.sliceSelector.setMinimum(0) #cambiar el valor mínimo del selector de corte
        #esto es temporal para que el cambiar el valor del corte no ocurra error
        self._ui.sliceSelector.setMaximum(999)
        #poner el valor de corte medio
        self._ui.sliceSelector.setValue(self._view.getSliceNumber())
        #cambiar el valor máximo del selector de corte
        self._ui.sliceSelector.setMaximum(self._view._size[self._view._cut_axis] - 1)

    @pyqtSlot("int")
    def _setHInvert(self, state):
        self._HInvert = state
        self._updateAxis()

    @pyqtSlot("int")
    def _setVInvert(self, state):
        self._VInvert = state
        self._updateAxis()

    @pyqtSlot()
    def _setXVerticalAxis(self):
        self._setVerticalAxis("X")

    @pyqtSlot()
    def _setYVerticalAxis(self):
        self._setVerticalAxis("Y")

    @pyqtSlot()
    def _setZVerticalAxis(self):
        self._setVerticalAxis("Z")

    @pyqtSlot()
    def _setXHorizontalAxis(self):
        self._setHorizontalAxis("X")

    @pyqtSlot()
    def _setYHorizontalAxis(self):
        self._setHorizontalAxis("Y")

    @pyqtSlot()
    def _setZHorizontalAxis(self):
        self._setHorizontalAxis("Z")

    @pyqtSlot("QString")
    def _setHorizontalAxis(self, axis):
        self._horizontalAxis = str(axis)
        self._updateAxis()
        self._reset_camera()

    @pyqtSlot("QString")
    def _setVerticalAxis(self, axis):
        self._verticalAxis = str(axis)
        self._updateAxis()
        self._reset_camera()

    def _setSliceNumView(self, num):
        """
        Cambia el corte y actualiza el render
        @param num: número del corte
        """
        self._view.setSliceNumber(num)
        self._iren.Render()

    @pyqtSlot(int)
    def _setSliceNumLabel(self, num):
        self._ui.sliceNum.setText(str(num))
        self._setSliceNumView(num)

    @pyqtSlot()
    def _setSliceNumSlider(self):
        self._ui.sliceSelector.setValue(self._ui.sliceNum.text().toInt()[0])
        self._setSliceNumView(self._ui.sliceNum.text().toInt()[0])

    @property
    def Image(self):
        """
        Devuelve la imagen que se está visualizando
        @return: la imagen que se visualzia, de tipo model.Image
        """
        return self._image

    @Image.setter
    def Image(self, img):
        """
        Cambia la imagen que se quiere visualizar
        @param img: imagen a visualizar, de tipo model.Image
        """
        self._image = img
        self._view.Image = self._image #actualizar la vista
        #cambiar la etiqueta donde mostramos el corte
        self._ui.sliceNum.setText(str(self._view.getSliceNumber()))
        #cambiar el selector de corte para que coincida con el corte adecuado
        self._ui.sliceSelector.setValue(self._view.getSliceNumber())
        #actualizar el plano
        self._updateAxis()
        #resetear la cámara para que la imagen se vea completamente
        self._reset_camera()

    def _reset_camera(self):
        """
        Actualiza la cámara para que la imagen ocupe todo el espacio de renderizado posible.
        Para esto se debe poner en modo paralelo y escalarla según la mayor lungitud de la imagen,
        obviando la longitud del eje de corte.
        """
        #si no se ha especificado una imagen no hacer nada
        if self._image is None:
            return
        hAxis = self._view.axis_map[self._horizontalAxis] #número que representa el eje horizontal
        vAxis = self._view.axis_map[self._verticalAxis] #número que representa el eje vertical
        size = self._image.Size #obtener el tamaño de la imagen
        hLen = size[hAxis] + 1 #longitud de la imagen en el eje horizontal
        vLen = size[vAxis] + 1 #longitud de la imagen en el eje vertical
        spc = self._image.Spacing #espaciado de la imagen
        hSpc = spc[hAxis] #espaciado horizontal
        vSpc = spc[vAxis] #espaciado vertical
        hLen = float(hLen)*float(hSpc) #longitud horizontal 'real' en el render
        vLen = float(vLen)*float(vSpc) #longitud vertical 'real' en el render
        hSize,vSize = self._render.GetSize() #diemsiones del render
        scale = vLen*0.5 #escala para la cámara
        #como la cámara trata de escalar la dimesión vertical para que ocupe toda el área de renderizado
        # hay que verificar que no se salga la imagen por la ortra dimensión(un poco truculento!!!)
        if hSize*vLen < vSize*hLen:
            scale = float(hLen)*float(vSize)*0.5/float(hSize)
        cam = self._render.GetActiveCamera() #obtener la cámara
        cam.ParallelProjectionOn() #ponerla en modo paralelo
        cam.SetParallelScale(scale) #escalar la cámara

    def _widget_resized(self,evt):
        """
        Se ejecuta cada ves que se cambia de tamaño el widget de esta visualización
        @param evt: objeto de tipo QResizeEvent que contine información sobre el evento de cambio det tamaño
        """
        self._widget.__class__.resizeEvent(self._widget,evt) #ejecutar la implementación por defecto
        self._reset_camera() #ahora resetear la cámara para que se ajuste al nuevo tamaño

    def setLinesColor(self,color):
        """
        Cambia el color de las líneas que se muestran al disparar un evento de slección (pickEvent)
        @param color: Nuevo color, una tripla que representa un colo RGB
        """
        self._lines_color_prop.SetColor(*color)
        
    def linesOn(self):
        """
        Muestra las líneas de selección
        """
        self._vLineActor.VisibilityOn()
        self._hLineActor.VisibilityOn()

    def linesOff(self):
        """
        Oculta las líneas de selección
        """
        self._vLineActor.VisibilityOff()
        self._hLineActor.VisibilityOff()

    def textOn(self):
        """
        Muestra el texto con la posición sleccionada y su valor
        """
        self._textActor.VisibilityOn()

    def textOff(self):
        """
        Oculta el texto con la posición sleccionada y su valor
        """
        self._textActor.VisibilityOff()

    def _raisePickEvent(self,obj,evt):
        """
        Este calback observa el evento de LeftMouseButtonPressed para lanzar un evento de selección en el punto
        donde se efectuó el evento del mouse
        @param obj: objeto que lanzó el vento
        @param evt: tipo del evento (debe ser 'LeftMouseButtonEvent')
        """
        ctrl,alt,shift = self._iren.GetControlKey(),self._iren.GetAltKey(),self._iren.GetShiftKey()
        #si control, alt o shift están oprimidos entonces esto no es un evento de selección
        # tampoco lo es si no hay una imagen mostrada
        if ctrl or alt or shift or not self._image:
            return
        x,y = obj.GetEventPosition() #obtener la posición del evento
        self._picker.Pick(x,y,0,self._render) #lanzar el evento de selección

    def _changeSelectedPosition(self,pos):
        self._selected_position = map(int,pos) #actualizar la posición seleccionada
        #actualizar el valor seleccionado
        self._selected_value = int(self._view._vtk_image.GetScalarComponentAsFloat(
            self._selected_position[0],self._selected_position[1],self._selected_position[2],0))
        self._updateText() #actualizar el texto
        self._updateLines(pos) #actualizar las líneas
        #actualizar el corte y la interfaz
        self._ui.sliceSelector.setValue(self._selected_position[self._view._cut_axis])

    def _onPickEvent(self,obj,evt):
        """
        Manejador del vento de selección en los RenderWindowsInteractors
        @param obj: el objeto que lanzó el evento
        @param evt: evento lanzado (en este caso 'EndPickEvent')
        """
        #si no se dio clicl sobre la imagen de la vista mostrar la información y retornar
        if not self._picker.GetProp3Ds().IsItemPresent(self._view.Actor):
            self._textActor.SetInput("Fuera de la Imagen")
            return
        picker = self._picker #obtener el picker de esta visualización
        self._picked_position = picker.GetPickPosition() #posición de selección en coordenadas del mapper
        pos = self.fromMapperToImage(self._picked_position) #obtener la nueva posición de selección
        #cambiar la posición del punto de sección(actualizando el texto y las líneas)
        self._changeSelectedPosition(pos)

    def _updateText(self):
        """
        Actualiza el texto de esta visualización
        """
        self._textActor.SetInput(str(self._selected_position)+":"+str(self._selected_value)) #cambiar el texto

    def fromMapperToImage(self,pickPos):
        """
        Canvierte una posición del mapper (posición de selección) en una posición dentro de la imagen 3D
        @param pickPos: posición de selcción (mapper)
        @return: la posición dentro de la imagen 3D
        """
        img_size = self.Image.Size #obtener el tamaño de la imagen mostrada
        img_spc = self.Image.Spacing #espaciado de la imagen
        #img_size = map(lambda (x,y): x*y,zip(img_size,img_spc)) #tamaño real
        vAxis = self._view.axis_map[self._verticalAxis] #obtener el eje mostrado verticalmente
        hAxis = self._view.axis_map[self._horizontalAxis] #obtener el eje mostrado horizontalmente
        cutAxis = self._view._cut_axis #obtener el eje de corte
        pos = [0,0,0] #posición en la imagen
        pos[cutAxis] = self._view.getSliceNumber() #en el eje de corte es el número del slice
        pos[vAxis] = pickPos[1] #en el eje vertical es la posición de selección vertical
        pos[hAxis] = pickPos[0] #en el eje horizontal es la posición de selección horizontal
        if self._VInvert: #si el eje vertical está invertido
            pos[vAxis] = -pos[vAxis] #invertir la coordenada
        if self._HInvert: #si el eje horizontal está invertido
            pos[hAxis] = -pos[hAxis] #invertir la coordenada
        #quitar la esclaa del mapper
        pos[hAxis] /= img_spc[hAxis]
        pos[vAxis] /= img_spc[vAxis]
        #sumarle el desplazamiento del origen que ahora es el centro de la imagen
        pos[hAxis] += img_size[hAxis]/2
        pos[vAxis] += img_size[vAxis]/2
        return pos

    def fromImageToMapper(self,imgPos):
        """
        Canvierte una posición del mapper (posición de selección) en una posición dentro de la imagen 3D
        @param imgPos: posición en la imeg 3D
        @return: la posición en el mapper para esta visualización
        """
        #para entender el código siguiente revisar los comentarios de fromMapperToImage ya que se hace lo mismo
        #pero en sentido contrario
        img_size = self.Image.Size #obtener el tamaño de la imagen mostrada
        img_spc = self.Image.Spacing #espaciado de la imagen
        vAxis = self._view.axis_map[self._verticalAxis] #eje vertical en la visualizición
        hAxis = self._view.axis_map[self._horizontalAxis] #eje horizontal en la visualizición
        pos = [0,0,0] #posición en el mapper
        pos[0] = imgPos[hAxis] #copiar la posición horizontal en la imagen
        pos[1] = imgPos[vAxis] #copiar la posición vertical en la imagen
        #mover las ccordenadas de manera que el origen sea en el centro de la imagen (esta es la forma por defecto
        # del mapper)
        pos[0] -= img_size[hAxis]/2
        pos[1] -= img_size[vAxis]/2
        #invertir las coordenadas en caso de ser necesario
        if self._VInvert:
            pos[1] = -pos[1]
        if self._HInvert:
            pos[0] = -pos[0]
        #normalizar las coordenas para el mapper ya que este no entiende de espaciado
        pos[0] *= img_spc[hAxis]
        pos[1] *= img_spc[vAxis]
        return pos

    def _updateLines(self,pos):
        """
        Actualiza las líneas según la posición dada en el espacio 3D de la imagen
        @param pos: posición 3D en la imagen
        """
        pickPos = self.fromImageToMapper(pos)
        img_size = self.Image.Size #obtener el tamaño de la imagen mostrada
        img_spc = self.Image.Spacing #espaciado de la imagen
        img_size = map(lambda (x,y): x*y,zip(img_size,img_spc)) #tamaño real
        vAxis = self._view.axis_map[self._verticalAxis]
        hAxis = self._view.axis_map[self._horizontalAxis]
        #actualizar las líneas
        self._vLine.SetPoint1(-img_size[hAxis]/2,pickPos[1],0)
        self._vLine.SetPoint2(img_size[hAxis]/2,pickPos[1],0)
        self._hLine.SetPoint1(pickPos[0],-img_size[vAxis]/2,0)
        self._hLine.SetPoint2(pickPos[0],img_size[vAxis]/2,0)

    def setPicker(self,picker):
        """
        Cambia el selector de esta visualzaición (debería ser de tipo vtkPointPicker)
        @param picker: elnuevo selecto, subtipo de vtkPicker
        """
        self._picker = picker
        self._picker.AddObserver("EndPickEvent",self._onPickEvent)
        self._iren.SetPicker(picker)

    def getPicker(self):
        """
        Devuelve el seleccionador de esta visualización
        @return: un objeto de tipo vtkPicker que representa el seleccionador de esta visualización
        """
        return self._picker