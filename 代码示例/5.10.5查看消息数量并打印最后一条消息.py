#coding=gbk
import arcpy
result=arcpy.GetCount_management(r'C:\Data\高德_南昌市_学校.shp')
print result
count=result.messageCount
print result.getMessage(count-1)