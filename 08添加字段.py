#coding=gbk
import arcpy
from arcpy import env
env.workspace = r'D:\Documents\ArcGIS\˫����.gdb'
arcpy.AddField_management("slope_Reclass", "����", "SHORT", 9)