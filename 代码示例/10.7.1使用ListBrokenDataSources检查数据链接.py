#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
brokenlist = arcpy.mapping.ListBrokenDataSources(mapdoc)
for lyr in brokenlist:
    print lyr.name
del mapdoc