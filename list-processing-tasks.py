# LIST PROCESSING TASKS
# For all tasks it is assumed the input list will have at least 4 integers.

# On the first line, print all the integers in the list.
# On the second line, print how many integers are in the list.
# On the third line, print the first integer in the list.
# On the fourth line, print the last integer in the list.
# On the fifth line, print the integer that is midway through the list.
# On the sixth line, print the first three integers in the list.
# On the seventh line, print the last two integers in the list.
# On the eighth line, print the third and fourth integers in the list.
# On the ninth line, print all the integers with odd indices.
# On the tenth line, print only the even integers in the list.
# On the eleventh line, print the list in reverse order.
# On the twelfth line, print the list in ascending order of integers.
# On the thirteenth line, print the sum of all the integers.
# On the fourteenth line, print the average of all the integers.
# On the fifteenth line, print how many of the integers are non-zero

# List Comprehension that reads a list of integers separated by spaces:
print('Enter at least four integer values separated by spaces, ending with ENTER')
a = [int(s) for s in input().split()]

# Program output (the first task has been done for you...)
print('1. All integers: ',end='')
for i in a:
    print(i, ' ', end='')
print()

