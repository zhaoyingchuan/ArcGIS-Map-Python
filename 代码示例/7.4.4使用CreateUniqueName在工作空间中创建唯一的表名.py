#coding=utf-8
import arcpy
arcpy.env.workspace = r'C:\Data'
unique_name = arcpy.CreateUniqueName("buffer.shp")
arcpy.Buffer_analysis(r'C:\Data\南昌市.shp',unique_name,"10 KILOMETER")