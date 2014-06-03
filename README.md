# QGIS plugin for prepair


QGIS plugin for [prepair](https://github.com/tudelft-gist/prepair). 
It permits you to *automatically* repair single polygons. Simply select one vector layer (containing polygons), and launch the plugin. You can then decide to repair only the selected polygons, or only those invalid (with perform validation with GEOS). Repairing a valid polygon will mean that its geometry might be changed (e.g. the first point in a ring could be a different one).

The output of prepair is new layer (always a shapefile at this moment). Each input polygon becomes a new object in the new layer, with its original attributes. If an invalid polygon, once repaired, is composed of 2+ polygons (e.g. if a bowtie polygon was the input, then 2 valid polygons are created), then only one geometry is created: a MultiPolygon.

Automated repair methods can be considered as interpreting ambiguous or ill-defined polygons and giving a coherent and clearly defined output. Examples of errors are: polygon has a dangling edge; polygon is not closed; polygon self-intersects; an inner ring of the polygon is located outside the outer ring; etc. We offer two repair paradigms:

  1. odd-even: an extension of the odd-even algorithm to handle GIS polygons containing inner rings and degeneracies; 
  2. setdiff: we follow a set difference rule for the rings.


## How to install it?

Use directly the QGIS repository from within QGIS (menu "Plugins/Manage and Install Plugins"). The name of the plugin is "prepair", the details of the plugin are available [there](http://plugins.qgis.org/plugins/prepair/).

To run it, you must also have the binary of prepair installed on your system.

__Windows__: download the [Windows 64bit binary](https://github.com/tudelft-gist/prepair/releases/download/v0.7/prepair_win64.zip) and unzip to any location (eg creating the folder 'C:\prepair_win64\'). The first time the plugin is used, select 'C:\prepair_win64\prepair.exe' for the 'prepair executable path' at the bottom of the windows. 

__Mac/Linux__: use the makefile to easily compile the code under Mac and Linux. (binaries for Mac coming soon)




