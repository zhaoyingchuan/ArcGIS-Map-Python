#coding=gbk
import arcpy
mxd = arcpy.mapping.MapDocument(r"D:\Desktop\˫����.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]
#�Ե�һ��ͼ������޸�
lyr = arcpy.mapping.ListLayers(mxd, "", df)[0]
lyr.showLabels = True
lyr.labelClasses[0].expression  = '[CITY_NAME] +"_"+[CNTRY_NAME]'
#������
mxd.save()