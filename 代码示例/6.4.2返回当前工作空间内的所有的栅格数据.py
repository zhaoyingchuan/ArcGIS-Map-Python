import arcpy
arcpy.env.workspace = r'C:\Data'
rasterslist = arcpy.ListRasters()
print rasterslist
