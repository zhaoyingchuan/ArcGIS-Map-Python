import arcpy
fc = r'C:\Data\学校.shp'
cursor = arcpy.da.SearchCursor(fc,["Name"])
for row in cursor:
	print "Name = {0}".format(row)