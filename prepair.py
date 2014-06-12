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
from qgis.gui import QgsMessageBar
from PyQt4.QtGui import QProgressBar
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from prepairdialog import PrepairDialog
import os.path
import os
import subprocess

MAXSIZE = 10000



class Prepair:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'prepair_{}.qm'.format(locale))

        self.process = QProcess(iface)
        self.tmpwkt = os.path.join(self.plugin_dir,'tmp.wkt')
        # self.progressbar = self.iface.messageBar().createMessage("prepair progress")

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
            u"prepair", self.iface.vectorMenu())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToVectorMenu(u"&prepair", self.action)
        # Help menu
        self.helpAction = QAction("help", self.iface.mainWindow())
        self.helpAction.triggered.connect(self.help)
        self.iface.addPluginToVectorMenu(u"&prepair", self.helpAction)

        self.dlg.prepairPath.setText(QSettings().value("prepair/prepairpath"))
        self.dlg.filename.setText(QSettings().value("prepair/lastfilename"))

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginVectorMenu(u"&prepair", self.action)
        self.iface.removePluginVectorMenu(u"&prepair", self.helpAction)
        self.iface.removeToolBarIcon(self.action)

    def verifypath(self, path):
        dirname = os.path.dirname(path)
        return os.path.exists(dirname)

    def help(self):
        QDesktopServices().openUrl(QUrl("https://github.com/tudelft-gist/prepair-qgis/blob/master/README.md"))

    def run(self):
        self.dlg.show()
        #-- stuff for selecting the proper layer
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
            if (self.dlg.comboLayers.currentIndex() == -1):
                QMessageBox.critical(mw, "prepair", "No layer selected.")
                return 1
            #-- verify output path can be created
            if (self.verifypath(path) == False):
                QMessageBox.critical(mw, "prepair", "Non-valid output file.")
                return 1
            #-- verify that minarea is a number>=0
            try:
                minarea = float(self.dlg.minarea.text())
                if (minarea < 0.0):
                    # QMessageBox.critical(mw, "prepair", "Minimum area must be a positive number")
                    self.iface.messageBar().pushMessage("prepair", \
                      "Minimum area must be a positive number", level=QgsMessageBar.CRITICAL)
                    return 1
            except:
                self.iface.messageBar().pushMessage("prepair", \
                  "Minimum area must be a positive number", level=QgsMessageBar.CRITICAL)
                return 1
            #-- repair paradigm
            selectedLayer = self.iface.mapCanvas().layer(polyl[self.dlg.comboLayers.currentIndex()][1])
            if (self.dlg.onlySelected.isChecked() == True):
                fs = selectedLayer.selectedFeatures()
            else:
                fs = selectedLayer.getFeatures()
            #-- repair only invalid polygons?
            bOnlyInvalid = False
            if (self.dlg.onlyInvalid.isChecked() == True):
                bOnlyInvalid = True
            invalid = 0
            features = list(fs)
            #-- if no features then stop this
            if len(features) == 0:
                QMessageBox.critical(mw, "prepair", "No features selected.")
                return 1
            writer = QgsVectorFileWriter(path, "CP1250", features[0].fields(), QGis.WKBPolygon, None, "ESRI Shapefile")
            if writer.hasError() != QgsVectorFileWriter.NoError:
                # QMessageBox.critical(mw, "prepair", "Error when creating shapefile:")
                self.iface.messageBar().pushMessage("prepair", "error when creating the shapefile", level=QgsMessageBar.CRITICAL)
                return 1
            cmd = []
            if (self.dlg.radioOddEven.isChecked() == False):
                cmd.append("--setdiff")
            if (minarea > 0.0):
                cmd.append("--minarea")
                cmd.append(str(minarea))
            cmd.append("--wkt")
            cmd.append("nothing")
            
            exe = self.dlg.prepairPath.text()
            if (exe == ''):
                QMessageBox.critical(mw, "prepair", "The path for the prepair executable must be set.")
                return 1
            QSettings().setValue("prepair/prepairpath", exe)
            QSettings().setValue("prepair/lastfilename", path)

            #-- setup a progressbar
            progressbar = self.iface.messageBar().createMessage("prepair progress")
            progress = QProgressBar()
            progress.setMaximum(100)
            progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            progressbar.layout().addWidget(progress)
            self.iface.messageBar().pushWidget(progressbar, self.iface.messageBar().INFO)

            totalfs = len(features)
            for i,f in enumerate(features):
                print "Feature #", int(f.id())
                progress.setValue(i/float(totalfs)*100)
                # self.iface.mainWindow().statusBar().showMessage("prepair: processed {} %".format(int(i/float(totalfs)*100)))
                # self.iface.messageBar().pushMessage("prepair", "processed {} %".format(int(i/float(totalfs)*100)), duration=2)
                # self.iface.mainWindow().statusBar().showMessage("roger moquin")
                err = list(f.geometry().validateGeometry())
                if ( (bOnlyInvalid == True) and (len(err) == 0) ):
                    continue

                if (f.geometry().wkbSize() > MAXSIZE):
                    print "*** large polygon"
                    tmpf = open(self.tmpwkt, 'w')
                    tmpf.write(f.geometry().exportToWkt())
                    tmpf.close()
                    cmd[-2] = '-f'
                    cmd[-1] = self.tmpwkt
                else:
                    cmd[-2] = '--wkt'
                    cmd[-1] = f.geometry().exportToWkt()
                self.process.start(exe, cmd)
                self.process.waitForFinished()
                t = str(self.process.readAllStandardOutput())
                if t == "":
                    self.iface.messageBar().pushMessage("prepair", "Problem feature #%d, not repaired." % (f.id()), level=QgsMessageBar.WARNING)
                    continue
                wkt2 = t.splitlines()[0]
                geom2 = QgsGeometry.fromWkt(wkt2)
                if (geom2 != None) and (geom2.isGeosEmpty() == False): #-- do not add to layer if repaired is emtpy
                    f.setGeometry(geom2)
                    writer.addFeature(f)
                else:
                    # print "WARNING: empty geometry, feature", f.id(), "not added to new layer."
                    self.iface.messageBar().pushMessage("prepair", "repaired feature #%d has an empty geometry, skipping." % (f.id()),\
                      level=QgsMessageBar.WARNING)
                self.process.kill()
            del writer
            if (os.path.exists(self.tmpwkt)):
                os.remove(self.tmpwkt)
            self.iface.messageBar().clearWidgets()
            self.iface.messageBar().pushMessage("prepair", "Features repaired.", \
              level=QgsMessageBar.INFO, duration=5)
            qgis.utils.iface.addVectorLayer(path, os.path.basename(path), "ogr")
