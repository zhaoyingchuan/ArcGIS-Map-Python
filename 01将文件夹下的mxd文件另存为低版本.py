#coding=gbk
import glob
import os
import arcpy
for filename in glob.glob(r'D:\Desktop\双评价资料数据\*.mxd'):
    fname = os.path.basename(filename)
    mxd = arcpy.mapping.MapDocument(filename)
    fpath = r'D:\Desktop\\'+fname
    mxd.saveACopy(fpath,"10.0")