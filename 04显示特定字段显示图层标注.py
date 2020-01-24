#coding=gbk
import arcpy
mxd = arcpy.mapping.MapDocument(r"D:\Desktop\双评价.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]
#对第一个图层进行修改
lyr = arcpy.mapping.ListLayers(mxd, "", df)[0]
lyr.showLabels = True
lyr.labelClasses[0].expression  = '[CITY_NAME] +"_"+[CNTRY_NAME]'
#保存结果
mxd.save()