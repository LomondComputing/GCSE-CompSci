# Program to test a number of sorting algorithms
# Selection sort, Bubble sort, Insertion sort

# Input number of values to sort
howMany = int(input('How many values do you want to sort? '))

# Define random list of numbers
import random, time

numbers = [ random.randint(1,100) for i in range(howMany) ]
names = [ chr(i) for i in range(90,64,-1) ]

# -----------------------------------------------------------
# Selection Sort Function
def selectionSort(data):
     firstUnsorted = 0
     swaps = 0
     length = len(data)                          # find how many items in list
    
     while (firstUnsorted < length-1) :          # while not sorted yet
        # find smallest unsorted item
        indexOfSmallest = firstUnsorted         
        index = firstUnsorted + 1
        
        while (index <= length - 1) :
            if data[index] < data[indexOfSmallest] :
                indexOfSmallest = index
            index += 1
   
        # swap first unsorted with the smallest
        tempItem = data[firstUnsorted]
        data[firstUnsorted] = data[indexOfSmallest]
        data[indexOfSmallest] = tempItem
        swaps += 1

        firstUnsorted += 1

     print('Number of swaps:',swaps)
     return data
# -----------------------------------------------------------
# Bubble Sort Function
def bubbleSort(data):
     firstUnsorted = 0
     swap = True
     swaps = 0
     length = len(data)
    
     while firstUnsorted  < length - 1 and swap:
        swap = False

        # 'Bubble up' the smallest item in unsorted part of list
        index = length - 1
        while index > firstUnsorted:
            if data[index] < data[index-1] :
                # Swap data[index] and data[index-1]
                temp = data[index]
                data[index] = data[index-1]
                data[index-1] = temp
                
                swaps += 1
                swap = True

            index -= 1
              
        firstUnsorted += 1

     print('Number of swaps:',swaps)
     return data







# -----------------------------------------------------------
# Insertion Sort Function
def insertionSort(data) :
     current = 1
     swaps = 0
     length = len(data)
    
     while current < length:
        index = current
        placeFound = False
        
        while index < 0 and not placeFound:
            if data[index] < data[index-1]:
                # Swap data[index] and data[index-1]
                temp = data[index]
                data[index] = data[index-1]
                data[index-1] = temp
                swaps += 1

                index -= 1
            else :
                placeFound = True

        current += 1

     print('Number of swaps:',swaps)
     return data
# -----------------------------------------------------------
# Output the unsorted lists
print('\nSORTING ALGORITHMS')
print ("Unsorted list of numbers: ",numbers)
print ("Unsorted list of names:",names)

# Test Selection Sort
start_time = time.time()
print('\nSELECTION SORT')
newNumbers = selectionSort(numbers)
newNames = selectionSort(names)
print ("Selection sort on numbers:", newNumbers)
print ("Selection sort on names:", newNames)
print("--- %s seconds ---" % (time.time() - start_time))

# Test Bubble Sort
start_time = time.time()
print('\nBUBBLE SORT')
print ("Bubble sort on numbers:",bubbleSort(numbers))
print ("Bubble sort on names: ",bubbleSort(names))
print("--- %s seconds ---" % (time.time() - start_time))

# Test Insertion Sort
start_time = time.time()
print('\nINSERTION SORT')
print ("Insertion sort on numbers: ",insertionSort(numbers))
print ("Insertion sort on names: ",insertionSort(names))
print("--- %s seconds ---" % (time.time() - start_time))
