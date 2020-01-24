#coding=utf-8
import arcpy
arcpy.env.workspace = r'C:\Data'
fc = r'C:\Data\result.shp'
fullname = arcpy.ParseTableName(fc)
namelist = fullname.split()
databasename = namelist[0]
ownername = namelist[1]
fcname = namelist[2]
print databasename
print ownername
print fcname