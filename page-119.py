# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
classTable = [[384, "Collins", "Ivy", 2010, 15.34],
              [405, "Brown", "James", 2011, 18.87],
              [410, "Jones", "Karen", 2010, 12.98]]
 
# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def displayNames (pTable):
    for student in pTable:
        print ("student variable = list:", student)
        print ("Name: " + student[2] + " " + student[1])
 
# -----------------------------------------------------------------
# Main program
# -----------------------------------------------------------------
 
# Call subprogram to display all the names
displayNames(classTable)
