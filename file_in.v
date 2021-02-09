#!/usr/bin/python

fo =open("aa.txt", "w+")
fo.write("The biggest town of Armenia? /Erevan\n")
fo.write("The capital of Russia? /Moscow\n")
fo.close()

fo = open("aa.txt", "r+")
str = fo.read()
position = fo.tell()
print position
print str

pos = fo.seek(0,1)
str1 = fo.read(20)
print str1
print(fo.readline())

print(fo.read())
