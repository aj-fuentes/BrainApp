from PyQt4.QtGui import QApplication, QMainWindow
import itk
import sys
import vtk
from controller.configuration_manager import ConfigurationManager
from controller.image_loader import ImageLoader
from controller.interface_runner import InterfaceRunner
from controller.main_window import MainWindow
from controller.slice_visualization import SliceVisualization
from controller.three_planes_visualization import ThreePlanesVisualization
from model.application import Application
from model.image import Image


__author__ = 'Alvaro Javier'

#app = QApplication([])


#app.exec_()


Application.init()
InterfaceRunner.init()
ConfigurationManager.init()
main_wnidow = MainWindow()
InterfaceRunner.start_even_loop(main_wnidow)


#img_ldr = ImageLoader()
#res,img = img_ldr.run()
#if res == ImageLoader.Canceled:
#    sys.exit(1)

#img = Application.Images()[0]

#img.InternalImage.SetSpacing((1.015625, 1.015625, 1.800000))
#img.InternalImage.SetSpacing((0.9375, 0.9375, 3.1))

#main = QMainWindow()

#vis = ThreePlanesVisualization()
#vis.setFixedPlanes()
#vis = SliceVisualization()
#vis.Image = img

#main.setCentralWidget(vis.Widget)

#main.show()

#vis.Image = img

#app.exec_()
