#coding=utf-8
import arcpy
fc = r'C:\Data\result.shp'
geolist = arcpy.CopyFeatures_management(fc,arcpy.Geometry())
length = 0
for geometry in geolist:
    length += geometry.length
print "Total length:" + str(length)