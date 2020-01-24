#coding=gbk
import arcpy
mydoc = arcpy.mapping.MapDocument(r'D:\Desktop\双评价资料数据\双评价.mxd')
lyrlist = arcpy.mapping.ListLayers(mydoc)
for lyr in lyrlist:
    print lyr.name