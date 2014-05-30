# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_prepair.ui'
#
# Created: Fri May 30 19:09:48 2014
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
        Prepair.resize(378, 425)
        self.layoutWidget = QtGui.QWidget(Prepair)
        self.layoutWidget.setGeometry(QtCore.QRect(34, 13, 314, 383))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.comboLayers = QtGui.QComboBox(self.layoutWidget)
        self.comboLayers.setObjectName(_fromUtf8("comboLayers"))
        self.horizontalLayout.addWidget(self.comboLayers)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.onlySelected = QtGui.QCheckBox(self.layoutWidget)
        self.onlySelected.setObjectName(_fromUtf8("onlySelected"))
        self.verticalLayout_2.addWidget(self.onlySelected)
        self.onlyInvalid = QtGui.QCheckBox(self.layoutWidget)
        self.onlyInvalid.setObjectName(_fromUtf8("onlyInvalid"))
        self.verticalLayout_2.addWidget(self.onlyInvalid)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioOddEven = QtGui.QRadioButton(self.groupBox)
        self.radioOddEven.setChecked(True)
        self.radioOddEven.setObjectName(_fromUtf8("radioOddEven"))
        self.verticalLayout_3.addWidget(self.radioOddEven)
        self.radioSetdiff = QtGui.QRadioButton(self.groupBox)
        self.radioSetdiff.setObjectName(_fromUtf8("radioSetdiff"))
        self.verticalLayout_3.addWidget(self.radioSetdiff)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.minarea = QtGui.QLineEdit(self.layoutWidget)
        self.minarea.setObjectName(_fromUtf8("minarea"))
        self.horizontalLayout_2.addWidget(self.minarea)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.browseOutfile = QtGui.QPushButton(self.layoutWidget)
        self.browseOutfile.setObjectName(_fromUtf8("browseOutfile"))
        self.gridLayout.addWidget(self.browseOutfile, 0, 1, 1, 1)
        self.filename = QtGui.QLineEdit(self.layoutWidget)
        self.filename.setText(_fromUtf8(""))
        self.filename.setReadOnly(True)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.gridLayout.addWidget(self.filename, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.prepairPath = QtGui.QLineEdit(self.layoutWidget)
        self.prepairPath.setObjectName(_fromUtf8("prepairPath"))
        self.horizontalLayout_3.addWidget(self.prepairPath)
        self.browsePrepairPath = QtGui.QPushButton(self.layoutWidget)
        self.browsePrepairPath.setObjectName(_fromUtf8("browsePrepairPath"))
        self.horizontalLayout_3.addWidget(self.browsePrepairPath)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(Prepair)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Prepair.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Prepair.reject)
        QtCore.QMetaObject.connectSlotsByName(Prepair)

    def retranslateUi(self, Prepair):
        Prepair.setWindowTitle(_translate("Prepair", "prepair", None))
        self.label_3.setText(_translate("Prepair", "Input polygon layers:", None))
        self.onlySelected.setText(_translate("Prepair", "Only selected polygons", None))
        self.onlyInvalid.setText(_translate("Prepair", "Only Invalid polygons", None))
        self.groupBox.setTitle(_translate("Prepair", "Algorithm", None))
        self.radioOddEven.setText(_translate("Prepair", "odd-even", None))
        self.radioSetdiff.setText(_translate("Prepair", "setdiff", None))
        self.label_2.setText(_translate("Prepair", "Minimum area (unit^2):", None))
        self.minarea.setText(_translate("Prepair", "0.0", None))
        self.label.setText(_translate("Prepair", "Save repaired polygons to:", None))
        self.browseOutfile.setText(_translate("Prepair", "Browse...", None))
        self.label_4.setText(_translate("Prepair", "prepair executable path:", None))
        self.browsePrepairPath.setText(_translate("Prepair", "Browse...", None))

