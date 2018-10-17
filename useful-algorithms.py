
# Function to count occurrences of something in a list or string

def count(searchItem,aList):
    count = 0
    for num in aList:
        if num == searchItem:
            count += 1
    return count


# Same count occurrences function, this time using a FOR .. IN .. RANGE loop

def count2(searchItem,aList):
    count = 0
    for num in range(0,len(aList)):
        if aList[num] == searchItem:
            count += 1
    return count


# Function to calculate the mean of a list of numbers

def mean(aList):
    sum = 0
    for num in aList:
        sum += num
    mean = sum / len(aList)
    return mean
















# Function to find the largest number in a list

def largest(aList):
    
    max = aList[0]
    for num in aList:
        if num > max:
            max = num
    return max



























# Function to find the smallest number in a list

def smallest(aList):
    min = aList[0]
    for num in aList:
        if num < min:
            min = num
    return min


















# Function to check if something is in a list

def member(something,aList):
    if something in aList:
        return True
    else:
        return False




















def countAll(aList):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0]
    for x in aList:
        result[x] = result[x] + 1
    return result



