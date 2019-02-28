#! -*- coding: cp1252 -*-
import itk, vtk
from model.cast_pipe import CastPipe
from model.image import Image

__author__ = 'Alvaro Javier'

class View(object):
    """
    Esta clase representa una vista de una imagen cualquiera, el concepto de vista aquí significa
    cualquier forma de visualizar una imagen
    """
    def __init__(self):
        #imagen mostrada en esta vista, de tipo model.Image
        self._image = None
        #imagen interna de la vista que ya etsá en el formato de VTK
        self._vtk_image = None
        # tamaño de la imagen
        self._size = [1,1,1]
        #espaciado de la imagen
        self._spacing = [1.0, 1.0, 1.0]
        #origen de la imagen
        self._origin = [0, 0, 0]
        #actor que se va devolver como resultado de esta vista
        self._actor = None
        #tubería interna que se usa para instanciar el actor de VTK
        self._vtk_pipeline = None

    @property
    def Actor(self):
        """
        Actor de esta vista
        @return: un objetode tipo vtkActor
        """
        return self._actor

    def _toVTK(self):
        """
        Convierte la imagen de entrade desde ITK a formato VTK
        """
        self._itk2vtk = itk.ImageToVTKImageFilter[self._image.ImageType].New()
        self._image.Origin = (0.0,0.0,0.0) #cambiar el origen para que VTK no tenga problemas
        self._itk2vtk.SetInput(self._image.InternalImage)
        self._itk2vtk.Update()
        self._vtk_image = self._itk2vtk.GetOutput()

    @property
    def Image(self):
        """
        Devuelve la imagen ITK usada en esta vista
        @return: un objeto de tipo model.Image
        """
        return self._image

    @Image.setter
    def Image(self,img):
        """
        Cambia la imagen que se va usar en esta vista
        @param img: un objeto de tipo model.Image
        """
        self._setImage(img)

    def _setImage(self, img):
        """
        Cambia la imagen que se va usar en esta vista, este método existe para poder sobrescribir la propiedad de
        cambio de imagen.
        @param img: un objeto de tipo model.Image
        """
        self._image = img
        self._size = self._image.Size
        self._spacing = self._image.Spacing
        self._origin = self._image.Origin
        self._toVTK()
        self._vtk_pipeline.SetInput(self._vtk_image)
        self._actor.SetInput(self._vtk_pipeline.GetOutput())


