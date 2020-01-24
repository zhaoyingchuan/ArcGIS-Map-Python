#coding=gbk
import arcpy
mapdoc = arcpy.mapping.MapDocument(r'D:\Desktop\双评价资料数据\双评价.mxd')
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name + ":" + elem.type
del mapdoc