# Program to do a sequential search of a sorted list

import random
numbers = [ random.randint(1,20) for i in range(10) ]   # initialise list of numbers
numbers.sort()                                          # sort the list
print('Numbers=',numbers)                               # print the list

searchItem = int(input("Enter value to search for: "))  # enter search item

def seqSearch2(item,aList):
    index = 0               # start at first index position
    found = False           # so far it's not found
    length = len(aList)   # find how many numbers in list

    while (index < length) and (not found):         # repeat while not at end of list and item not found
        if aList[index] == item:            # is number the one we're looking for?
            print('Item %s was found in list %s at position %s' % (item,aList,index)  )
            return True                            # we've found it
        elif (aList[index] > item):         # otherwise
            return False                          # end loop because past the point
        else:                                       # otherwise
            index += 1                              # look at the next number
    return False

if not(seqSearch2(searchItem,numbers)):                                                      # otherwise
    print(Item %s was NOT found in list %s' % (searchItem,numbers)  )                # tell us it's not there


        
