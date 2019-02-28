#! -*- coding: cp1252 -*-

from PyQt4.QtCore import pyqtSlot
from model.application import Application

__author__ = 'Alvaro Javier'

class ImageUiSync(object):
    def __init__(self,properties_tree,images_list):
        self._properties_tree = properties_tree
        self._images_list = images_list
        # guarda los ids de las imágenes cargadas, en el mismo orden que se muestran en la lista de
        # imágenes de este widget
        self._images_ids = []
        #Conectar las señales de Qt
        self._images_list.itemSelectionChanged.connect(self._update_image_properties)
        self._properties_tree.itemChanged.connect(self._update_image)
        #definir las propiedades que controla esta clase
        root = self._properties_tree.invisibleRootItem()
        self._id_prop       = root.child(0)
        self._name_prop     = root.child(1)
        self._format_prop   = root.child(2)
        self._file_prop     = root.child(3)
        self._dim_prop      = root.child(4)
        self._pt_prop       = root.child(5)
        self._size_prop     = root.child(6)
        self._sizeX_prop    = root.child(6).child(0)
        self._sizeY_prop    = root.child(6).child(1)
        self._sizeZ_prop    = root.child(6).child(2)
        self._spc_prop      = root.child(7)
        self._spcX_prop     = root.child(7).child(0)
        self._spcY_prop     = root.child(7).child(1)
        self._spcZ_prop     = root.child(7).child(2)

    def add_image(self,img):
        """
        Para notificar a esta clase que se ha agregado una imagen, actualiza la lista de imágenes para
        mostrarla.
        @param img: la nueva imagen, de tipo model.Image
        """
        self._images_list.addItem(img.DisplayName) #mostar en nombre en la lista de imágenes
        self._images_ids.append(img.Id) #agegar el id a la lista de ids

    def get_selected_image_id(self):
        """
        Devuelve el id de la imagen sleccionada en la lista de imágenes.
        @return: el id de la imagen selccionada, de tipo entero, None si no hay ninguna selccionada
        """
        index = self._images_list.currentRow() #obtener el índice de la imagen seleccionada
        if 0<= index < self._images_list.count():
            return self._images_ids[index]
        else:
            return None

    def _update_editable_labels(self):
        """
        Actualiza las etiquetas de los campos editables en los árboles de propiedades para si
        se cambiaron por error
        """
        #restaurar las etiquetas de las propiedades de la imagen
        self._properties_tree.blockSignals(True) #bloquear momentáneamente las señales
        self._name_prop.setText(0,self._properties_tree.tr("Nombre"))
        self._spcX_prop.setText(0,self._properties_tree.tr("X"))
        self._spcY_prop.setText(0,self._properties_tree.tr("Y"))
        self._spcZ_prop.setText(0,self._properties_tree.tr("Z"))
        self._properties_tree.blockSignals(False) #desbloaquear las señales

    @pyqtSlot()
    def _update_image_properties(self):
        """
        Actualiza los campos que muestran las propiedades de la imagen
        """
        index = self._images_list.currentRow() #obtener el índice de la imagen seleccionada
        if 0 <= index < self._images_list.count():
            id = self._images_ids[index] #obtener el id de la imagen según el índice
            img = Application.get_images()[id]
            self._images_list.currentItem().setText(img.DisplayName)
            index = self._images_list.currentRow() #obtener el índice de la imagen seleccionada
            id = self._images_ids[index] #obtener el id de la imagen según el índice
            img = Application.get_images()[id] #imagen para obtener las propiedades
            #actualizar los atributos de la imagen que se muestran
            self._properties_tree.blockSignals(True)
            self._id_prop.setText(1,str(img.Id))
            self._name_prop.setText(1,str(img.DisplayName))
            self._format_prop.setText(1,str(img.OriginalFormat))
            self._file_prop.setText(1,str(img.OriginalFile))
            self._dim_prop.setText(1,str(img.Dimension))
            self._pt_prop.setText(1,str(img.PixelType))
            self._size_prop.setText(1,str(img.Size))
            self._sizeX_prop.setText(1,str(img.Size[0]))
            self._sizeY_prop.setText(1,str(img.Size[1]))
            self._sizeZ_prop.setText(1,str(img.Size[2]))
            self._spc_prop.setText(1,str(img.Spacing))
            self._spcX_prop.setText(1,str(img.Spacing[0]))
            self._spcY_prop.setText(1,str(img.Spacing[1]))
            self._spcZ_prop.setText(1,str(img.Spacing[2]))
            self._properties_tree.blockSignals(False)

    def _update_image(self,item,col):
        """
        Actualiza las propiedades de la imagen luego de haberlas editado
        @param item: item que se editó
        @param col: columna del item que se editó
        @return: None
        """
        #cambiaron la etiqueta de la propiedad no el valor
        if col == 0:
            self._update_editable_labels() #restaurar las etiquetas
            return
        id = self.get_selected_image_id() #obtener el id de la imagen seleccionada
        if id is None: #no se ha seleccionado ninguna imagen
            return
        img = Application.get_images()[id]
        if item.text(0) == "Nombre":
            #actualizamos el nombre
            img.DisplayName = self._name_prop.text(1)
        elif item.text(0) in ["X","Y","Z"]:
            #actualizamos el espaciado
            spc = [self._spcX_prop.text(1),
                   self._spcY_prop.text(1),
                   self._spcZ_prop.text(1)]
            try:
                spc = map(float,spc)
                #verificar que no haya un espaciado mayor que 100 o menor o igual que 0
                if any(map(lambda x: 100.0<=x or x<=0.0,spc)):
                    raise ValueError()
                img.Spacing = spc
            except ValueError:
                pass
        self._update_image_properties()