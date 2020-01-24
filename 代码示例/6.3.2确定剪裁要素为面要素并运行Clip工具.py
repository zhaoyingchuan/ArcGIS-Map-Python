#coding=gbk
import arcpy
arcpy.env.workspace = r'C:\Data'
desc = arcpy.Describe(r'C:\Data\南昌市.shp')
type = desc.shapeType
print type
if type == "Polygon":
	arcpy.Clip_analysis(r'C:\Data\火车线.shp',r'C:\Data\南昌市.shp',"result7.shp")
else:
	print "The clip features are not polygons."