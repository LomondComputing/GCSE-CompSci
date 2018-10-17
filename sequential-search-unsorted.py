# Program to do a linear search of an unsorted list of integers

import random
numbers = [ random.randint(1,20) for i in range(10) ]   # initialise list of numbers
print('Numbers=',numbers)                               # print the list

searchItem = int(input("Enter value to search for: "))  # enter search item

def linearSearch(item, aList) :
    pos = 0                                         # start at first element
    found = False                                   # so far it's not found
    length = len(aList)                             # find how many numbers in list

    while (pos < length) and (not found) :
        if aList[pos] == item:                      # is number the one we're looking for?
            print('Item %s is found in list %s at index %s' % (item, aList, pos) )         
            return True                             # we've found it
        else:                                       # otherwise
            pos += 1                                # look at the next number
    print('Item %s was NOT found in list %s' % (item, aList))  
    return False


linearSearch(searchItem,numbers)          
    



        
