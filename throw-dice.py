# Write a program that acts like a dice.
# After each ‘throw’ of the dice it should
# ask if the player wishes to continue
# and stop when they enter ‘N’.

import random

cont = True
print('Welcome to the Dice rolling game...')

while cont:
    throw = random.randint(1,6)
    print('Throw was a ...',throw)
    ask = input('Do you want to throw again (y/n)? ')
    if ask[:1].lower() != 'y':
        cont = False

print('Thank you for playing ... Goodbye!')
