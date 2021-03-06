#coding=utf-8
import arcpy
arcpy.env.workspace = r'C:\Data'
fc = r'C:\Data\result.shp'
cursor = arcpy.da.SearchCursor(fc,["OID@","SHAPE@"])
for row in cursor:
    print "Feature {0}:".format(row[0])
    partnum = 0
    for part in row[1]:
        print "Part {0}".format(partnum)
        for point in part:
            if point:
                print "{0},{1}".format(point.X,point.Y)
            else:
                print "Interior Ring"
        partnum += 1