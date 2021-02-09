#!/usr/bin/python
fo = open("aa.txt", "r+")
ll=[]
count = len(open("aa.txt").readlines())
for line in fo:
    for word in line.split():
	ll.append(word)
    m=ll.index("?")
    str=""
    for i in ll[:m+1]:
        str += i
        str = str + " "    
    print str
    print "Please answer the question enter char by char------"
    print ll[m+1]
    n=[ch for ch in ll[m+1]]
    print (n)
word = raw_input("Pl1 en word: ")
lives=6
print("pl2 have {} lives left".format(lives))
print("The word","_"*len(word))
word_guess = False
while lives >0:
    guess =input("pl2 guess letter  ")
    wordFormatted = ""
    for char in word:
	if char in word:
	   wordformatted = ch + " "
	else:
	    wordFormatted = "-"
    print(wordFormatted)
