# Wolf, sheep and cabbage river crossing problem

left = ["wolf","sheep","cabbage","farmer"]
right = []

def canCross(who) :
    if who == 'farmer':
        return True
    else:
        whoBank = whichBank(who)
        farmerBank = whichBank("farmer")
        if whoBank != farmerBank:
            print("Sorry, not on same bank as the farmer")
            return False
        else:
            return True

def whichBank(who) :
    for i in range(len(left)) :
        if left[i] == who :
            return 'left'
    for i in range(len(right)) :
        if right[i] == who :
            return 'right'
                   
def cross(who) :
    if canCross(who):
        currentBank = whichBank(who)
        if currentBank == 'left':
            newBank = 'right'
            left.remove(who)
            right.append(who)
            if who != 'farmer':
                left.remove("farmer")
                right.append("farmer")             
        else:
            newBank = 'left'
            right.remove(who)
            left.append(who)
            if who != 'farmer':
                left.remove("farmer")            
                right.append("farmer")
        print(who,'has moved to the',newBank,'bank.')
        checkState()
        printState()

def checkState() :
    wolfBank = whichBank('wolf')
    sheepBank = whichBank('sheep')
    cabbageBank = whichBank('cabbage')
    farmerBank = whichBank('farmer')
    if (wolfBank == sheepBank) and (wolfBank != farmerBank):
        print('The wolf has eaten the sheep! You have failed ...')
        exit()
    elif  (sheepBank == cabbageBank) and (sheepBank != farmerBank):
        print('The sheep has eaten the cabbage! You have failed ...')
        exit()
    
def printState() :
    print ('Left bank:',left)
    print ('Right bank:',right)


printState()
cross('sheep')
cross('farmer')
cross('wolf')
cross('sheep')
cross('cabbage')
cross('farmer')
cross('sheep')

            
