#coding=gbk
import arcpy
arcpy.env.workspace = r'C:\Data'
fc = r'C:\Data\ѧУ.shp'
prjfile = r'C:\Data\WGS 1984 Complex UTM Zone 20N.prj'
spatialref = arcpy.SpatialReference(prjfile)
cursor = arcpy.da.SearchCursor(fc,["SHAPE@"],spatialref)
output = open("result.txt","w")
for row in cursor:
    point = row[0]
    output.write(str(point.X)) + " " + str(point.Y) + "\n"
output.close()