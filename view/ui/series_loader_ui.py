# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'series_loader.ui'
#
# Created: Wed Apr 11 19:51:38 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(338, 284)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fileName = QtGui.QLineEdit(Dialog)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.horizontalLayout.addWidget(self.fileName)
        self.findFile = QtGui.QPushButton(Dialog)
        self.findFile.setMinimumSize(QtCore.QSize(31, 23))
        self.findFile.setMaximumSize(QtCore.QSize(31, 23))
        self.findFile.setObjectName(_fromUtf8("findFile"))
        self.horizontalLayout.addWidget(self.findFile)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.start = QtGui.QSpinBox(self.groupBox)
        self.start.setMinimum(-999)
        self.start.setMaximum(999)
        self.start.setObjectName(_fromUtf8("start"))
        self.horizontalLayout_2.addWidget(self.start)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.end = QtGui.QSpinBox(self.groupBox)
        self.end.setMinimum(-999)
        self.end.setMaximum(999)
        self.end.setObjectName(_fromUtf8("end"))
        self.horizontalLayout_2.addWidget(self.end)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pixelText = QtGui.QLabel(self.groupBox_3)
        self.pixelText.setEnabled(True)
        self.pixelText.setObjectName(_fromUtf8("pixelText"))
        self.horizontalLayout_6.addWidget(self.pixelText)
        self.pixelType = QtGui.QComboBox(self.groupBox_3)
        self.pixelType.setEnabled(True)
        self.pixelType.setEditable(False)
        self.pixelType.setObjectName(_fromUtf8("pixelType"))
        self.horizontalLayout_6.addWidget(self.pixelType)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.rawImage = QtGui.QGroupBox(self.groupBox_3)
        self.rawImage.setFlat(True)
        self.rawImage.setCheckable(True)
        self.rawImage.setChecked(False)
        self.rawImage.setObjectName(_fromUtf8("rawImage"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.rawImage)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.widthText = QtGui.QLabel(self.rawImage)
        self.widthText.setEnabled(False)
        self.widthText.setObjectName(_fromUtf8("widthText"))
        self.horizontalLayout_8.addWidget(self.widthText)
        self.widthValue = QtGui.QSpinBox(self.rawImage)
        self.widthValue.setSuffix(_fromUtf8(""))
        self.widthValue.setMinimum(0)
        self.widthValue.setMaximum(999)
        self.widthValue.setProperty("value", 256)
        self.widthValue.setObjectName(_fromUtf8("widthValue"))
        self.horizontalLayout_8.addWidget(self.widthValue)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.heightText = QtGui.QLabel(self.rawImage)
        self.heightText.setEnabled(False)
        self.heightText.setObjectName(_fromUtf8("heightText"))
        self.horizontalLayout_9.addWidget(self.heightText)
        self.heightValue = QtGui.QSpinBox(self.rawImage)
        self.heightValue.setSuffix(_fromUtf8(""))
        self.heightValue.setPrefix(_fromUtf8(""))
        self.heightValue.setMaximum(999)
        self.heightValue.setProperty("value", 256)
        self.heightValue.setObjectName(_fromUtf8("heightValue"))
        self.horizontalLayout_9.addWidget(self.heightValue)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_2.addWidget(self.rawImage)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.fileName)
        self.label_2.setBuddy(self.start)
        self.label_3.setBuddy(self.end)
        self.pixelText.setBuddy(self.pixelType)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.rawImage, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widthText.setEnabled)
        QtCore.QObject.connect(self.rawImage, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widthValue.setEnabled)
        QtCore.QObject.connect(self.rawImage, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.heightText.setEnabled)
        QtCore.QObject.connect(self.rawImage, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.heightValue.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Cargar serie de imágenes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Fichero:", None, QtGui.QApplication.UnicodeUTF8))
        self.findFile.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Serie de nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Inicio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Fin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Use el comodín %d donde desee poner los números de la serie", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Formato", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelText.setText(QtGui.QApplication.translate("Dialog", "Tipo de pixel", None, QtGui.QApplication.UnicodeUTF8))
        self.rawImage.setTitle(QtGui.QApplication.translate("Dialog", "Imagen Raw", None, QtGui.QApplication.UnicodeUTF8))
        self.widthText.setText(QtGui.QApplication.translate("Dialog", "Ancho:", None, QtGui.QApplication.UnicodeUTF8))
        self.heightText.setText(QtGui.QApplication.translate("Dialog", "Alto:", None, QtGui.QApplication.UnicodeUTF8))

