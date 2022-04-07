# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
score = 0                   # Invalid score
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
 
while (score == 0):         # Keep looping
    try:
        # This is the normal program code. 
        # It executes.
        score = int (input ("Enter a score: "))
    except TypeError:
        # If there is any Exception this code 
        # executes
        print ("Your entry is invalid. Try again.")
        score = 0           # Keep loop going
    else:
        # If there is no Exception, 
        # then this code executes
        print ("You entered:", score)
 
print ("Goodbye")
