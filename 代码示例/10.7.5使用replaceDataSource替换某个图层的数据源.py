#coding=utf-8
import arcpy
mapdoc=arcpy.mapping.MapDocument(u"D:\Desktop\南昌市健康资源分析\六段服务区2.mxd")
df=arcpy.mapping.ListDataFrames(mapdoc,u"专科医院")[0] #找到第一个名称为“专科医院”的数据框
lyr=arcpy.mapping.ListLayers(mapdoc,u"卫生室",df)[0] #找到数据框中第一个名称为“卫生室”的图层
lyr.replaceDataSource(r'D:\Desktop\南昌市健康资源分析\设施点及原始数据.gdb',"FILEGDB_WORKSPACE",u"专科医院") #将“卫生室”图层的数据源设置为D:\Desktop\南昌市健康资源分析\设施点及原始数据.gdb下名称为“专科医院”的数据