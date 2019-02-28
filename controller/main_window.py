#! -*- coding: cp1252 -*-
import subprocess

from PyQt4.QtCore import pyqtSlot,Qt, QObject
from PyQt4.QtGui import QMessageBox, QKeySequence, QIcon, QPixmap
from controller.configuration_manager import ConfigurationManager
from controller.filters_ui_sync import FiltersUiSync
from controller.image_loader import ImageLoader
from controller.image_saver import ImageSaver
from controller.image_ui_sync import ImageUiSync
from controller.segmentation_data import SegmentationData
from controller.series_loader import SeriesLoader
from controller.three_planes_visualization import ThreePlanesVisualization
from controller.wait_process import WaitProcess
from model.application import Application
from view.main_window_widget import MainWindowWidget

__author__ = 'Alvaro Javier'

##Clase controladora principal de la aplicación
#
# Esta clase contienen el widget de la ventana principal de la aplicación, ademas de mantener todos los
# componentes de la intefaz interactuando correctamente con las demás clases conroladoras y con el modelo.
#
# @yo
class MainWindow(object):

    ##Inicializador
    # @selfdoc
    def __init__(self):
        ##@var _widget
        # Widget de la ventana principal
        self._widget = MainWindowWidget()
        ##@var _ui
        # Referecia a la interfaz de la vantana principal @see @ref MainWindow::_widget
        self._ui = self._widget.ui
        ui = self._ui
        ##@var _planes
        # Visualización inicial de la imagen según los tres planos del cuerpo
        self._planes = ThreePlanesVisualization(ui.threePlanes)
        ##@var _processed_planes
        # Visualización de la imagen procesada
        self._processed_planes = ThreePlanesVisualization(ui.threePlanesResult)
        #conección de señales de Qt
        ui.useImage.clicked.connect(self._update_image)
        ui.processImage.clicked.connect(self._processImage)
        ui.actionCargar_imagen.triggered.connect(self._load_image)
        ui.actionCargar_serie.triggered.connect(self._load_series)
        ui.actionGuardar.triggered.connect(self._save_image)
        ui.actionGuardar_2.triggered.connect(self._save_configuration)
        ui.actionCargar_configuraci_n.triggered.connect(self._load_configuration)
        ui.imagesList.itemSelectionChanged.connect(self._update_use_button)
        ui.actionAcerca_de.triggered.connect(self._about)
        ui.propertiesTree.itemChanged.connect(self._update_current_image_name)
        ##@var _images_ui_syncronyzer
        # Sincronizador de las propiedades de los filros
        self._images_ui_synchronizer = ImageUiSync(ui.propertiesTree,ui.imagesList)
        ##@var _filters_ui_synchronizer
        # Sincronizador de las propiedades de las imágenes
        self._filters_ui_synchronizer = FiltersUiSync(ui.filtersTree)
        ##@var _segmentation_data
        # Muestra la información de la segmentación
        self._segmentation_data = SegmentationData()
        self._widget.addDockWidget(Qt.TopDockWidgetArea, self._segmentation_data._widget)
        self._segmentation_data._widget.setFloating(True)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/seleccion/show_data.png"), QIcon.Normal,
                       QIcon.Off)
        self._segmentation_data._widget.setWindowIcon(icon)
        self._segmentation_data._widget.toggleViewAction().trigger()
        action = self._segmentation_data._widget.toggleViewAction()
        action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_D))
        action.setIcon(icon)
        trans = QObject()
        action.setToolTip(trans.tr("Datos de la segmentación"))
        action.setIconText(trans.tr("Datos de la segmentación"))
        action.setStatusTip(trans.tr("Mostrar/Ocultar los datos de la segmentación."))
        ui.menuVer.addAction(action)
        ui.toolBar.addAction(action)

        ui.actionAyuda_de_BrainApp.triggered.connect(self._help)

    @pyqtSlot()
    def _help(self):
        import os
        try:
            #subprocess.call([sumatra_path,manual_path])
            os.system("help.bat")
        except Exception:
            pass


    @pyqtSlot()
    def _about(self):
        trans = QObject()
        QMessageBox.about(None,
                          trans.tr("Acerca de BrainApp"),
                          trans.tr(
                          '<table>'
                          '<tr>'
                          '<td colspan=2 style="color:darkblue;font-size:20pt;font-weight:bold"> BrainApp</td>'
                          '</tr>'
                          '<tr>'
                          '<td style="font-weight:bold">Versión:</td>'
                          '<td style="color:red;">0.1</td>'
                          '</tr>'
                          '<tr>'
                          '<td style="font-weight:bold;text-align:right">Autor:</td>'
                          '<td>Alvaro Javier Fuentes Suárez</td>'
                          '</tr>'
                          '<tr>'
                          '<td></td>'
                          '<td style="color:darkgreen;">CIMCNI-UCLV</td>'
                          '</tr>'
                          '<tr>'
                          '<td></td>'
                          '<td><b>2012</b></td>'
                          '</tr>'
                          '<table>'
                          )
        )

    ##Abre el diálogo encargado de salvar la configuración del procesamiento
    #
    # @slot para guardar la configuración del procesamiento
    # @selfdoc
    # @see BrainApp.controller.configuration_manager.ConfigurationManager
    @pyqtSlot()
    def _save_configuration(self):
        conf_manager = ConfigurationManager() #crear al manipulador de la configuración
        conf_manager.save_configuration() #salvar la configuración

    ##Abre el diálogo encargado de cargar la configuración del procesamiento
    #
    # @slot para cargar la configuración del procesamiento
    # @selfdoc
    # @see BrainApp.controller.configuration_manager.ConfigurationManager
    @pyqtSlot()
    def _load_configuration(self):
        conf_manager = ConfigurationManager() #crear al manipulador de la configuración
        conf_manager.load_configuration() #cargar la configuración
        self._filters_ui_synchronizer.update()

    ##Abre el diálogo encargado de salvar la imagen procesada
    #
    # @slot para guardar una imagen
    # @selfdoc
    # @see BrainApp.controller.image_saver.ImageSaver
    @pyqtSlot()
    def _save_image(self):
        img_svr = ImageSaver() #crear el diálogo
        img_svr.saveImage(Application.get_processed_image()) #salvar la imagen

    ##Actualizar el botón de usar/actualizar imagen
    #
    # Si no hay ninguna imagen seleccionada se mantiene el botón de usar/actualizar deshabilitado
    # @selfdoc
    @pyqtSlot()
    def _update_use_button(self):
        self._ui.useImage.setDisabled(self._ui.imagesList.selectedIndexes() == [])

    ##Abre el cargador de imágenes
    # @selfdoc
    # @see BrainApp.controller.image_loader.ImageLoader
    @pyqtSlot()
    def _load_image(self):
        img_ldr = ImageLoader() #crear un cargador
        res,img = img_ldr.run() #ejecutar el cargador
        if res == ImageLoader.OK:
            Application.add_image(img) #agregar la nueva imagen cargada a la aplicación
            #notificar al sincronizador de las propiedades de las imágenes que hay una nueva imagen cargada
            self._images_ui_synchronizer.add_image(img)

    ##Abre el cargador de imágenes en serie
    # @selfdoc
    # @see BrainApp.controller.series_loader.SeriesLoader
    @pyqtSlot()
    def _load_series(self):
        img_ldr = SeriesLoader() #crear un cargador
        res,img = img_ldr.run() #ejecutar el cargador
        if res == ImageLoader.OK:
            Application.add_image(img) #agregar la nueva imagen cargada a la aplicación
            #notificar al sincronizador de las propiedades de las imágenes que hay una nueva imagen cargada
            self._images_ui_synchronizer.add_image(img)

    ##Actualiza la imagen que la aplicación esta usando para el procesamiento
    #
    # @slot al hacer click en el botón de usar/actualizar imagen
    # @selfdoc
    @pyqtSlot()
    def _update_image(self):
        wt = WaitProcess
        wt.run()
        wt.change_info("Obteniendo imagen")
        wt.change_value(5)
        id = self._images_ui_synchronizer.get_selected_image_id()
        #verificar si la imagen seleccionada es distinta de la imagen actual
        clean_pipes = (Application.get_current_image_id() != id)
        #limpia las tuberías en caso de ser necesario
        if id is not None:
            if clean_pipes:
                Application.get_current_document().clean_pipes()
            wt.change_info("Cambiando imagen")
            wt.change_value(50)
            Application.set_current_image_id(id) #cambiar la imagen actual
            img = Application.get_current_image() #obtener la imagen actual
            self._ui.imageName.setText(img.DisplayName) #actualiza el nombre mostrado de la imagen
            wt.change_info("Visualizando imagen")
            wt.change_value(65)
            #actualizar la vista de los tres planos de la imagen
            self._planes.Image = img
            #habilitar el procesameinto de la imagen
            self._ui.processImage.setEnabled(True)
            #habilitar la configuración de los filtros
            self._ui.filters.setEnabled(True)
            #habilitar la salva de la configuración de los filtros
            self._ui.actionGuardar_2.setEnabled(True)
            #habilitar la carga de la configuración de los filtros
            self._ui.actionCargar_configuraci_n.setEnabled(True)
            #actualizar la información de los filtros
            self._filters_ui_synchronizer.update()
        wt.stop()

    ##Actualiza el nombre de la imagen que se muestra encima de la vista de los planos.
    #
    # @slot luego de editar un campo de las propiedades de  la imagen.  Actualiza el nombre mostrado
    # como imagen actual encima de los tres planos.
    # @selfdoc
    # @param item el item editado
    # @param col columna editada dentro del item
    def _update_current_image_name(self,item,col):
        id = self._images_ui_synchronizer.get_selected_image_id()
        img = Application.get_current_image()
        if id is None or img is None:
            return
        if id == img.Id and col == 1 and item.text(0) == "Nombre":
            self._ui.imageName.setText(item.text(1))

    ##Muestra la ventana para que pueda ser ejecutada la aplicación (incioa de la aplicación)
    # @selfdoc
    def run(self):
        self._widget.show() #mostrar la ventana princcipal

    ##Realiza el procesamiento de la imagen según los filtros seleccionados
    #
    # @slot cuando se hace click en el botón de procesar la imagen
    # @selfdoc
    @pyqtSlot()
    def _processImage(self):
        wt = WaitProcess
        wt.run()
        wt.change_value(50)
        wt.change_info("Procesando imagen")
        Application.processImage()
        wt.change_value(80)
        wt.change_info("Visualizando datos")
        #actualizar la vista de los tres planos de la imagen procesada
        self._processed_planes.Image = Application.get_processed_image()
        self._filters_ui_synchronizer._update_filters_properties()
        wt.stop()


