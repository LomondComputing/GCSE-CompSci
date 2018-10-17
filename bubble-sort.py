# Program to demonstrate the BUBBLE SORT algorithm

howMany = int(input('How many integer values do you want to sort? '))

# Define random list of numbers
import random
data = [ random.randint(1,100) for i in range(howMany) ]

# Output the unsorted list
print('BUBBLE SORT...')
print("Unsorted list: ",data)

length = len(data)      # find how many data items in list
firstUnsorted = 0
swap = True
numSwaps = 0
numComps = 0
    
while (firstUnsorted  < length - 1 and swap):
    swap = False

    # 'Bubble up' the smallest item in the unsorted part of list
    index = length - 1
    while (index > firstUnsorted) :
        numComps += 1
        if (data[index] < data[index-1]) :
            # Swap data[index] and data[index-1]
            print('Swapping',data[index],'with',data[index-1],'...')
            temp = data[index]
            data[index] = data[index-1]
            data[index-1] = temp

            swap = True
            numSwaps += 1

        index -= 1
               
    firstUnsorted += 1
    print("Unsorted list: ",data)
        
print("\nSorted list:",data)
print('There was a total of',numSwaps,'swaps')
print('There was a total of',numComps,'comparisons')


