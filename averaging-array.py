 # AVERAGING AN ARRAY

import random       # generate list of 1000 random numbers
numItems = 1000
stock = []
for n in range(numItems):
    stock.append(random.randint(0,10))

count = 0  # count of non-zero values 
total = 0  # total of array

for n in range(len(stock)):
    if stock[n] > 0:        # is it a non-zero value?
        count += 1          # increment count by 1
        total += stock[n]   # increment total by current number

if count != 0:      # if there are non-zero values
    print('There are',count,'non-zero values')
    average = total/count
else:       # otherwise all numbers are zero
    print('There are no non-zero values')
    average = 0

print('Average = ',average)
