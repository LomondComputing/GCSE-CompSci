
# A program to enter two numbers and add and subtract them

# INPUT
num1 = int(input("What is first number? "))
num2 = int(input("What is second number? "))

# PROCESS,
add = num1+num2
sub = num1-num2

# OUTPUT
print(num1,"+",num2,"=",add)
print(num1,"-",num2,"=",sub)

if num1 > num2:
                 print(num1,"is bigger than",num2)
elif num1 == num2:
                print(num,"is equal to",num2)
else:
                 print(num2,"is bigger than",num1)
