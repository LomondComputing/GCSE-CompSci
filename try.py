num = input('Enter a number: ')

try:
    num = int(num)
except:
    print('Input must be an integer number...')
else:
    print(num)
