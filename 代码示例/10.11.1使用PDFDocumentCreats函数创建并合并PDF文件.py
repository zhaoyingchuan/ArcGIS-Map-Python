#coding=utf-8
import arcpy
pdfpath = r'D:\Desktop\mypdf.pdf'
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
pdfdoc.appendPages(r'D:\Desktop\002北京中外建江西简介及项目业绩20190110.pdf')
pdfdoc.appendPages(r'D:\Desktop\2018注册规划师资格证书.pdf')
pdfdoc.saveAndClose()
del pdfdoc