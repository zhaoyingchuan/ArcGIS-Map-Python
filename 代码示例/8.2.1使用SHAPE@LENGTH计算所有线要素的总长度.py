#coding=utf-8
import arcpy
fc = r'C:\Data\result.shp'
cursor = arcpy.da.SearchCursor(fc,["SHAPE@LENGTH"])
length = 0
for row in cursor:
    length += row[0]
print length