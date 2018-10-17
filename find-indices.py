# My Function

def findIndices(anArray, searchItem):
    i = 0
    indexList = []

    while ( i < len(anArray) ):
        if anArray[i] == searchItem:
            indexList.append(i)

        i += 1

    return indexList

