#coding=gbk
import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mxd)
for df in dflist:
    for lyr in arcpy.mapping.ListLayers(mxd, u"各类球类场所", df):
        if arcpy.Describe(lyr).shapeType == "Polygon":
            lyr.visible = True
            lyr.transparency = 50
mxd.save()
del mxd