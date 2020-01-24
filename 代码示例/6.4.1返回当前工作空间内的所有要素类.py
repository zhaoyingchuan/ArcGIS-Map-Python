#coding=gbk
import arcpy
from arcpy import env
env.workspace = r'C:\Data'
fclist = arcpy.ListFeatureClasses()
for i in fclist:
    print i
