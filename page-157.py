# --------------------------------------------------------------
# Constants
# --------------------------------------------------------------
FILENAME = "StudentRecords.txt"
FILENAMEOUT = "StudentRecordsOutput.txt"
 
# --------------------------------------------------------------
# Global variables
# --------------------------------------------------------------
studentTable = []                   # Holds all the records
 
# --------------------------------------------------------------
# Subprograms
# --------------------------------------------------------------
def loadData ():
    theFields = []          # Structure of individual fields
    aRecord = []            # A single student record
 
    theFile = open(FILENAME, "r")   # Open for reading only
 
    for line in theFile:            # Read one line
        line = line.strip()         # Remove the CR
 
        # Each field is appended to a list of fields
        #    without the commas
        theFields = line.split(",")
 
        # Put values into a record, converting types
        # Fields don't have to be in the same order
        aRecord = []                            # Clear record
        aRecord.append (int (theFields[0]))     # Integer
        aRecord.append (theFields[1])           # String
        aRecord.append (theFields[2])           # String
        aRecord.append (int (theFields[3]))     # Integer
        aRecord.append (float (theFields[4]))   # Real
 
        # Put this record into the table of records
        studentTable.append (aRecord)
 
    theFile.close()         # Close the file
 
def saveData ():
    lineOut = ""
 
    theFile = open(FILENAMEOUT, "w")    # Open for writing
 
    for student in studentTable:        # Get one record
        lineOut = ""                    # Clear output line
 
        # Build output line from fields, add commas
        lineOut = lineOut + str (student[0])    # Convert
        lineOut = lineOut + ","                 # Add comma
        lineOut = lineOut + student[1] + ","
        lineOut = lineOut + student[2] + ","
        lineOut = lineOut + str(student[3]) + ","
        lineOut = lineOut + str(student[4])      # No comma
 
        lineOut = lineOut + "\n"                # Add CR
 
        theFile.write(lineOut)          # Write the line
 
    theFile.close()         # Close the file
# --------------------------------------------------------------
# Main program
# --------------------------------------------------------------
loadData ()                 # Load the data from file
 
# For testing only, change the records
for student in studentTable:
    student[0] = student[0] + 100
    student[1] = student[1].upper()
 
saveData()                  # Save the data to file
