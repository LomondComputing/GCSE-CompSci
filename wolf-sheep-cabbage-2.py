# Wolf, sheep and cabbage river crossing problem - no lists

farmer = False
wolf = False
sheep = False
cabbage = False

f = 'farmer'
w = 'wolf'
s = 'sheep'
c = 'cabbage'

def canCross(who) :
    if who == f:
        return True
    elif    (who == w and wolf != farmer) or (who == s and sheep != farmer) or (who == c and cabbage != farmer) :
                print("Sorry, not on same bank as the farmer")
                return False
    else:
        return True

def whichBank(who) :
    if who == f :        
        bank = farmer
    elif who == w:
        bank = wolf
    elif who == s:
        bank = sheep
    elif who == c:
        bank == cabbage
    else:
        print('I don\'t know who',who,'is.')
    if bank:
        return 'left'
    else:
        return 'right'                   

def checkEnd() :
    if farmer and wolf and sheep and cabbage:
        print('Congratulations, you have managed to cross the river successfully!')
        return True
    elif wolf == sheep and wolf != farmer:
        print('The wolf has eaten the sheep! You have failed ...')
        return True
    elif sheep == cabbage and sheep != farmer:
        print('The sheep has eaten the cabbage! You have failed ...')
        return True
    else:
        return False
    
def printState() :
        left = []
        right = []
        if farmer:
            right.append(f)
        else:
            left.append(f)
        if wolf:
            right.append(w)
        else:
            left.append(w)
        if sheep:
            right.append(s)
        else:
            left.append(s)
        if cabbage:
            right.append(c)
        else:
            left.append(c)
        print ('LEFT BANK:',left)        
        print ('RIGHT BANK:',right)

printState()
while not checkEnd():
    who = str(input('Who is to cross the river now?'))
    if canCross(who):
        farmer = not farmer
        if who == w:
            wolf = not wolf
        elif who == s:
            sheep = not sheep
        elif who == c:
            cabbage = not cabbage
  
        print(who,'has now crossed to the other bank')    
        printState()



            
