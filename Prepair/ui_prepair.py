# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_prepair.ui'
#
# Created: Mon Mar  3 11:46:35 2014
#      by: PyQt4 UI code generator 4.10.3
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
        Prepair.resize(400, 469)
        self.buttonBox = QtGui.QDialogButtonBox(Prepair)
        self.buttonBox.setGeometry(QtCore.QRect(50, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.onlySelected = QtGui.QCheckBox(Prepair)
        self.onlySelected.setGeometry(QtCore.QRect(40, 220, 191, 20))
        self.onlySelected.setObjectName(_fromUtf8("onlySelected"))
        self.groupBox = QtGui.QGroupBox(Prepair)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 211, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioOddEven = QtGui.QRadioButton(self.groupBox)
        self.radioOddEven.setGeometry(QtCore.QRect(20, 30, 102, 20))
        self.radioOddEven.setChecked(True)
        self.radioOddEven.setObjectName(_fromUtf8("radioOddEven"))
        self.radioSetdiff = QtGui.QRadioButton(self.groupBox)
        self.radioSetdiff.setGeometry(QtCore.QRect(20, 60, 102, 20))
        self.radioSetdiff.setObjectName(_fromUtf8("radioSetdiff"))
        self.layoutWidget = QtGui.QWidget(Prepair)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 260, 331, 67))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.browseOutfile = QtGui.QPushButton(self.layoutWidget)
        self.browseOutfile.setObjectName(_fromUtf8("browseOutfile"))
        self.gridLayout.addWidget(self.browseOutfile, 0, 1, 1, 1)
        self.filename = QtGui.QLineEdit(self.layoutWidget)
        self.filename.setText(_fromUtf8(""))
        self.filename.setReadOnly(True)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.gridLayout.addWidget(self.filename, 0, 0, 1, 1)
        self.label = QtGui.QLabel(Prepair)
        self.label.setGeometry(QtCore.QRect(30, 240, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Prepair)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 151, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.minarea = QtGui.QLineEdit(Prepair)
        self.minarea.setGeometry(QtCore.QRect(210, 150, 71, 22))
        self.minarea.setObjectName(_fromUtf8("minarea"))

        self.retranslateUi(Prepair)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Prepair.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Prepair.reject)
        QtCore.QMetaObject.connectSlotsByName(Prepair)

    def retranslateUi(self, Prepair):
        Prepair.setWindowTitle(_translate("Prepair", "Prepair", None))
        self.onlySelected.setText(_translate("Prepair", "Only selected polygons", None))
        self.groupBox.setTitle(_translate("Prepair", "Algorithm", None))
        self.radioOddEven.setText(_translate("Prepair", "odd-even", None))
        self.radioSetdiff.setText(_translate("Prepair", "setdiff", None))
        self.browseOutfile.setText(_translate("Prepair", "Browse...", None))
        self.label.setText(_translate("Prepair", "Save repaired polygons to:", None))
        self.label_2.setText(_translate("Prepair", "Minimum area (unit^2):", None))
        self.minarea.setText(_translate("Prepair", "0.0", None))

