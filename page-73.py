# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numCoffee = 0                   # For counting up
numTea = 0
noDrink = 0
choice = ""                     # What the person wants to drink
drinks = ["T", "T", "C", "T", "C", "T", "T", 
          "C", "T", "C"]
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
for choice in drinks:
    if (choice == "T"):
        numTea = numTea + 1
    elif (choice == "C"):
        numCoffee = numCoffee + 1
    else:
        noDrink = noDrink + 1
print ("Coffees = " + str(numCoffee))
print ("Teas = " + str(numTea))
print ("No drink = " + str(noDrink))
