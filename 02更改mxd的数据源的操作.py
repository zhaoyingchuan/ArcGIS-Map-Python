#coding=gbk
#�޸�����Դ
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\PythonTest\changeSource.mxd")
mxd.findAndReplaceWorkspacePaths(r"C:\PythonTest\data\Python.gdb",r"C:\PythonTest\changeSource.gdb","FILEGDB_WORKSPACE")
#���Ϊһ���µ�mxd
mxd.saveACopy(r"C:\PythonTest\changeSource2.mxd")
