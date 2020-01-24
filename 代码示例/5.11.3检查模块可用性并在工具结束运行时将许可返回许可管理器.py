import arcpy
from arcpy import env
env.workspace = "C:/Data"
if arcpy.CheckExtension("3D") == "Available":
	arcpy.CheckOutExtension("3D")
	arcpy.Slope_3d("Yudu_DEM.img","Slope","DEGREES")
	arcpy.CheckInExtension("3D")
else:
	print "3D Analyst license is unavailable."