#coding=gbk
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\PythonTest\change.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]
lyr = arcpy.mapping.ListLayers(mxd,"",df)[1]
if lyr.symbologyType == "UNIQUE_VALUES":
  lyr.symbology.valueField = "Dis"
  lyr.symbology.addAllValues()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.save()
del mxd
