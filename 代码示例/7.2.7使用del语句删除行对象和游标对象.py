import arcpy
fc = r'C:\Data\学校.shp'
cursor = arcpy.da.UpdateCursor(fc,["Name"])
for row in cursor:
    if row[0] == u'流湖第二小学':
        cursor.deleteRow()
del row
del cursor