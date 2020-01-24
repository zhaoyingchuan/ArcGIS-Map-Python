#coding=utf-8
import arcpy
fc = r'C:\Data\result.shp'
fieldname = arcpy.ValidateFieldName("新字段")
arcpy.AddField_management(fc,fieldname,"text","","",12)