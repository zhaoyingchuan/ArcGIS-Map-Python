#coding=gbk
import arcpy
fc = r'C:\Data\火车线.shp'
desc = arcpy.Describe(fc)
sc = desc.spatialReference
print "Dataset type:" + desc.dataType
print "Spatial reference:" + sc.name
