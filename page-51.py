# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
rightPassword = "LetMeIn"       # Looking for this one
userPassword = ""               # Not set yet
maxTries = 3                    # How many times to ask
countTries = 0                  # User tries
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
while (countTries < maxTries):
    userPassword = input ("Enter the password: ")
    # Checks against good one
    if (userPassword == rightPassword):     
        print ("You entered the correct password")
        # Stops the loop
        countTries = maxTries               
    else:
        print ("You entered an incorrect password")
        # Counts one more try
        countTries = countTries + 1         
        print ("You have " + str(maxTries-countTries) + " tries left.")
 
print("Goodbye")
