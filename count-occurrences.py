
# Function to count occurrences of something in a list or string

def count(searchItem,aList):
    count = 0
    for x in aList:
        if x == searchItem:
            count += 1
    return count

def countAll(aList):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0]
    for x in aList:
        result[x] = result[x] + 1
    return result



