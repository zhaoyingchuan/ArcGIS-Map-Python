#coding=gbk
import arcpy
mapdoc = arcpy.mapping.MapDocument(r'D:\Desktop\˫������������\˫����.mxd')
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name + ":" + elem.type
del mapdoc