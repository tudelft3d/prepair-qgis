prepair-qgis
============

QGIS v2.x plugin for [prepair](https://github.com/tudelft-gist/prepair). The binary of prepair must be installed on your system---we offer [Windows 64bit binaries](https://github.com/tudelft-gist/prepair/releases), and makefile to easily compile binaries for Mac/Linux.

It permits you to automatically repair single polygons. Simply select one vector layer (containing polygons), and launch the plugin. You can then decide to repair only the selected polygons, or only those invalid. Using a valid polygon will mean that its geometry might be changed (e.g. the first point in a ring could be a different one).

A new layer with the input polygon is created (always a shape file). Each input polygon becomes a new object in the new layer, with its original attribute. If an invalid polygon, once repaired, is formed by 2+ polygons (e.g. if a bowtie polygon was the input, then 2 valid polygons are created), then only one geometry is created: a MultiPolygon.

Automated repair methods can be considered as interpreting ambiguous or ill-defined polygons and giving a coherent and clearly defined output. Examples of errors are: polygon has a dangling edge; polygon is not closed; polygon self-intersects; an inner ring of the polygon is located outside the outer ring; etc. We offer two repair paradigms:

  1. odd-even: an extension of the odd-even algorithm to handle GIS polygons containing inner rings and degeneracies; 
  2. setdiff: we follow a set difference rule for the rings.




