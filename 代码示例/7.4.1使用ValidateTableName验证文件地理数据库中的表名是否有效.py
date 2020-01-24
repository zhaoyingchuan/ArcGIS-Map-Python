#coding=utf-8
import arcpy
tablename = arcpy.ValidateTableName("高德_南昌市",r'D:\Documents\ArcGIS\江西.gdb')
print tablename