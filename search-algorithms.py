# Program to do a binary search of a sorted list

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]      # list must be initially sorted
searchItem = input("Enter value to search for: ")   # enter value to search


def binarySearch(item,list) :
    length = len(list)       # find length of list
    first = 0                   # start at first element
    last = length-1             # finish at last element
    found = False               # so far, number is not found
    
    while (first <= last and not found) :           # so long as not at end of list without finding it
        middle = (first + last) / 2                 # divide list in the middle
        if item == list[middle] :                   # if we've found it
            return(True)                            # done
        else :
            if item < list[middle] :                # otherwise if it's in the first half
                last = middle - 1                   # reset the end marker
            else :                                  # otherwise it must be in the second half
                first = middle + 1                  # so reset the start marker
    return(False)


if binarySearch(searchItem,numbers) :
    print "Item",searchItem,"is found"
else :
    print "Item",searchItem,"is not found"

        
