#coding=utf-8
import arcpy
fc = r'C:\Data\学校.shp'
cursor = arcpy.SearchCursor(fc,["Name"])
for row in cursor:
	print "Name = {0}".format(row)