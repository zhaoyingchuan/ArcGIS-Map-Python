#coding=utf-8
import arcpy
fc = r'C:\Data\result.shp'
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
for row in cursor:
    x,y = row[0]
    print "{0},{1}".format(x,y)