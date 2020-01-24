#coding=utf-8
mapdoc = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mapdoc)[0]
lyr1 = arcpy.mapping.Layer(r'D:\Desktop\南昌市健康资源分析\固定时段服务区面.gdb\公共康体保健\各类球类场所步行15分钟')
lyr2 = arcpy.mapping.Layer(r'D:\Desktop\南昌市健康资源分析\固定时段服务区面.gdb\公共康体保健\公园步行15分钟')
legend = arcpy.mapping.ListLayoutElements(mapdoc,"LEGEND_ELEMENT")[0]
legend.autoAdd = True
arcpy.mapping.AddLayer(df,lyr1,"BOTTOM")
legend.autoAdd = False
arcpy.mapping.AddLayer(df,lyr2,"BOTTOM")
mapdoc.save()
del mapdoc