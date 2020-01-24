import arcpy
arcpy.env.workspace = r'C:\Data'
fcs = arcpy.ListFeatureClasses()
print len(fcs)


