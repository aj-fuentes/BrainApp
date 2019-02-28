# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segmentation_data.ui'
#
# Created: Mon Jun 04 20:22:40 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(284, 249)
        DockWidget.setFloating(True)
        DockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.data = QtGui.QTreeWidget(self.dockWidgetContents)
        self.data.setObjectName(_fromUtf8("data"))
        item_0 = QtGui.QTreeWidgetItem(self.data)
        item_0 = QtGui.QTreeWidgetItem(self.data)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        self.data.header().setDefaultSectionSize(150)
        self.data.header().setHighlightSections(False)
        self.verticalLayout.addWidget(self.data)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.calculate = QtGui.QCommandLinkButton(self.dockWidgetContents)
        self.calculate.setObjectName(_fromUtf8("calculate"))
        self.verticalLayout_2.addWidget(self.calculate)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.save = QtGui.QCommandLinkButton(self.dockWidgetContents)
        self.save.setEnabled(False)
        self.save.setObjectName(_fromUtf8("save"))
        self.verticalLayout.addWidget(self.save)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "Datos de la segmentación", None, QtGui.QApplication.UnicodeUTF8))
        self.data.headerItem().setText(0, QtGui.QApplication.translate("DockWidget", "Dato", None, QtGui.QApplication.UnicodeUTF8))
        self.data.headerItem().setText(1, QtGui.QApplication.translate("DockWidget", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.data.isSortingEnabled()
        self.data.setSortingEnabled(False)
        self.data.topLevelItem(0).setText(0, QtGui.QApplication.translate("DockWidget", "Volumen", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).setText(0, QtGui.QApplication.translate("DockWidget", "Longitudes", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "Longitud eje X", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(0).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "Coordenada inicial X", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(0).child(1).setText(0, QtGui.QApplication.translate("DockWidget", "Coordenada final X", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("DockWidget", "Longitud eje Y", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(1).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "Coordenada inicial Y", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(1).child(1).setText(0, QtGui.QApplication.translate("DockWidget", "Coordenada final Y", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("DockWidget", "Longitud eje Z", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(2).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "Coordenada inicial Z", None, QtGui.QApplication.UnicodeUTF8))
        self.data.topLevelItem(1).child(2).child(1).setText(0, QtGui.QApplication.translate("DockWidget", "Coordenada final Z", None, QtGui.QApplication.UnicodeUTF8))
        self.data.setSortingEnabled(__sortingEnabled)
        self.calculate.setText(QtGui.QApplication.translate("DockWidget", "Calcular datos", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("DockWidget", "Guardar datos", None, QtGui.QApplication.UnicodeUTF8))

