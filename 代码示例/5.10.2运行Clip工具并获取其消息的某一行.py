#coding=gbk
import arcpy
arcpy.env.workspace = "C:\Data"
infc = "����.shp"
clipfc = "�ϲ���.shp"
outfc = "result3.shp"
arcpy.Clip_analysis(infc,clipfc,outfc)
print arcpy.GetMessage(0)