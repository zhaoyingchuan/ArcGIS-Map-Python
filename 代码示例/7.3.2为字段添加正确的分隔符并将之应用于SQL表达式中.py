import arcpy
fc = r'C:\Data\学校.shp'
fieldname = "Category"
delimfield = arcpy.AddFieldDelimiters(fc,fieldname)
cursor = arcpy.da.SearchCursor(fc,["Name","Adress"],delimfield + " = '科教文化服务;学校;中学'")
for row in cursor:
	print row[0]
del row
del cursor