# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
validNum = False            # Assume everything is invalid
userNum = 0                 # Set to an invalid value
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
while (not validNum):
    userNum = int (input (
        "Enter a number between 1 and 10 "))
    if (userNum >= 1) and (userNum <= 10):
        validNum = True
    else:
        print ("Invalid number, try again ")
 
print ("You entered " + str(userNum))
