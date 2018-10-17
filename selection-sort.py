# Program to demonstrate the SELECTION SORT algorithm

howMany = int(input('How many values do you want to sort? '))

# Define random list of numbers
import random
data = [ random.randint(1,100) for i in range(howMany) ]

# Output the unsorted list
print('SELECTION SORT')
print("Unsorted list:",data)

length = len(data)                      # find how many items in list
firstUnsorted = 0
    
while firstUnsorted < length-1:         # while not sorted yet
    # find smallest unsorted item
    indexOfSmallest = firstUnsorted         
    index = firstUnsorted + 1
    
    while (index <= length - 1) :
        if data[index] < data[indexOfSmallest] :
            indexOfSmallest = index
        index = index + 1
    
    # swap first unsorted with the smallest item
    print('Swapping',data[indexOfSmallest],'with',data[firstUnsorted])
    tempItem = data[firstUnsorted]
    data[firstUnsorted] = data[indexOfSmallest]
    data[indexOfSmallest] = tempItem

    # reset pointer to past the sorted portion
    firstUnsorted = firstUnsorted + 1
    print("Unsorted list: ",data)
        
print("Sorted list:",data)



