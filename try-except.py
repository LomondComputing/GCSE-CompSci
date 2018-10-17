'''
Activity 16.7
Try command: divide by zero error check
Write a program that asks the user for two numbers,
then divides the numbers and displays the answer.
If the program generates a divide by zero error,
display a message to explain they entered a zero as the second number.
'''

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

try:
    answer = num1/num2
except ZeroDivisionError:
    print('You entered zero as the second number')
else:
    print(num1,'/',num2,'=',num1/num2)

