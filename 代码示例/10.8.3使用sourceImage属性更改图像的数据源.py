#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
elemlist = arcpy.mapping.ListLayoutElements(mapdoc,"PICTURE_ELEMENT")
for elem in elemlist:
    if elem.name == "公共康体保健资源密度图.png":
        elem.sourceImage = r'D:\Desktop\南昌市健康资源分析\核密度分析图\公共医疗保健资源密度图.png'
mapdoc.save()
del mapdoc