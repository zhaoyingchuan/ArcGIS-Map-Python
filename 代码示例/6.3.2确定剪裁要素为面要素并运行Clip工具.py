#coding=gbk
import arcpy
arcpy.env.workspace = r'C:\Data'
desc = arcpy.Describe(r'C:\Data\�ϲ���.shp')
type = desc.shapeType
print type
if type == "Polygon":
	arcpy.Clip_analysis(r'C:\Data\����.shp',r'C:\Data\�ϲ���.shp',"result7.shp")
else:
	print "The clip features are not polygons."