#coding=gbk
import arcpy
pdfpath = r'D:\Desktop\MapBook.pdf'
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.dataDrivePages.exportToPDF(r'D:\Desktop\MapBook.pdf')
pdfdoc.appendPages(r'D:\Desktop\Cover.pdf')
pdfdoc.appendPages(r'D:\Desktop\Maps.pdf')
del mapdoc