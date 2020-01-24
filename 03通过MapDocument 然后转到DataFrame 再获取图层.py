#coding=gbk
#通过MapDocument获取dataframe，从而获取每一个图层
import arcpy
mxd = arcpy.mapping.MapDocument(r"D:\Desktop\南昌市健康资源分析\六段服务区1.mxd")
dflist = arcpy.mapping.ListDataFrames(mxd)
for df in dflist:
    inLayer=arcpy.mapping.ListLayers(mxd, "", df)
    for layer in inLayer:
    #打印图层名称
        print layer.name