#! -*- coding: cp1252 -*-

from PyQt4.QtGui import QFileDialog, QErrorMessage
import itk, os, subprocess
from model.application import Application
from view.segmentation_data_widget import SegmentationDataWidget

__author__ = 'Alvaro Javier'

class SegmentationData(object):
    def __init__(self,widget=None):
        if widget is None:
            widget = SegmentationDataWidget()
        self._widget = widget
        self._ui = self._widget.ui

        self._ui.calculate.clicked.connect(self.update_data)
        self._ui.save.clicked.connect(self._save_data)

        # Diálogo de Qt para salvar un fichero
        self._file_dialog = QFileDialog()
        #configuración del fileDialog de Qt
        self._file_dialog.setAcceptMode(QFileDialog.AcceptSave) #Sólo se acepta salvar fichero
        self._file_dialog.setViewMode(QFileDialog.Detail) #La vista se muestra en detalles

        root = self._ui.data.invisibleRootItem()
        self._vol_data          = root.child(0)
        self._len_data          = root.child(1)
        self._lenX_data         = root.child(1).child(0)
        self._lenX_start_data   = root.child(1).child(0).child(0)
        self._lenX_end_data     = root.child(1).child(0).child(1)
        self._lenY_data         = root.child(1).child(1)
        self._lenY_start_data   = root.child(1).child(1).child(0)
        self._lenY_end_data     = root.child(1).child(1).child(1)
        self._lenZ_data         = root.child(1).child(2)
        self._lenZ_start_data   = root.child(1).child(2).child(0)
        self._lenZ_end_data     = root.child(1).child(2).child(1)

        self._image = None
        self._calculate_data()

        import os.path
        path  = os.path.dirname(__file__)
        path =  path[:path.rfind(os.sep)]

        self._root_path = path
        self._volume_exec_path = path+os.sep+"volume.exe"
        self._volume_file_path = path+os.sep+"data"+os.sep+"volume"
        self._temp_file_path = path+os.sep+"data"+os.sep+"__temp__.tif"

    def _save_data(self):
        res = self._file_dialog.exec_() #ejecutar el diálogo para obtener el nombre del fichero
        if res == QFileDialog.Rejected: #se canceló la salva
            return
        file_name = str(self._file_dialog.selectedFiles()[0]) #obtener el nombre del fichero

        f = open(file_name,"wt")
        try:
            f.write("Volumen: "                     +str(self._vol)                             +"\n")
            f.write("Longitudes máximas X,Y,Z: "    +str([self._lenX,self._lenY,self._lenZ])    +"\n")
            f.write("  Longitud eje X: "            +str(self._lenX)                            +"\n")
            f.write("    Coordenanda incial eje X: "+str(self._startX)                          +"\n")
            f.write("    Coordenanda final eje X: " +str(self._endX)                            +"\n")
            f.write("  Longitud eje Y: "            +str(self._lenY)                            +"\n")
            f.write("    Coordenanda incial eje Y: "+str(self._startY)                          +"\n")
            f.write("    Coordenanda final eje Y: " +str(self._endY)                            +"\n")
            f.write("  Longitud eje Z: "            +str(self._lenZ)                            +"\n")
            f.write("    Coordenanda incial eje Z: "+str(self._startZ)                          +"\n")
            f.write("    Coordenanda final eje Z: " +str(self._endZ)                            +"\n")
        finally:
            f.close()

    def _calculate_data(self):
        img = Application.get_processed_image()
        if img is None:
            return

        self._ui.calculate.setEnabled(False)

        writer = itk.ImageFileWriter[img.ImageType].New() #crear el writer de ITK
        writer.SetFileName(self._temp_file_path) #ponerle el nombre seleccionado
        writer.SetInput(img.InternalImage) #conectar la imagen a guardar
        writer.Update() #guardar la imagen!


        subprocess.call([self._volume_exec_path,self._temp_file_path,self._volume_file_path])
        #os.system('"'+self._volume_exec_path+'" "'+self._temp_file_path+'" '+self._volume_file_path)

        spc = img.Spacing
        spc_factor = spc[0]*spc[1]*spc[2];

        f = open(self._volume_file_path,'rt')
        try:
            self._vol = float(f.readline())*spc_factor

            self._lenX = float(f.readline())*spc[0]
            self._startX = map(int,f.readline()[1:-2].split(", "))
            self._endX =  map(int,f.readline()[1:-2].split(", "))

            self._lenY = float(f.readline())*spc[1]
            self._startY = map(int,f.readline()[1:-2].split(", "))
            self._endY =  map(int,f.readline()[1:-2].split(", "))

            self._lenZ = float(f.readline())*spc[2]
            self._startZ = map(int,f.readline()[1:-2].split(", "))
            self._endZ =  map(int,f.readline()[1:-2].split(", "))
        finally:
            f.close()

        self._update_labels()
        self._ui.calculate.setEnabled(True)
        self._ui.save.setEnabled(True)

    def _update_labels(self):
        self._vol_data.setText(         1,str(self._vol)                            )
        self._len_data.setText(         1,str([self._lenX,self._lenY,self._lenZ])   )
        self._lenX_data.setText(        1,str(self._lenX)                           )
        self._lenX_start_data.setText(  1,str(self._startX)                         )
        self._lenX_end_data.setText(    1,str(self._endX)                           )
        self._lenY_data.setText(        1,str(self._lenY)                           )
        self._lenY_start_data.setText(  1,str(self._startY)                         )
        self._lenY_end_data.setText(    1,str(self._endY)                           )
        self._lenZ_data.setText(        1,str(self._lenZ)                           )
        self._lenZ_start_data.setText(  1,str(self._startZ)                         )
        self._lenZ_end_data.setText(    1,str(self._endZ)                           )

    def update_data(self):
        self._calculate_data()

