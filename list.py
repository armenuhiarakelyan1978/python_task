#!/usr/bin/python

list2 = [1,4,7,8,9,4,8,5]
list1 = [1,4,7,9]
list3 = []
def list_el_un(list2):
    for  i in list2:
        for j in range(i+1,len(list2)):
            if list2[i] == list2[j]:
                 print("the elements of list are repeated")
print (list_el_un(list1))
print (list_el_un(list2))

setarr = set(list2)
if len(list2) == len(setarr):
    print ("All elements are unic")
else:
    print ("the elements are repeated")
print (list2)
print (setarr)
print (list1)
print (setarr)

