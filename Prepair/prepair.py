# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Prepair
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import qgis
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from prepairdialog import PrepairDialog
import os.path
import os
import subprocess


class Prepair:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'prepair_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = PrepairDialog()


    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/prepair/icon.png"),
            u"prepair", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&prepair", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&prepair", self.action)
        self.iface.removeToolBarIcon(self.action)

    def verifypath(self, path):
        dirname = os.path.dirname(path)
        return os.path.exists(dirname)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        
        #-- stuff for selecting the proper layer
        # print str(self.iface.mapCanvas().currentLayer().name())
        layers = self.iface.mapCanvas().layers()
        polyl = []
        self.dlg.comboLayers.clear()
        curlayer = 0
        alll = 0 #-- to keep track of all layers
        for l in layers:
            if (l.type() == 0) and (l.geometryType() == 2): # if vector && polygon 
                polyl.append((l.name(), alll))
                if (l == self.iface.mapCanvas().currentLayer()):
                    curlayer = len(polyl)-1
            alll += 1
        for l in polyl:
            self.dlg.comboLayers.addItem(l[0])
        self.dlg.comboLayers.setCurrentIndex(curlayer)


        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            mw = self.iface.mainWindow()
            path = self.dlg.filename.text()
            #-- get selected layer by the user
            # print "selected layer", polyl[self.dlg.comboLayers.currentIndex()]
            selectedLayer = self.iface.mapCanvas().layer(polyl[self.dlg.comboLayers.currentIndex()][1])
            #-- verify output path can be created
            if (self.verifypath(path) == False):
                QMessageBox.critical(mw, "prepair", "Non-valid output file.")
                return 1
            #-- verify that minarea is a number>=0
            try:
                minarea = float(self.dlg.minarea.text())
                if (minarea < 0.0):
                    QMessageBox.critical(mw, "prepair", "Minimum area must be a positive number")
                    return 1
            except:
                QMessageBox.critical(mw, "prepair", "Minimum area must be a positive number")
                return 1

            #-- repair paradigm
            if (self.dlg.onlySelected.isChecked() == True):
                # print "only selected"
                fs = selectedLayer.selectedFeatures()
            else:
                # print "all features"
                fs = selectedLayer.getFeatures()
            invalid = 0
            features = list(fs)
            writer = QgsVectorFileWriter(path, "CP1250", features[0].fields(), QGis.WKBPolygon, None, "ESRI Shapefile")
            if writer.hasError() != QgsVectorFileWriter.NoError:
                QMessageBox.critical(mw, "prepair", "Error when creating shapefile:")
                return 1
            for f in features:
                cmd = []
                cmd.append("prepair")
                cmd.append("--wkt")
                cmd.append(f.geometry().exportToWkt())
                if (self.dlg.radioOddEven.isChecked() == False):
                    cmd.append("--setdiff")
                if (minarea > 0.0):
                    cmd.append("--minarea")
                    cmd.append(str(minarea))
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
                wkt2 = p.stdout.read()
                p.terminate()
                geom2 = QgsGeometry.fromWkt(wkt2)
                if (geom2.isGeosEmpty() == False): #-- do not add to layer if repaired is emtpy
                    f.setGeometry(geom2)
                    writer.addFeature(f)
                else:
                    print "WARNING: empty geometry, feature", f.id(), "not added to new layer."
            del writer
            qgis.utils.iface.addVectorLayer(path, os.path.basename(path), "ogr")
