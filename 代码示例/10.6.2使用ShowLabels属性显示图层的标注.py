#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc,"",dflist[0])
for lyr in lyrlist:
    lyr.showLabels = True
del lyrlist