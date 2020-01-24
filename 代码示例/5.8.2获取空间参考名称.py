import arcpy
prjfile = "C:\Data\streams.prj"
spatialref = arcpy.SpatialReference(prjfile)
print spatialref.name