#coding=gbk
import arcpy
arcpy.env.workspace = "C:\Data"
infc = "火车线.shp"
clipfc = "南昌市.shp"
outfc = "result3.shp"
arcpy.Clip_analysis(infc,clipfc,outfc)
print arcpy.GetMessage(0)