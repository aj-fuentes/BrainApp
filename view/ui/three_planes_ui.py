# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'three_planes.ui'
#
# Created: Sun Mar 25 22:04:54 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(626, 216)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.coronalPlane = SliceVisualizationWidget(Form)
        self.coronalPlane.setObjectName(_fromUtf8("coronalPlane"))
        self.horizontalLayout.addWidget(self.coronalPlane)
        self.axialPlane = SliceVisualizationWidget(Form)
        self.axialPlane.setObjectName(_fromUtf8("axialPlane"))
        self.horizontalLayout.addWidget(self.axialPlane)
        self.sagittalPlane = SliceVisualizationWidget(Form)
        self.sagittalPlane.setObjectName(_fromUtf8("sagittalPlane"))
        self.horizontalLayout.addWidget(self.sagittalPlane)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

from view.slice_visualization_widget import SliceVisualizationWidget
