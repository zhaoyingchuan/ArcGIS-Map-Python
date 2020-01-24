import arcpy
import os
arcpy.env.workspace = r'C:\Data'
outworkspace = r'D:\Documents\ArcGIS\Default.gdb'
fclist = arcpy.ListFeatureClasses()
for shapefile in fclist:
    fcname = arcpy.Describe(shapefile).basename
    newfcname = arcpy.ValidateTableName(fcname)
    outfc = os.path.join(outworkspace,newfcname)
    arcpy.CopyFeatures_management(shapefile,outfc)
