import arcpy
out_path = "C:\Data"
out_name = "line.shp"
prjfile = "C:\Data\streams.prj"
spatialref = arcpy.SpatialReference(prjfile)
arcpy.CreateFeatureclass_management(out_path,out_name,"POLYLINE","","","",spatialref)
