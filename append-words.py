# Add words to a list until 'stop' entered. Output each item from the list on a new line

# FOR LOOP

print('FOR LOOP')
myList = []

for w in range(1000):
     word = input('Enter a new word: ')
     if word.lower() != 'stop':
          myList.append(word)
     else:
          break

for word in myList:
     print(word)


# WHILE LOOP

print('WHILE LOOP')
myList = []

word = input('Enter a new word: ')
while word.lower() != 'stop':
     myList.append(word)
     word = input('Enter a new word: ')

index = 0
while index < len(myList):
     print(myList[index])
     index += 1



