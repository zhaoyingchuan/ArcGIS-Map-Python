#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
    print df.name
del mapdoc
