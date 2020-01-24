#coding=utf-8
import arcpy
infc = r'C:\Data\学校.shp'
fieldname = "Category"
outfc = r'C:\Data\学校_select2.shp'
delimfield = arcpy.AddFieldDelimiters(infc,fieldname)
arcpy.Select_analysis(infc,outfc,delimfield + " = '科教文化服务;学校'")