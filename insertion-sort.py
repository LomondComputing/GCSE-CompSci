# Program to demonstrate an INSERTION SORT

# Input number of values to sort
howMany = int(input('How many values do you want to sort? '))

# Define random list of numbers
import random
data = [ random.randint(1,100) for i in range(howMany) ]

# Output the unsorted list
print('INSERTION SORT')
print("Unsorted list: ",data)

length = len(data)      # find how many items in list

current = 1     # start at index 1 because the first item is already sorted!
    
while current < length:     # while not at end of list
    index = current         # set current index position
    placeFound = False      # at the moment we don't know where it is to go

    # find the correct place and 'bubble up' the sorted portion    
    while index > 0 and not placeFound:
        if data[index] < data[index-1]:  # have not yet found the correct place
            # Swap data[index] and data[index-1]
            print('Swapping',data[index],'with',data[index-1])
            temp = data[index]
            data[index] = data[index-1]
            data[index-1] = temp

            index -= 1      # decrement the index
        else:
            placeFound = True   # we have found the correct position
            
        current += 1        # move the marker for the sorted portion up one
        
print("Sorted list:",data)



