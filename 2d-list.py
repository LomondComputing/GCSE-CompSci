# Example of using List Comprehension to fill a 2D list with data

# Initialise variables for dimensions of 2D list
rows = 4
columns = 6


# Use list comprehension to initialise all elements to 0
myList=[[0 for col in range(columns)] for row in range(rows)]


# How to assign a value to a particular index position
myList[2][3] = 99


# How to index a particular element in 2D list
print(myList[2][3])


# Use nested loop to iterate over each row and column, printing the element
for row in range(rows):
    for col in range(columns):
        print(myList[row][col],' ',end='')
    print()



        

