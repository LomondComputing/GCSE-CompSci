# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import random           # Library name
 
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numberSweets = 0        # Number of sweets in a jar
count = 0               # Number of times to loop
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
while (count < 5):
    numberSweets = random.randint(100, 500)
    print (str(numberSweets) + 
           " sweets in the jar")
    count = count + 1
