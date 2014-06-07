# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PrepairDialog
                                 A QGIS plugin
 Automatic repair of single polygons
                             -------------------
        begin                : 2014-03-03
        copyright            : (C) 2014 by GIS technology group at TU Delft
        email                : https://github.com/tudelft-gist
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_prepair import Ui_Prepair
# create the dialog for zoom to point


class PrepairDialog(QtGui.QDialog, Ui_Prepair):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        QtCore.QObject.connect(self.browseOutfile,     QtCore.SIGNAL("clicked()"), self.browse_outfile)
        QtCore.QObject.connect(self.browsePrepairPath, QtCore.SIGNAL("clicked()"), self.browse_prepairpath)

    def browse_outfile(self):
        newname = QtGui.QFileDialog.getSaveFileName(self, "Output Shapefile", "", "Shapefile (*.shp)")
        if newname != "":
            self.filename.setText(newname)

    def browse_prepairpath(self):
        newname = QtGui.QFileDialog.getOpenFileName(self, "", "", "")
        if newname != "":
            self.prepairPath.setText(newname)
