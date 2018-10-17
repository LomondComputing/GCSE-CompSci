def printR():
    print("R5=",R5,"R6=",R6,"R7=",R7,"R8=",R8)


R5 = 4
R7 = 0

while R5 != 0:
    R6 = R5-1
    R5 = R6
    R8 = R7+R5
    R7 = R8
    printR()

R8 = 0

printR()


