#! -*- coding: cp1252 -*-
from controller.slice_visualization import SliceVisualization
from controller.visualization import Visualization
from view.three_planes_widget import ThreePlanesWidget

__author__ = 'Alvaro Javier'

class ThreePlanesVisualization(Visualization):
    """
    Esta clase representa una visualización de una imagen 3D según 3 panos que la cortan.
    Originalmente estos planos deben represtar los cortes coronal, axial y sagital del cuerpo.
    Permite cambiar los planos a voluntad en caso de que no sea puesta en modo fijo.
    """
    def __init__(self,widget=None):
        if widget is None:
            self._widget = ThreePlanesWidget()
        super(ThreePlanesVisualization,self).__init__(widget)

        #interfaz del widget
        self._ui = self._widget.ui
        ui =  self._ui

        #instancias de las visualizaciones de los tres planos
        self._coronalVisualization = SliceVisualization(ui.coronalPlane)
        self._axialVisualization = SliceVisualization(ui.axialPlane)
        self._sagittalVisualization = SliceVisualization(ui.sagittalPlane)

        #orientacione de los planos
        self._coronalVisualization.setCanonicalSliceOrientation("X","NegY")
        self._axialVisualization.setCanonicalSliceOrientation("X","NegZ")
        self._sagittalVisualization.setCanonicalSliceOrientation("Z","NegY")

        #mostrar el texto
        self._coronalVisualization.textOn()
        self._axialVisualization.textOn()
        self._sagittalVisualization.textOn()
        #mostrar las líneas
        self._coronalVisualization.linesOn()
        self._axialVisualization.linesOn()
        self._sagittalVisualization.linesOn()
        #observar los eventos de selección para sincronizar las res visualizaciones
        self._coronalVisualization._picker.AddObserver("EndPickEvent",self._synchronizePicking,8)
        self._axialVisualization._picker.AddObserver("EndPickEvent",self._synchronizePicking,8)
        self._sagittalVisualization._picker.AddObserver("EndPickEvent",self._synchronizePicking,8)

        #imagen de la visualización
        self._image = None

    def _synchronizePicking(self,obj,evt):
        """
        Este observador se usa para sincronizar las tres visaulzaiciones para que muestren el mismo punto de
        selección
        @param obj:
        @param evt:
        """
        if obj is self._coronalVisualization._picker:
            self._axialVisualization._changeSelectedPosition(self._coronalVisualization._selected_position)
            self._axialVisualization._iren.Render()
            self._sagittalVisualization._changeSelectedPosition(self._coronalVisualization._selected_position)
            self._sagittalVisualization._iren.Render()
        elif obj is self._axialVisualization._picker:
            self._coronalVisualization._changeSelectedPosition(self._axialVisualization._selected_position)
            self._coronalVisualization._iren.Render()
            self._sagittalVisualization._changeSelectedPosition(self._axialVisualization._selected_position)
            self._sagittalVisualization._iren.Render()
        elif obj is self._sagittalVisualization._picker:
            self._coronalVisualization._changeSelectedPosition(self._sagittalVisualization._selected_position)
            self._coronalVisualization._iren.Render()
            self._axialVisualization._changeSelectedPosition(self._sagittalVisualization._selected_position)
            self._axialVisualization._iren.Render()


    def setFixedPlanes(self):
        """
        Hace que esta visualización sea fija, o sea que no se pueden cambiar los cortes
        """
        self._coronalVisualization.setFixedCanonicalSlice()
        self._axialVisualization.setFixedCanonicalSlice()
        self._sagittalVisualization.setFixedCanonicalSlice()

    @property
    def Image(self):
        """
        Devuelve la imagen de esta vizualización
        @return: la imagen, de tipo model.Image
        """
        return self._image

    @Image.setter
    def Image(self, img):
        """
        Cambia la imagen de esta vizaulización
        @param img: imagen a visualizar, de tipo model.Image
        """
        self._image = img #actualizar la imagen de esta visualización
        #cambiar la imagen en los planos
        self._coronalVisualization.Image = self._image
        self._axialVisualization.Image = self._image
        self._sagittalVisualization.Image = self._image
        #actualizar la visualización de los planos
        self._coronalVisualization._updateAxis()
        self._axialVisualization._updateAxis()
        self._sagittalVisualization._updateAxis()