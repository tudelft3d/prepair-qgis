# QGIS plugin for prepair

QGIS plugin for [prepair](https://github.com/tudelft-gist/prepair). It permits you to *automatically* repair single polygons. Simply select one vector layer (containing polygons), and launch the plugin. You can then decide to repair only the selected polygons, or only those that are invalid (as validated by GEOS). Repairing a valid polygon will mean that its geometry might be changed (e.g. the first point in a ring could be a different one).

The output of prepair is a new layer (always a shapefile at this moment). Each input polygon becomes a new MultiPolygon object in the new layer, with its original attributes.

Automated repair methods can be considered as interpreting ambiguous or ill-defined polygons and giving a coherent and clearly defined output. Examples of errors are: polygon has a dangling edge; polygon is not closed; polygon self-intersects; an inner ring of the polygon is located outside the outer ring; etc. We offer two repair paradigms:

  1. odd-even: an extension of the odd-even algorithm to handle GIS polygons containing inner rings and degeneracies; 
  2. setdiff: we follow a point set difference rule for the rings (outer \ inner).


## How to install it?

Install it directly from the QGIS repository within QGIS (menu "Plugins/Manage and Install Plugins"). The name of the plugin is "prepair", the details of the plugin are available [here](http://plugins.qgis.org/plugins/prepair/).

To run it, you must also have the binary of prepair installed on your system.

__Windows/Mac binaries__: download the 64-bit [Windows](https://github.com/tudelft-gist/prepair/releases/download/v0.7/prepair_win64.zip) or [Mac](https://github.com/tudelft-gist/prepair/releases/download/v0.7/prepair_mac.zip) binaries and unzip to any location (eg creating the folder 'C:\prepair_win64\'). The first time the plugin is used, select 'C:\prepair_win64\prepair.exe' for the 'prepair executable path' at the bottom of the prepair plugin window. The Mac binaries require Kyngchaos' [GDAL 1.11 Complete Framework](http://www.kyngchaos.com/software/frameworks#gdal_complete).

__From source__: installing from source is easy under Mac and Linux using the included CMake file.