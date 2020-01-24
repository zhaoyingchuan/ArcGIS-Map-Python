#coding=gbk
import arcpy
arcpy.env.workspace=r'C:\Data'
fcs=arcpy.ListFeatureClasses()
fcs.sort()
for fc in fcs:
    print fc
fcs.sort(reverse=True)
for fc in fcs:
    print fc