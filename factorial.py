# Program to work out factorial of a number
# eg. 4! = 1*2*3*4

num = int(input('Which factorial do you want? '))
product = 1

print('FOR LOOP')

for i in range(1,num+1):
    product = product*i

print('The factorial of',num,'is',product)

print('WHILE LOOP')




