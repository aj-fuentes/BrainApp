# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slice_visualization.ui'
#
# Created: Mon Mar 26 00:26:05 2012
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
        Form.resize(463, 300)
        Form.setMinimumSize(QtCore.QSize(1, 0))
        Form.setStyleSheet(_fromUtf8("#Form {\n"
"border: 1px solid black;\n"
"}"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.invert = QtGui.QCheckBox(Form)
        self.invert.setMinimumSize(QtCore.QSize(16, 16))
        self.invert.setMaximumSize(QtCore.QSize(16, 16))
        self.invert.setText(_fromUtf8(""))
        self.invert.setObjectName(_fromUtf8("invert"))
        self.verticalLayout.addWidget(self.invert)
        self.XButton = QtGui.QPushButton(Form)
        self.XButton.setEnabled(False)
        self.XButton.setMinimumSize(QtCore.QSize(16, 16))
        self.XButton.setMaximumSize(QtCore.QSize(16, 16))
        self.XButton.setStyleSheet(_fromUtf8(""))
        self.XButton.setCheckable(True)
        self.XButton.setChecked(False)
        self.XButton.setAutoExclusive(True)
        self.XButton.setFlat(False)
        self.XButton.setObjectName(_fromUtf8("XButton"))
        self.buttonGroup = QtGui.QButtonGroup(Form)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.XButton)
        self.verticalLayout.addWidget(self.XButton)
        self.YButton = QtGui.QPushButton(Form)
        self.YButton.setEnabled(True)
        self.YButton.setMinimumSize(QtCore.QSize(16, 16))
        self.YButton.setMaximumSize(QtCore.QSize(16, 16))
        self.YButton.setStyleSheet(_fromUtf8(""))
        self.YButton.setCheckable(True)
        self.YButton.setChecked(True)
        self.YButton.setAutoExclusive(True)
        self.YButton.setObjectName(_fromUtf8("YButton"))
        self.buttonGroup.addButton(self.YButton)
        self.verticalLayout.addWidget(self.YButton)
        self.ZButton = QtGui.QPushButton(Form)
        self.ZButton.setMinimumSize(QtCore.QSize(16, 16))
        self.ZButton.setMaximumSize(QtCore.QSize(16, 16))
        self.ZButton.setStyleSheet(_fromUtf8(""))
        self.ZButton.setCheckable(True)
        self.ZButton.setAutoExclusive(True)
        self.ZButton.setObjectName(_fromUtf8("ZButton"))
        self.buttonGroup.addButton(self.ZButton)
        self.verticalLayout.addWidget(self.ZButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.visualization = QVTKRenderWindowInteractor(Form)
        self.visualization.setObjectName(_fromUtf8("visualization"))
        self.horizontalLayout_3.addWidget(self.visualization)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ZButton_2 = QtGui.QPushButton(Form)
        self.ZButton_2.setMinimumSize(QtCore.QSize(16, 16))
        self.ZButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.ZButton_2.setStyleSheet(_fromUtf8(""))
        self.ZButton_2.setCheckable(True)
        self.ZButton_2.setAutoExclusive(True)
        self.ZButton_2.setObjectName(_fromUtf8("ZButton_2"))
        self.horizontalLayout.addWidget(self.ZButton_2)
        self.YButton_2 = QtGui.QPushButton(Form)
        self.YButton_2.setEnabled(False)
        self.YButton_2.setMinimumSize(QtCore.QSize(16, 16))
        self.YButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.YButton_2.setStyleSheet(_fromUtf8(""))
        self.YButton_2.setCheckable(True)
        self.YButton_2.setChecked(False)
        self.YButton_2.setAutoExclusive(True)
        self.YButton_2.setObjectName(_fromUtf8("YButton_2"))
        self.horizontalLayout.addWidget(self.YButton_2)
        self.XButton_2 = QtGui.QPushButton(Form)
        self.XButton_2.setEnabled(True)
        self.XButton_2.setMinimumSize(QtCore.QSize(16, 16))
        self.XButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.XButton_2.setStyleSheet(_fromUtf8(""))
        self.XButton_2.setCheckable(True)
        self.XButton_2.setChecked(True)
        self.XButton_2.setAutoExclusive(True)
        self.XButton_2.setFlat(False)
        self.XButton_2.setObjectName(_fromUtf8("XButton_2"))
        self.horizontalLayout.addWidget(self.XButton_2)
        self.invert_2 = QtGui.QCheckBox(Form)
        self.invert_2.setMinimumSize(QtCore.QSize(16, 16))
        self.invert_2.setMaximumSize(QtCore.QSize(16, 16))
        self.invert_2.setText(_fromUtf8(""))
        self.invert_2.setObjectName(_fromUtf8("invert_2"))
        self.horizontalLayout.addWidget(self.invert_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.sliceSelector = QtGui.QSlider(Form)
        self.sliceSelector.setOrientation(QtCore.Qt.Horizontal)
        self.sliceSelector.setObjectName(_fromUtf8("sliceSelector"))
        self.horizontalLayout_4.addWidget(self.sliceSelector)
        self.sliceNum = QtGui.QLineEdit(Form)
        self.sliceNum.setMinimumSize(QtCore.QSize(29, 20))
        self.sliceNum.setMaximumSize(QtCore.QSize(29, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sliceNum.setFont(font)
        self.sliceNum.setStyleSheet(_fromUtf8("* {\n"
"border: none;\n"
"background-color: hsva(0,0,0, 0%)\n"
"}"))
        self.sliceNum.setMaxLength(3)
        self.sliceNum.setObjectName(_fromUtf8("sliceNum"))
        self.horizontalLayout_4.addWidget(self.sliceNum)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.XButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.XButton_2.setDisabled)
        QtCore.QObject.connect(self.XButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.XButton.setDisabled)
        QtCore.QObject.connect(self.YButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.YButton_2.setDisabled)
        QtCore.QObject.connect(self.YButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.YButton.setDisabled)
        QtCore.QObject.connect(self.ZButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.ZButton_2.setDisabled)
        QtCore.QObject.connect(self.ZButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.ZButton.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.XButton.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.YButton.setText(QtGui.QApplication.translate("Form", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.ZButton.setText(QtGui.QApplication.translate("Form", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.ZButton_2.setText(QtGui.QApplication.translate("Form", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.YButton_2.setText(QtGui.QApplication.translate("Form", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.XButton_2.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.sliceNum.setText(QtGui.QApplication.translate("Form", "000", None, QtGui.QApplication.UnicodeUTF8))

from view.qvtk_render_window_interactor import QVTKRenderWindowInteractor
