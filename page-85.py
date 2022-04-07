# --------------------------------------------------------------
# Import libraries
# --------------------------------------------------------------
import random
 
# --------------------------------------------------------------
# Global variables
# --------------------------------------------------------------
userRoll = 0                    # Global variable
 
# --------------------------------------------------------------
# Subprograms
# --------------------------------------------------------------
def roll():
    print ("Entering subprogram roll()")
    theDie = 0                          # Local variable
    theDie = random.randint(1,6)
    print ("Local variable 'theDie' = " +
           str(theDie))
    print ("Leaving subprogram roll()")
    return (theDie)
 
# --------------------------------------------------------------
# Main program
# --------------------------------------------------------------
print ("Entering main program")
userRoll = roll()
print ("Global variable 'userRoll' = " + 
       str(userRoll))
print ("Exiting main program")
