# Program to find the mean of a series of a numbers

sum = 0
count = 0

num = int(input('Enter a number (0 to quit): '))

while num != 0:
    sum += num
    count += 1
    num = int(input('Enter a number (0 to quit): '))

mean = sum/count
print('The mean of the numbers is: ',mean)
