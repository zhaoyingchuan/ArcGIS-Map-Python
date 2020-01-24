#coding=utf-8
import arcpy
arcpy.env.workspace = r'C:\Data'
coordlist = [[17.0,20.0],[125.0,32.0],[4.0,87.0]]
pointlist = []
for x,y in coordlist:
    point = arcpy.Point(x,y)
    pointgeometry = arcpy.PointGeometry(point)
    pointlist.append(pointgeometry)
arcpy.Buffer_analysis(pointlist,"buffer1.shp","10 METERS")