#! -*- coding: cp1252 -*-
import vtk

__author__ = 'Alvaro Javier'


class Visualization(object):
    """
    Esta clase represanta una visualización de una vista en la pantalla.
    Tiene un widget que es el que contiene el renderWindow de VTK
    """

    def __init__(self,widget):
        # Widget donde se muestra la visualización
        self._widget = widget
        # Rederer
        self._render = None
        # QVTKRenderWindowInteractor
        self._iren = None
        # Vista de esta visualización
        self._view = None

    @property
    def Widget(self):
        return self._widget

    def _init_interactor(self):
        """
        Inicializa los elementos encargados de la visualización en esta vista
        @return: None
        """
        self._render = vtk.vtkRenderer()
        self._render.AddActor(self._view.Actor)

        self._renderWindow = self._iren.GetRenderWindow()
        self._renderWindow.AddRenderer(self._render)

        self._iren.Initialize()
        self._render.Render()
        self._iren.Start()

