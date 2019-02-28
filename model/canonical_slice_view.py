#! -*- coding: cp1252 -*-

from model.view import View
import vtk

__author__ = 'Alvaro Javier'

class CanonicalSliceView(View):
    """
    Esta clase representa una vista 2D de un corte canónico de una imagen 3D.
    Los cortes canónicos son los paralelos a los planos canónicos: XY,YZ,ZX.
    Estos cortes además de ser paralelos a uno de estos planos también pueden ser reorientados
    en cualqiera de sus dos direcciones, por ejemplo un corte paralelo a XY pude representar
    cualquieea de los siguienes planos con ses respecivas direcciones:
        * XY
        * X(-Y)
        * (-X)Y
        * (-X)(-Y)
        * YX
        * (-Y)X
        * Y(-X)
        * (-Y)(-X)
    Lo que para los todos los planos canónicos da un total de 24 cortes.
    En los cortes la primera coordenada será la coordenada que se visualiza de forma horizontal y la segunda
    de forma vertical.
    """
    #Representación numérica de los ejes
    XAxis = 0
    YAxis = 1
    ZAxis = 2

    #mappeo entre los ejes y su representación numérica
    axis_map = {
        "X": 0,
        "Y": 1,
        "Z": 2
    }

    #mappeo de las posibles direcciones horizontales/verticales en forma de
    #cosenos directores
    _orientations = dict(
        #direcciones canónicas de los ejes
        X=[1, 0, 0], #X
        Y=[0, 1, 0], #Y
        Z=[0, 0, 1], #Z
        #direcciones canónicas inversas
        X_=[-1, 0, 0], #-X
        Y_=[0, -1, 0], #-Y
        Z_=[0, 0, -1]  #-Z
    )

    def __init__(self):
        super(CanonicalSliceView, self).__init__()
        self._slicer = vtk.vtkImageReslice()#obtiene los cortes de la imagen
        self._vtk_pipeline = self._slicer #este es la tubería VTK de esta vista
        self._actor = vtk.vtkImageActor() #el actor de esta vista
        self._slicer.SetOutputDimensionality(2) #para que devuelva un corte 2D
        self._slicer.SetInterpolationModeToCubic() #método de interpolación
        #self._actor.SetInput(self._slicer.GetOutput())

        self._cut_axis = self.ZAxis #eje a través del cual se realiza el corte de manera perpendicular
        #cosenos directores del corte que se usa para obtener la imagen
        #en este caso se hace un corte paralelo al plano XY con esas mismas direcciones
        self._x_cosines = self._orientations["X"]
        self._y_cosines = self._orientations["Y"]
        self._z_cosines = self._orientations["Z"]

    def _setImage(self, img):
        """
        cambia la imagen de esta vista
        @param img: imagen a visualizar, de tipo model.Image
        """
        super(CanonicalSliceView, self)._setImage(img)
        #por defecto el número del slice es la longitud a lo largo del eje de corte sobre 2
        self._slice_number = self._size[self._cut_axis] / 2
        self.setSliceNumber(self._slice_number)
        self.setXYSlice()

    def getSliceNumber(self):
        """
        Devuelve el número del corte
        @return: un entero
        """
        return self._slice_number

    def setSliceNumber(self, slice_number):
        """
        Cambia el corte actual de la imagen
        @param slice_number: un entero que será el nuevo corte
        """
        self._slice_number = slice_number
        # el punto de corte por defecto es el centro de la imagen, de manera que se obtenga el corte
        #central en cualquiera de las direcciones
        cut_point = map(lambda (x, y): x * y / 2, zip(self._spacing, self._size))
        ax = self._cut_axis #eje de corte
        #el punto de corte se actualiza para que sea en el punto indicado según la dirección de corte
        cut_point[ax] = self._spacing[ax] * slice_number
        self._setCutPoint(cut_point)

    def _setCutPoint(self, xyz):
        """
        Cambia el punto de corte
        @param xyz: coordenadas del punto de corte (x,y,z)
        """
        self._slicer.SetResliceAxesOrigin(xyz[0], xyz[1], xyz[2])

    def _setOrientation(self, Xdir, Ydir):
        """
        Cambia la orinetación del corte, esta e una función interna no debe ser llamada por el usuario
        @param Xdir: Dirección del eje X del corte
        @param Ydir: Dirección del eje Y del corte
        el eje Z representa el eje de corte, que puede ser cualquiera
        """
        self._x_cosines = self._orientations[Xdir] #cosenos directores del eje X
        self._y_cosines = self._orientations[Ydir] #cosenos directores del eje Y
        #aquí se detecta el eje queda como eje de corte
        cut_axis = "XYZ".replace(Xdir[0], "").replace(Ydir[0], "")
        self._z_cosines = self._orientations[cut_axis] #cosenos directores del eje Z
        #aquí se realiza el coret en el filtro de VTK
        self._slicer.SetResliceAxesDirectionCosines(self._x_cosines, self._y_cosines, self._z_cosines)
        self._cut_axis = self.axis_map[cut_axis] #se actualiza el eje de corte
        #por defecto luego de cambiar la orientación el corte debe ser el punto medio
        self.setSliceNumber(self._size[self._cut_axis] / 2)

    def setXYSlice(self):
        self._setOrientation("X", "Y")

    def setXNegYSlice(self):
        self._setOrientation("X", "Y_")

    def setNegXYSlice(self):
        self._setOrientation("X_", "Y")

    def setNegXNegYSlice(self):
        self._setOrientation("X_", "Y_")

    def setXZSlice(self):
        self._setOrientation("X", "Z")

    def setXNegZSlice(self):
        self._setOrientation("X", "Z_")

    def setNegXZSlice(self):
        self._setOrientation("X_", "Z")

    def setNegXNegZSlice(self):
        self._setOrientation("X_", "Z_")

    def setYXSlice(self):
        self._setOrientation("Y", "X")

    def setYNegXSlice(self):
        self._setOrientation("Y", "X_")

    def setNegYXSlice(self):
        self._setOrientation("Y_", "X")

    def setNegYNegXSlice(self):
        self._setOrientation("Y_", "X_")

    def setYZSlice(self):
        self._setOrientation("Y", "Z")

    def setYNegZSlice(self):
        self._setOrientation("Y", "Z_")

    def setNegYZSlice(self):
        self._setOrientation("Y_", "Z")

    def setNegYNegZSlice(self):
        self._setOrientation("Y_", "Z_")

    def setZXSlice(self):
        self._setOrientation("Z", "X")

    def setZNegXSlice(self):
        self._setOrientation("Z", "X_")

    def setNegZXSlice(self):
        self._setOrientation("Z_", "X")

    def setNegZNegXSlice(self):
        self._setOrientation("Z_", "X_")

    def setZYSlice(self):
        self._setOrientation("Z", "Y")

    def setZNegYSlice(self):
        self._setOrientation("Z", "Y_")

    def setNegZYSlice(self):
        self._setOrientation("Z_", "Y")

    def setNegZNegYSlice(self):
        self._setOrientation("Z_", "Y_")
