#coding=utf-8
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
title = arcpy.mapping.ListLayoutElements(mapdoc,"TEXT_ELEMENT")[0]
title.text = "新的标题"
mapdoc.save()
del mapdoc