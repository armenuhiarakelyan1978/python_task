#!/usr/bin/python
word = "secret"
guesses = ''
turns = 10
while turns>0:
   failed = 0
   for char in word:
       if char in guesses:
	  print char
       else:
     	   print "-"
           failed +=1
           if failed == 0:
              print "you won"
              break
              print
	      guess = raw_input("guess a character")
              guesses += guess
              if guess not in word:
                 turns -= 1
                 print "wrong"
                 print "you have" + turns
                 if turns == 0:
	            print "you lose"       


