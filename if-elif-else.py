# Make a program to ask you for your year at school
# The program will output the Key Stage you are in
# or tell you you have left school

#  not started yet: <1
#  KS1:  1, 2
#  KS2:  3,4,5,6
#  KS3:  7,8,9
#  KS4:  10,11
#  KS5:  12,13
#  left school: >13

# and, or, not


# Make a program to input two numbers and output which number is larger
# How about 3 numbers?

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if num1 > num2 and num1 > num3:
     print(num1,'is bigger than',num2,'and',num3)
elif num2 > num1 and num2 > num3:
     print(num2,'is bigger than',num1,'and',num3)
elif num3 > num1 and num3 > num2:
     print(num3,'is bigger than',num1,'and',num2)     
else:
     

