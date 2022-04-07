# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
MIN_NAME = 1                # Constants for name length
MAX_NAME = 20
 
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
firstName = ""              # User types
valid = False               # Assume everything is invalid
length = 0                  # Invalid length
newName = ""                # Invalid capitalised name
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
while (not valid):
    firstName = input ("Enter your first name: ")
    length = len(firstName)
    if (length >= MIN_NAME) and (length <= MAX_NAME):
        if (firstName.isalpha()):
            newName = firstName
            print ("Your entry is valid.\nYour name is: ", newName)
            valid = True
        else:
            print ("Your entry is not valid")
    else:
        print ("Your entry is not the right size")
