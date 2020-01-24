#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
lyrlist = arcpy.mapping.ListLayers(mapdoc)
for lyr in lyrlist:
    if lyr.supports("DATASOURCE"):
        if lyr.dataSource == r'C:\Data\result.shp':
            lyr.findAndReplaceWorkspacePath("database.gdb","newdata.gdb")
mapdoc.save()
del mapdoc