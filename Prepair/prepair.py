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
        print "exists?", os.path.exists(dirname)


    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            mw = self.iface.mainWindow()
            path = self.dlg.filename.text()
            if (self.verifypath(path) == False):
                QMessageBox.information(mw, "prepair", "Non-valid output file.")
            else:
                if (self.dlg.onlySelected.isChecked() == True):
                    print "only selected"
                    fs = self.iface.mapCanvas().currentLayer().selectedFeatures()
                else:
                    print "all features"
                    fs = self.iface.mapCanvas().currentLayer().getFeatures()
                invalid = 0
                # print str(self.iface.mapCanvas().currentLayer().displayField())
                ls = list(fs)
                # print path, ls[0].fields
                writer = QgsVectorFileWriter(path, "CP1250", ls[0].fields(), QGis.WKBPolygon, None, "ESRI Shapefile")
                if writer.hasError() != QgsVectorFileWriter.NoError:
                    print "Error when creating shapefile: ", writer.hasError()
                for f in ls:
                    if (f.geometry().isGeosValid() == True):
                        writer.addFeature(f)
                    else:
                        invalid += 1
                        wkt = f.geometry().exportToWkt()
                        # print wkt
                        if (self.dlg.radioOddEven.isChecked() == True):
                            print "oddeven repair"
                            cmd = []
                            cmd.append("/Users/hugo/projects/prepair-github/prepair")
                            cmd.append("--wkt")
                            # cmd.append('POLYGON((0 0, 0 10, 10 0, 10 10, 0 0))')
                            cmd.append(wkt)
                            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
                            # p.wait()
                            wkt2 = p.stdout.read()
                            p.terminate()
                            newgeom = QgsGeometry.fromWkt(wkt2)
                            print "multi:", newgeom.isMultipart()
                            f.setGeometry(newgeom)
                            writer.addFeature(f)
                            # lsArgs = ['--wkt']
                            # lsArgs.append(wkt)
                            # lsArgs.append('POLYGON((0 0, 0 10, 10 0, 10 10, 0 0))')
                            # print lsArgs
                            # self.process.start('/Users/hugo/projects/prepair/prepair-github/prepair', lsArgs, QIODevice.ReadOnly)
                            # msg = str(self.process.readAllStandardError())
                            # print "msg:", msg
                            # if msg == '':
                                # msg = str(self.process.readAllStandardOutput())
                                # outMessages = str(self.process.readAllStandardOutput()).splitlines()
                                # print outMessages
                            # self.process.kill()
                        else:
                            print "setdiff repair"
                print "no invalid polygons:", invalid
                del writer
                qgis.utils.iface.addVectorLayer(path, os.path.basename(path), "ogr")
