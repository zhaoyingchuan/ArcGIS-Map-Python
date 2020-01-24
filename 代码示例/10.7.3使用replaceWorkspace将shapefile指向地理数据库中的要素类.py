#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
mapdoc.replaceWorkspaces("C:/mydata/shape","SHAPE_WORKSPACE","C:/mydata/database.gdb","FILEGDB_WORKSPACE")
mapdoc.save()
del mapdoc