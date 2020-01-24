#coding=gbk
import arcpy
fc = r'D:\Desktop\南昌市健康资源分析\设施点及原始数据.gdb\公共康体保健'
desc = arcpy.Describe(fc)
print desc.dataType


