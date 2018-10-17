# Program to sum a series of numbers that are entered

done = False
sum = 0

while not done:
    num = int(input('Enter a number: '))
    if num < 0:
        done = True
    else:
        sum += num

print('The total is',sum)
