#coding=gbk
import arcpy
fieldlist = arcpy.ListFields(r'C:\Data\市域.shp')
for field in fieldlist:
	print "{0} is a type of {1} with a length of {2}".format(field.name,field.type,field.length)