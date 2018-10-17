'''
Validation – LENGTH CHECK
Write a program that asks the user to input a password
and then uses a length check to make sure the password
is at least eight characters long. If it is shorter than
eight characters the user is asked to enter a different password.
'''

# Method 1 - while loop checking length condition

pw = input('Please enter your password: ')

while len(pw) < 8:
    print('Password must have at least 8 characters')
    pw = input('Please enter your password: ')
    
print('Thank you')




# Method 2 - while loop with Boolean flag (sentinel) condition

valid = False

while not valid:
    pw = input('Please enter your password: ')
    if len(pw) >= 8:
        valid = True
    else:
        print('Password must have at least 8 characters')

print('Thank you')




# Method 3 - infinite while loop with break ** BAD PROGRAMMING TECHNIQUE

while True:
    pw = input('Please enter your password: ')
    if len(pw) >= 8:
        break
    else:
        print('Password must have at least 8 characters')

print('Thank you')
