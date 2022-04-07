# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
mark1 = 0           # Homework marks
mark2 = 0
mark3 = 0
maxMark = 0         # Reduce number of print statements
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
mark1 = int (input ("Enter the first mark "))
mark2 = int (input ("Enter the second mark "))
mark3 = int (input ("Enter the third mark "))
 
if (mark1 > mark2):
    if (mark1 > mark3):
        maxMark = mark1
    else:
        maxMark = mark3
elif (mark2 > mark3):
    maxMark = mark2
else:
    maxMark = mark3
 
print ("The maximum mark is", maxMark)
