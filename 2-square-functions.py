# TWO WAYS OF USING FUNCTIONS IN PYTHON

#1 As a procedure to do one single task

def area1(r):
    area = 3.14*r*r
    print("The area of circle radius {0} is {1}".format(r,area))

#2 As a function that returns a value

def area2(pizza):
    return 3.14*pizza*pizza

getRad = int(input("Enter radius of circle? "))

area1(getRad)

answer = area2(getRad)
print("The area of circle radius {0} is {1}".format(getRad,answer))


# IDENTIFY THESE PARTS OF A FUNCTION

#1 A function name
#2 A parameter name
#3 An argument value
#4 A function call
#5 A return value
