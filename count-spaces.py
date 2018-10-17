# Counting spaces in a string

def space1(s):
     counter = 0
     for c in s:
          if c == ' ':
               counter += 1
     return counter

def space2(s):
     return len(s.split(' '))-1

def space3(s):
     return s.count(' ')
