# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numCoffee = 0                   # For counting up
numTea = 0
noDrink = 0
choice = ""                     # What the person wants to drink
layout = ""                     # For formatting string
drinks = ["T", "T", "C", "T", "C", "T", "T", "C", "T", "C"]
 
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
 
# Layout and print the headers for the columns
layout = "{:^6}  {:^6}  {:^6}  {:^6}"
print (layout.format("Coffee", "Tea", "None", "Total"))
 
# Print a line to divide the headers from the numbers
print ("="*30)
 
# Print out the line required
print (layout.format(numCoffee, numTea, noDrink, len(drinks)))
