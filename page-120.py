# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
classTable = [[384, "Collins", "Ivy", 2010, 15.34],
              [405, "Brown", "James", 2011, 18.87],
              [410, "Jones", "Karen", 2010, 12.98]]
firstName = ""
lastName = ""
id = -1
 
# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def findStudentID (pFirst, pLast):
    ndxRow = 0                  # Index in table
    found = False               # Not found
    id = 0                      # Invalid id number
 
    # Loop if not yet found and more records left
    while ((not found) and (ndxRow < len(classTable))):
        print ("Row is: ", classTable[ndxRow]) # Debug only
        # Pick up a whole record
        student = classTable[ndxRow]
 
        # Either not a match, then look at next record
        if ((student[1] != pLast) or
            (student[2] != pFirst)):
            ndxRow = ndxRow + 1
        else:                       # Both a match
            found = True            # Stop the loop
            id = student[0]      # Pick up id number
    return (id)
 
# -----------------------------------------------------------------
# Main program
# -----------------------------------------------------------------
 
firstName = "James"
lastName = "Brown"
id = findStudentID(firstName, lastName)
if (id != 0):
    print (firstName + " " + lastName + " is ID: " + str(id))
else:
    print (firstName + " " + lastName + " is not in class")
