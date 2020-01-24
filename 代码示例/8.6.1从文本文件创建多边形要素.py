#coding=utf-8
import arcpy
arcpy.env.workspace = r'C:\Data'
infile = r'C:\Data\point.txt'
fc = "newpoly.shp"
arcpy.CreateFeatureclass_management(r'C:\Data',fc,"Polylgon")
cursor = arcpy.da.InsertCursor(fc,["SHAPE@"])
array = arcpy.Array()
point = arcpy.Point()
for line in fileinput.input(infile):
    point.ID, point.X, point.Y = line.split()
    line_array.add(point)
    polygon = arcpy.Polygon(array)
    cursor.insertRow([polygon])
    fileinput.close()
    del cursor