#!/usr/bin/python

n1 = int(input("Input int "))
n2 = 0
while n1 > 0:
    digit = n1 % 10
    n1 = n1 / 10
    print (n1)
    n2 = n2 * 10
    n2 = n2 + digit
    print (n2) 
