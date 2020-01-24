#coding=gbk
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Project\Project.mxd")
for elm in arcpy.mapping.ListLayoutElements(mxd,"PICTURE_ELEMENT", "*logo*"):
    if elm.name == "CityLogo":
        elm.sourceImage = r"C:\Project\Data\Photo.bmp"
mxd.saveACopy(r"C:\Project\Project2.mxd")
del mxd
