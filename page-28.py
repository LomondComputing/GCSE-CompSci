# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
finishedTest = True         # Initialisation as Boolean
totalScore = 7              # Initialisation as integer
cost = 12.74                # Initialisation as float
theColour = "green"         # Initialisation as string
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
print ("========== Explicit type conversion ==========")
print (finishedTest, type(finishedTest), "===>",
       int(finishedTest), type(int(finishedTest)))
print (totalScore, type(totalScore), "===>",
       str(totalScore), type(str(totalScore)))
print (cost, type(cost), "===>",
       int(cost), type(int(cost)))
print (theColour, type(theColour), "===>",
       bool(theColour), type(bool(theColour)))
