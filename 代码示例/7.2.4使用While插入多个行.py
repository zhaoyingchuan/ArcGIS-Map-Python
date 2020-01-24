import arcpy
fc = r'C:\Data\学校.shp'
cursor = arcpy.da.InsertCursor(fc,["Name"])
x = 1
while x <= 5:
	cursor.insertRow(["New Row"])
	x += 1