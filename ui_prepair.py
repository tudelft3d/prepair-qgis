# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_prepair.ui'
#
# Created: Thu Jun 12 09:51:17 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Prepair(object):
    def setupUi(self, Prepair):
        Prepair.setObjectName(_fromUtf8("Prepair"))
        Prepair.resize(370, 523)
        self.groupBox_2 = QtGui.QGroupBox(Prepair)
        self.groupBox_2.setGeometry(QtCore.QRect(27, 11, 321, 137))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboLayers = QtGui.QComboBox(self.groupBox_2)
        self.comboLayers.setObjectName(_fromUtf8("comboLayers"))
        self.gridLayout.addWidget(self.comboLayers, 1, 0, 1, 1)
        self.onlySelected = QtGui.QCheckBox(self.groupBox_2)
        self.onlySelected.setObjectName(_fromUtf8("onlySelected"))
        self.gridLayout.addWidget(self.onlySelected, 2, 0, 1, 1)
        self.onlyInvalid = QtGui.QCheckBox(self.groupBox_2)
        self.onlyInvalid.setObjectName(_fromUtf8("onlyInvalid"))
        self.gridLayout.addWidget(self.onlyInvalid, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Prepair)
        self.groupBox.setGeometry(QtCore.QRect(30, 150, 321, 82))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioOddEven = QtGui.QRadioButton(self.groupBox)
        self.radioOddEven.setChecked(True)
        self.radioOddEven.setObjectName(_fromUtf8("radioOddEven"))
        self.verticalLayout_2.addWidget(self.radioOddEven)
        self.radioSetdiff = QtGui.QRadioButton(self.groupBox)
        self.radioSetdiff.setObjectName(_fromUtf8("radioSetdiff"))
        self.verticalLayout_2.addWidget(self.radioSetdiff)
        self.line = QtGui.QFrame(Prepair)
        self.line.setGeometry(QtCore.QRect(30, 300, 321, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.widget = QtGui.QWidget(Prepair)
        self.widget.setGeometry(QtCore.QRect(29, 332, 321, 159))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.prepairPath = QtGui.QLineEdit(self.widget)
        self.prepairPath.setObjectName(_fromUtf8("prepairPath"))
        self.gridLayout_2.addWidget(self.prepairPath, 1, 0, 1, 1)
        self.browsePrepairPath = QtGui.QPushButton(self.widget)
        self.browsePrepairPath.setObjectName(_fromUtf8("browsePrepairPath"))
        self.gridLayout_2.addWidget(self.browsePrepairPath, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)
        self.filename = QtGui.QLineEdit(self.widget)
        self.filename.setText(_fromUtf8(""))
        self.filename.setReadOnly(True)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.gridLayout_2.addWidget(self.filename, 3, 0, 1, 1)
        self.browseOutfile = QtGui.QPushButton(self.widget)
        self.browseOutfile.setObjectName(_fromUtf8("browseOutfile"))
        self.gridLayout_2.addWidget(self.browseOutfile, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.widget1 = QtGui.QWidget(Prepair)
        self.widget1.setGeometry(QtCore.QRect(30, 240, 198, 47))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        self.minarea = QtGui.QLineEdit(self.widget1)
        self.minarea.setObjectName(_fromUtf8("minarea"))
        self.gridLayout_3.addWidget(self.minarea, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.retranslateUi(Prepair)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Prepair.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Prepair.reject)
        QtCore.QMetaObject.connectSlotsByName(Prepair)

    def retranslateUi(self, Prepair):
        Prepair.setWindowTitle(_translate("Prepair", "prepair", None))
        self.groupBox_2.setTitle(_translate("Prepair", "Features to repair", None))
        self.label_3.setText(_translate("Prepair", "Input polygon layers:", None))
        self.onlySelected.setText(_translate("Prepair", "Only selected polygons", None))
        self.onlyInvalid.setText(_translate("Prepair", "Only Invalid polygons", None))
        self.groupBox.setTitle(_translate("Prepair", "Repair algorithm", None))
        self.radioOddEven.setText(_translate("Prepair", "odd-even", None))
        self.radioSetdiff.setText(_translate("Prepair", "setdiff", None))
        self.label_4.setText(_translate("Prepair", "prepair executable path:", None))
        self.browsePrepairPath.setText(_translate("Prepair", "Browse...", None))
        self.label.setText(_translate("Prepair", "Save repaired polygons to:", None))
        self.browseOutfile.setText(_translate("Prepair", "Browse...", None))
        self.label_2.setText(_translate("Prepair", "Delete areas smaller than:", None))
        self.minarea.setText(_translate("Prepair", "0.0", None))
        self.label_5.setText(_translate("Prepair", "unit^2", None))

