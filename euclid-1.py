# Euclid's algorithm for finding GCDs

def euclid1(a, b):
    while a != b: 
        if a > b:
           a = a - b
        else:
           b = b - a 
    return a


def euclid2(a, b):
    while b != 0:
       t = b 
       b = a % b 
       a = t 
    return a

def euclid3(a, b):
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
