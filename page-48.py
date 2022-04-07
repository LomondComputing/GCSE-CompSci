# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
score = 0
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# Get first score
score = int (input ("Enter a score "))      
# Keep looping until user enters a 0
while (score != 0):   
    
    if (score >= 70):
        print("Distinction")
    elif (score >= 60):
        print("Merit")
    elif (score >= 50):
        print("Pass")
    else:
        print("No category found")
    # Get next score
    score = int(input("Enter a score "))    
print("Goodbye")
