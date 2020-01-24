#coding=gbk
#修改数据源
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\PythonTest\changeSource.mxd")
mxd.findAndReplaceWorkspacePaths(r"C:\PythonTest\data\Python.gdb",r"C:\PythonTest\changeSource.gdb","FILEGDB_WORKSPACE")
#另存为一个新的mxd
mxd.saveACopy(r"C:\PythonTest\changeSource2.mxd")
