import arcpy
fc = r'C:\Data\学校.shp'
cursor = arcpy.da.InsertCursor(fc,["Name"])
cursor.insertRow(["ABCD幼儿园"])