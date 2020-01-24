import arcpy
arcpy.env.workspace = r'C:\Data'
tifflist = arcpy.ListRasters("","TIF")
for tiff in tifflist:
	arcpy.BuildPyramids_management(tiff)