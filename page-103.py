# -----------------------------------------------------------------
# Global variables
# -----------------------------------------------------------------
score = 0
count = 0
distinctions = 0
merits = 0
passes = 0
noAward = 0
layout = "Total: {}, Distinctions: {}, " \
         "Merits: {}, Passes: {}, No award: {}"
 
# -----------------------------------------------------------------
# Main program
# -----------------------------------------------------------------
# Get first score
score = int (input ("Enter a score "))      
 
while (score != 0):             # Keep looping until user 
                                # enters a 0
    count = count + 1
    if (score >= 70):
        distinctions = distinctions + 1
    elif (score >= 60):
        passes = passes + 1
    elif (score >= 50):
        merits = merits + 1
    else:
        noAward = noAward + 1
 
    score = int(input("Enter a score "))    # Get next score
 
print (layout.format (count, distinctions, 
                      merits, passes, noAward))
print("Goodbye")
