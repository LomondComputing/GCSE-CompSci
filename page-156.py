# --------------------------------------------------------------
# Constants
# --------------------------------------------------------------
FILENAME = "StudentRecords.txt"
 
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
 
        # Each field is appended to a list of fields without the commas
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
 
# --------------------------------------------------------------
# Main program
# --------------------------------------------------------------
loadData ()
