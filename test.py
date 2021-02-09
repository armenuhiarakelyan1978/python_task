#!/usr/bin/python
print "Please enter the string "
m = raw_input()
def upper(m):
    k = m.upper()
    print(k)
upper(m)
print "Please split the string using comma"
h = raw_input()
def split(h):
    out = []
    word = ""
    for c in h:
        if c not in (","):
           word += c
        else:
            out.append(word)
            word = ""
    out.append(word)
    return out
print(split(h))

print "Please strip the string"
g = raw_input()
def strip(g):
    start = 0
    end = -1
    while g[start].isspace():
        start += 1
    while g[end].isspace():
        end -= 1
    end += 1
    return g[start:end]
print(strip(g))

print "Please enter thr string for title "
ww = raw_input()
def title(ww):
   new = ""
   delim = "'.,;:?! "
   next = True
   for char in ww:
       if next:
          char = char.upper()
       new += char
       next = char in delim
   return new
print(title(ww))

print "Please enter the string for replace"
qq = raw_input()
print "enter the search string"
se  = raw_input()
print "enter the replace string"
repl = raw_input()
def replacer(qq, se, repl):
    return(qq.replace(se,repl))
print(replacer(qq,se,repl))
