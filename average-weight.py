# GCSE Year 10 Computer Science Exam question

sumWeights = 0
fruitWeights = []
fruitTypes = []
validFruits = ["apple","banana","pear","peach","plum","orange","grape","mango","kiwi","melon"]
valid = False

def member(a,l):
    i = 0
    found = False
    while not found and i < len(l):
        if l[i] == a:
            found = True
        i += 1
    return found
        
while not valid:
    numFruits = int(input("How many fruits do you want to weigh? "))
    if numFruits >= 1 and numFruits <= 10:
        valid = True
    else:
        print("Number of fruits must be between 1 and 10")

for w in range(numFruits):
    valid = False
    while not valid:
        fruit = input("What type of fruit? ")
        if member(fruit,validFruits):
            valid = True
        else:
            print("Sorry, I don't recognise that fruit")
    fruitTypes.append(fruit)
    valid = False
    while not valid:
        fruitWeight = int(input("Enter weight: "))
        if 1 <= fruitWeight <= 999:
            valid = True
        else:
            print("Fruit weight must be less than 1000")
    fruitWeights.append(fruitWeight)        
    sumWeights += fruitWeight

average = float(sumWeights/numFruits)
lightest = fruitWeights[0]
heaviest = fruitWeights[0]
lightestFruit = fruitTypes[0]
heaviestFruit = fruitTypes[0]

for f in range(numFruits):
    if fruitWeights[f] < lightest:
        lightest = fruitWeights[f]
        lightestFruit = fruitTypes[f]
    if fruitWeights[f] > heaviest:
        heaviest = fruitWeights[f]
        heaviestFruit = fruitTypes[f]

print("\nFRUITS\tWEIGHTS")
print("------\t-------")
for f in range(numFruits):
    print(fruitTypes[f],"\t",fruitWeights[f])
    
print("\nYou entered",numFruits,"fruits")
print("The average weight is:",format(average,'.2f'))
print("The lightest fruit is a",lightestFruit,"weighing",lightest)
print("The heaviest fruit is a",heaviestFruit,"weighing",heaviest)
