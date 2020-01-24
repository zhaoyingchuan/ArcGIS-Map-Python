#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.findAndReplaceWorkspacePaths("C:/mydata","C:/newdata")
mapdoc.save()
del mapdoc