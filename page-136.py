# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
validChoice = False             # Assume all invalid
userChoice = ""                 # Empty string
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
while (not validChoice):
    userChoice = input (
        "Enter either 'Yes' or 'No' ")
    if (userChoice == "Yes") or (userChoice == 
                                 "No"):
        validChoice = True
    else:
        print ("Invalid input, try again ")
 
print ("You entered " + userChoice)
