#coding=gbk
import arcpy
fieldlist = arcpy.ListFields(r'C:\Data\ѧУ.shp'.decode('gbk'))
for field in fieldlist:
    print field.name