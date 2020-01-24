#coding=gbk
import arcpy
from arcpy import env
env.workspace = r'D:\Documents\ArcGIS\双评价.gdb'
arcpy.AddField_management("slope_Reclass", "日文", "SHORT", 9)