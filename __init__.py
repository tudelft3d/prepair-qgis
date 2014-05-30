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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Prepair class from file Prepair
    from prepair import Prepair
    return Prepair(iface)
