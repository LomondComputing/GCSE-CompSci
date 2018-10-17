# Program to do a binary search of a sorted list

def binarySearch(item,aList):
    length = len(aList)                         # find length of list
    item = str(item)
    first = 0                                   # start at first element
    last = length-1                             # finish at last element
    found = False                               # so far, number is not found
    position = -1
    divs = 0
    
    while (first <= last and not found):        # so long as not at end of list without finding it
        middle = (first + last) // 2            # divide list in the middle
        divs += 1
        if item == str(aList[middle]):          # if we've found it
            found = True                        # done
            position = middle
        elif item < str(aList[middle]):              # otherwise if it's in the first half
            last = middle - 1                   # reset the end marker
        else :                                  # otherwise it must be in the second half
            first = middle + 1                  # so reset the start marker

    return position, divs


import random
numbers = [ random.randint(1,100) for i in range(10) ]   # initialise list of numbers
numbers.sort()
print('Numbers=',numbers)                               # print the list

searchItem = int(input("Enter value to search for: "))   # enter value to search
result, divisions = binarySearch(searchItem, numbers)

if result != -1:                   # if we found it
    print('Item %s was found in list %s at position %s' % (searchItem,numbers,result)  )          # tell us it's there
else:                                       # otherwise
    print('Item %s was NOT found in list %s' % (searchItem,numbers)  )      # tell us it's not there

print('Number of divisions:',divisions)
