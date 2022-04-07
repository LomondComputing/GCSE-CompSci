# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
score = 0                   # Invalid score
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
 
try:
    # This is the normal program code. It executes.
    score = int (input ("Enter a score: "))
except:
    # If there is any Exception this code executes
    print ("Your entry is invalid")
else:
    # If there is no Exception, 
    # then this code executes
    print ("You entered:", score)
 
print ("Goodbye")
