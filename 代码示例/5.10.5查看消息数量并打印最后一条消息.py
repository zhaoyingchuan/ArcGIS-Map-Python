#coding=gbk
import arcpy
result=arcpy.GetCount_management(r'C:\Data\�ߵ�_�ϲ���_ѧУ.shp')
print result
count=result.messageCount
print result.getMessage(count-1)