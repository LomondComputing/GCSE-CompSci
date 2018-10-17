# My Function

def myFunction():
    anArray = [78, 83, 72, 80, 83]
    f = False
    c = -1
    i = 0
    b = 75

    while ( not f ):
        if anArray[i] == b:
            f = True
            c = i
        else:
            i += 1

    return c

