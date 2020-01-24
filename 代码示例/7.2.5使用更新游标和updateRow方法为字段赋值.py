import arcpy
fc = r'C:\Data\学校.shp'
cursor = arcpy.da.UpdateCursor(fc,["Name","Telephone"])
for row in cursor:
    row[1] = row[0]
    cursor.updateRow(row)