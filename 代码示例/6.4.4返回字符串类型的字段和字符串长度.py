#coding=gbk
import arcpy
fieldslist = arcpy.ListFields(r'C:\Data\ѧУ.shp'.decode('gbk'))
for field in fieldslist:
    print field.name + ":" + str(field.length)
    

