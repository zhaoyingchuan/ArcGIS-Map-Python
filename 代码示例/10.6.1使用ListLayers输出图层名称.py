#coding=gbk
import arcpy
mydoc = arcpy.mapping.MapDocument(r'D:\Desktop\˫������������\˫����.mxd')
lyrlist = arcpy.mapping.ListLayers(mydoc)
for lyr in lyrlist:
    print lyr.name