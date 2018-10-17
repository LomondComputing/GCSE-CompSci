''' FUNCTIONS
Some important reminders about Functions in Python:

* Functions are used to simplify the structure of a program
* Usually they perform ONE particular action
* Give them sensible names (use camelText)
* They may or may not have input parameters (..)
* They may or may not return a value
* They can return multiple values
* Everything in the function is indented
'''

# Make a function that returns the square a number

def squareNum(x):
    return x**2

# Make a function that inputs a name and age and returns both

def getNameAge():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    return name, age

# Make a function that returns the sums all the numbers up to the input number

def sum(x):
    total = 0
    for num in range(1,x+1):
        total += num         # total = total + num
    return total

# Make a function that returns the factorial of a number eg. 4! = 4*3*2*1

def fact(x):
    product = 1
    for num in range(1,x+1):
        product *= num
    return product

# Make a function that checks if a number is even

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Make a function that inputs a password of at least 8 chars and returns it

def inputPass():
    pw = input('Enter your password: ')
    while len(pw) < 8:
        print('Sorry, must be at least 8 chars')
        pw = input('Try entering your password again: ')
    print('That is a valid password')
    return pw

# Make a function that inputs a age of between 3 and 120 and returns it

def getAge(age):
    age = int(input('Enter your age: '))
    while age<3 or age>120:
        print('Sorry, age must be between 3 and 120')
        age = int(input('Try entering your age again: '))
    print('That is a valid age')
    return age
        
# Make a function that counts the occurrences of a character in a string

def count(char,string):
    total = 0
    for c in string:
        if c == char:
            total += 1
    return total


# Make a function that checks if something is in a list

def member(something,aList):
    if something in aList:
        return True
    else:
        return False

# Make a function that replaces all somethings in a list with something else 

def replace(something,somethingelse,aList):
    for item in range(0,len(aList)):    # loop through the list
        if aList[item] == something:    # have we found the something?
            aList[item] = somethingelse # replace it
    return aList

  
# Make a function that inserts something in a list at an index position

def insert(something,aList,pos):
    aList.insert(pos,something)
    return aList


# Make a function that returns a list of all multiples of a number up to a maximum value

def multiples(num,max):
    multList = []
    for i in range(num,max+num,num):
        multList.append(i)
    return multList

# Make a function that removes all occurrences of something from a list and returns
# the new list


# Make a function that removes all duplicate items from a list

# Make a function that reverses a list and returns the new list

# Make a function that swaps the contents of two variables
