#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument(r'D:\Desktop\mxd.mxd')
arcpy.mapping.ExportToJPEG(mapdoc,r'D:\Desktop\final.jpg',"","","",300)
del mapdoc