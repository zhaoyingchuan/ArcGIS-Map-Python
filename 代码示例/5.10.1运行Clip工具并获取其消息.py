#coding=gbk
import arcpy
arcpy.env.workspace = "C:/Data"
infc = "����.shp"
clipfc = "�ϲ���.shp"
outfc = "result4.shp"
arcpy.Clip_analysis(infc,clipfc,outfc)
print arcpy.GetMessages()