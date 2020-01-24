#coding=utf-8
import arcpy
dataset = r'D:\Documents\ArcGIS\江西.gdb\江西_localities_AdministrativeBoundary\南昌市'
spatialref = arcpy.Describe(dataset).spatialReference
mapdoc = arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mapdoc):
    df.spatialReference = spatialref
    df.scale = 200000
del mapdoc