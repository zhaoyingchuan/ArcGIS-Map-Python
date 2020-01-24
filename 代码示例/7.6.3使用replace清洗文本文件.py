#coding=utf-8
input = open(r'C:\Data\test.txt')
output = open(r'C:\Data\test1.txt',"w")
for line in input:
    str = line.replace("ID: ","")
    str = str.replace(", Latitude:","")
    str = str.replace(", Longitude:","")
    output.write(str)
input.close()
output.close()