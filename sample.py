#coding=utf-8
import arcpy

aprx  = arcpy.mp.ArcGISProject(r"D:\Desktop\shiyan.mxd")
m = arcpy.mp.ListDataFrames(mxd)[0]
lyr = arcpy.mp.ListLayers(mxd, "", df)[0]
lyr.definitionQuery = '"序号" = ' + "'1'"
df.extent = lyr.getSelectedExtent()
arcpy.RefreshActiveView()
