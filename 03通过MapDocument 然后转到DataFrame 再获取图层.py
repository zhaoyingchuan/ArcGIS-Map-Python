#coding=gbk
#ͨ��MapDocument��ȡdataframe���Ӷ���ȡÿһ��ͼ��
import arcpy
mxd = arcpy.mapping.MapDocument(r"D:\Desktop\�ϲ��н�����Դ����\���η�����1.mxd")
dflist = arcpy.mapping.ListDataFrames(mxd)
for df in dflist:
    inLayer=arcpy.mapping.ListLayers(mxd, "", df)
    for layer in inLayer:
    #��ӡͼ������
        print layer.name