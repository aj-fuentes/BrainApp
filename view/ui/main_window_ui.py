# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Jun 20 20:33:02 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/main_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.imageName = QtGui.QLabel(self.centralwidget)
        self.imageName.setText(_fromUtf8(""))
        self.imageName.setObjectName(_fromUtf8("imageName"))
        self.horizontalLayout.addWidget(self.imageName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.threePlanes = ThreePlanesWidget(self.centralwidget)
        self.threePlanes.setStatusTip(_fromUtf8(""))
        self.threePlanes.setObjectName(_fromUtf8("threePlanes"))
        self.verticalLayout_2.addWidget(self.threePlanes)
        self.processImage = QtGui.QCommandLinkButton(self.centralwidget)
        self.processImage.setEnabled(False)
        self.processImage.setObjectName(_fromUtf8("processImage"))
        self.verticalLayout_2.addWidget(self.processImage)
        self.threePlanesResult = ThreePlanesWidget(self.centralwidget)
        self.threePlanesResult.setObjectName(_fromUtf8("threePlanesResult"))
        self.verticalLayout_2.addWidget(self.threePlanesResult)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        self.menuVer = QtGui.QMenu(self.menubar)
        self.menuVer.setObjectName(_fromUtf8("menuVer"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.images = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.images.sizePolicy().hasHeightForWidth())
        self.images.setSizePolicy(sizePolicy)
        self.images.setMinimumSize(QtCore.QSize(251, 162))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/show_images.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images.setWindowIcon(icon1)
        self.images.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.images.setObjectName(_fromUtf8("images"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.imagesList = QtGui.QListWidget(self.dockWidgetContents)
        self.imagesList.setAlternatingRowColors(True)
        self.imagesList.setObjectName(_fromUtf8("imagesList"))
        self.verticalLayout.addWidget(self.imagesList)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.useImage = QtGui.QCommandLinkButton(self.dockWidgetContents)
        self.useImage.setEnabled(False)
        self.useImage.setObjectName(_fromUtf8("useImage"))
        self.verticalLayout_5.addWidget(self.useImage)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.images.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.images)
        self.imageProperties = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageProperties.sizePolicy().hasHeightForWidth())
        self.imageProperties.setSizePolicy(sizePolicy)
        self.imageProperties.setMinimumSize(QtCore.QSize(250, 180))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/show_properties.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageProperties.setWindowIcon(icon2)
        self.imageProperties.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.imageProperties.setObjectName(_fromUtf8("imageProperties"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.propertiesTree = QtGui.QTreeWidget(self.dockWidgetContents_2)
        self.propertiesTree.setAlternatingRowColors(True)
        self.propertiesTree.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.propertiesTree.setAnimated(True)
        self.propertiesTree.setObjectName(_fromUtf8("propertiesTree"))
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.propertiesTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.verticalLayout_3.addWidget(self.propertiesTree)
        self.imageProperties.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.imageProperties)
        self.filters = QtGui.QDockWidget(MainWindow)
        self.filters.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters.sizePolicy().hasHeightForWidth())
        self.filters.setSizePolicy(sizePolicy)
        self.filters.setMinimumSize(QtCore.QSize(250, 180))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/show_filters.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filters.setWindowIcon(icon3)
        self.filters.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.filters.setObjectName(_fromUtf8("filters"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.filtersTree = QtGui.QTreeWidget(self.dockWidgetContents_3)
        self.filtersTree.setEnabled(True)
        self.filtersTree.setAlternatingRowColors(True)
        self.filtersTree.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.filtersTree.setAnimated(True)
        self.filtersTree.setObjectName(_fromUtf8("filtersTree"))
        item_0 = QtGui.QTreeWidgetItem(self.filtersTree)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.filtersTree)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.filtersTree)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.filtersTree)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.filtersTree.header().setDefaultSectionSize(100)
        self.filtersTree.header().setMinimumSectionSize(30)
        self.filtersTree.header().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.filtersTree)
        self.filters.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.filters)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setToolTip(_fromUtf8(""))
        self.toolBar.setStatusTip(_fromUtf8(""))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAyuda_de_BrainApp = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAyuda_de_BrainApp.setIcon(icon4)
        self.actionAyuda_de_BrainApp.setObjectName(_fromUtf8("actionAyuda_de_BrainApp"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setIcon(icon)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.actionCargar_imagen = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/load_image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargar_imagen.setIcon(icon5)
        self.actionCargar_imagen.setObjectName(_fromUtf8("actionCargar_imagen"))
        self.actionSalir = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon6)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionCargar_serie = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/load_serie.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargar_serie.setIcon(icon7)
        self.actionCargar_serie.setObjectName(_fromUtf8("actionCargar_serie"))
        self.actionIm_genes = QtGui.QAction(MainWindow)
        self.actionIm_genes.setCheckable(True)
        self.actionIm_genes.setChecked(True)
        self.actionIm_genes.setIcon(icon1)
        self.actionIm_genes.setObjectName(_fromUtf8("actionIm_genes"))
        self.actionPropiedades_de_la_imagen = QtGui.QAction(MainWindow)
        self.actionPropiedades_de_la_imagen.setCheckable(True)
        self.actionPropiedades_de_la_imagen.setChecked(True)
        self.actionPropiedades_de_la_imagen.setIcon(icon2)
        self.actionPropiedades_de_la_imagen.setObjectName(_fromUtf8("actionPropiedades_de_la_imagen"))
        self.actionFiltros_del_proceso = QtGui.QAction(MainWindow)
        self.actionFiltros_del_proceso.setCheckable(True)
        self.actionFiltros_del_proceso.setChecked(True)
        self.actionFiltros_del_proceso.setIcon(icon3)
        self.actionFiltros_del_proceso.setObjectName(_fromUtf8("actionFiltros_del_proceso"))
        self.actionGuardar = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/save_image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuardar.setIcon(icon8)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionGuardar_2 = QtGui.QAction(MainWindow)
        self.actionGuardar_2.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/save_conf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuardar_2.setIcon(icon9)
        self.actionGuardar_2.setObjectName(_fromUtf8("actionGuardar_2"))
        self.actionCargar_configuraci_n = QtGui.QAction(MainWindow)
        self.actionCargar_configuraci_n.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/load_conf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargar_configuraci_n.setIcon(icon10)
        self.actionCargar_configuraci_n.setObjectName(_fromUtf8("actionCargar_configuraci_n"))
        self.actionBarra_de_herramientas = QtGui.QAction(MainWindow)
        self.actionBarra_de_herramientas.setCheckable(True)
        self.actionBarra_de_herramientas.setChecked(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/seleccion/show_toolbar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBarra_de_herramientas.setIcon(icon11)
        self.actionBarra_de_herramientas.setObjectName(_fromUtf8("actionBarra_de_herramientas"))
        self.menuArchivo.addAction(self.actionCargar_imagen)
        self.menuArchivo.addAction(self.actionCargar_serie)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar_2)
        self.menuArchivo.addAction(self.actionCargar_configuraci_n)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAyuda_de_BrainApp)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuVer.addAction(self.actionBarra_de_herramientas)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.actionIm_genes)
        self.menuVer.addAction(self.actionPropiedades_de_la_imagen)
        self.menuVer.addAction(self.actionFiltros_del_proceso)
        self.menuVer.addSeparator()
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionCargar_imagen)
        self.toolBar.addAction(self.actionCargar_serie)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGuardar_2)
        self.toolBar.addAction(self.actionCargar_configuraci_n)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionIm_genes)
        self.toolBar.addAction(self.actionPropiedades_de_la_imagen)
        self.toolBar.addAction(self.actionFiltros_del_proceso)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionIm_genes, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.images.setVisible)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionPropiedades_de_la_imagen, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.imageProperties.setVisible)
        QtCore.QObject.connect(self.images, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionIm_genes.setChecked)
        QtCore.QObject.connect(self.imageProperties, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionPropiedades_de_la_imagen.setChecked)
        QtCore.QObject.connect(self.filters, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionFiltros_del_proceso.setChecked)
        QtCore.QObject.connect(self.actionFiltros_del_proceso, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.filters.setVisible)
        QtCore.QObject.connect(self.actionBarra_de_herramientas, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.toolBar.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BrainApp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Imagen mostrada:", None, QtGui.QApplication.UnicodeUTF8))
        self.processImage.setStatusTip(QtGui.QApplication.translate("MainWindow", "Procesar la imagen con los filtros seleccionados.", None, QtGui.QApplication.UnicodeUTF8))
        self.processImage.setText(QtGui.QApplication.translate("MainWindow", "Procesar imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.processImage.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F5", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVer.setTitle(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.images.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Imágenes cargadas", None, QtGui.QApplication.UnicodeUTF8))
        self.imagesList.setStatusTip(QtGui.QApplication.translate("MainWindow", "Lista de imágenes cargadas.", None, QtGui.QApplication.UnicodeUTF8))
        self.useImage.setStatusTip(QtGui.QApplication.translate("MainWindow", "Usar esta imagen en el proceso.", None, QtGui.QApplication.UnicodeUTF8))
        self.useImage.setText(QtGui.QApplication.translate("MainWindow", "Usar/Actualizar esta imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.useImage.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.imageProperties.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Propiedades de la imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.setStatusTip(QtGui.QApplication.translate("MainWindow", "Propiedades de la imagen seleccionada.", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Propiedad", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.propertiesTree.isSortingEnabled()
        self.propertiesTree.setSortingEnabled(False)
        self.propertiesTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "Formato", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "Fichero", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(4).setText(0, QtGui.QApplication.translate("MainWindow", "Dimensión", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(5).setText(0, QtGui.QApplication.translate("MainWindow", "Tipo de Pixel", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(6).setText(0, QtGui.QApplication.translate("MainWindow", "Tamaño", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(6).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Ancho", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(6).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Alto", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(6).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Profundidad", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(7).setText(0, QtGui.QApplication.translate("MainWindow", "Espaciado", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(7).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(7).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.topLevelItem(7).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesTree.setSortingEnabled(__sortingEnabled)
        self.filters.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Filtros del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.filtersTree.isSortingEnabled()
        self.filtersTree.setSortingEnabled(False)
        self.filtersTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Suavizador", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Iteraciones", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Paso de tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Conductancia", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Segmentador", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Semilla", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Mínimo", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Máximo", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(1).child(3).setText(0, QtGui.QApplication.translate("MainWindow", "Relleno", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "Segmentador estadístico", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Semilla", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Radio inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Multiplicador", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(3).setText(0, QtGui.QApplication.translate("MainWindow", "Relleno", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(2).child(4).setText(0, QtGui.QApplication.translate("MainWindow", "Iteraciones", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "Votación", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Radio", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Fondo", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Máscara", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(3).setText(0, QtGui.QApplication.translate("MainWindow", "Supervivencia", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.topLevelItem(3).child(4).setText(0, QtGui.QApplication.translate("MainWindow", "Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersTree.setSortingEnabled(__sortingEnabled)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Barra de Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda_de_BrainApp.setText(QtGui.QApplication.translate("MainWindow", "Ayuda de BrainApp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda_de_BrainApp.setStatusTip(QtGui.QApplication.translate("MainWindow", "Obtener ayuda.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda_de_BrainApp.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setStatusTip(QtGui.QApplication.translate("MainWindow", "Acerca de BrainApp.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_imagen.setText(QtGui.QApplication.translate("MainWindow", "Cargar imagen...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_imagen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cargar una imgen 3D o 2D desde un fichero.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_imagen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setStatusTip(QtGui.QApplication.translate("MainWindow", "Salir de la aplicación.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_serie.setText(QtGui.QApplication.translate("MainWindow", "Cargar serie...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_serie.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cargar una serie de imáges 2D para obtener un volumen 3D.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_serie.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIm_genes.setText(QtGui.QApplication.translate("MainWindow", "Imágenes cargadas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIm_genes.setToolTip(QtGui.QApplication.translate("MainWindow", "Imágenes cargadas.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIm_genes.setStatusTip(QtGui.QApplication.translate("MainWindow", "Mostrar/Ocultar las imágenes cargadas.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIm_genes.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropiedades_de_la_imagen.setText(QtGui.QApplication.translate("MainWindow", "Propiedades de la imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropiedades_de_la_imagen.setToolTip(QtGui.QApplication.translate("MainWindow", "Propiedades de la imagen.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropiedades_de_la_imagen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Mostrar/Ocultar las propiedades de las imágenes cargadas.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropiedades_de_la_imagen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFiltros_del_proceso.setText(QtGui.QApplication.translate("MainWindow", "Filtros del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFiltros_del_proceso.setToolTip(QtGui.QApplication.translate("MainWindow", "Filtros del proceso.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFiltros_del_proceso.setStatusTip(QtGui.QApplication.translate("MainWindow", "Mostrar/Ocultar los filtros del proceso.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFiltros_del_proceso.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("MainWindow", "Guardar imagen...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setToolTip(QtGui.QApplication.translate("MainWindow", "Guardar la imagen procesada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setStatusTip(QtGui.QApplication.translate("MainWindow", "Guardar la imagen procesada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar_2.setText(QtGui.QApplication.translate("MainWindow", "Guardar configuración...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Guardar la configuración de los filtros en un fichero.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar_2.setStatusTip(QtGui.QApplication.translate("MainWindow", "Guardar la configuración de los filtros en un fichero.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_configuraci_n.setText(QtGui.QApplication.translate("MainWindow", "Cargar configuración...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_configuraci_n.setToolTip(QtGui.QApplication.translate("MainWindow", "Cargar la configuración de los filtros desde un fichero.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_configuraci_n.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cargar la configuración de los filtros desde un fichero.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBarra_de_herramientas.setText(QtGui.QApplication.translate("MainWindow", "Barra de herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBarra_de_herramientas.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))

from view.three_planes_widget import ThreePlanesWidget
import icons_rc
