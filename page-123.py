# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
 
classTable = []
 
# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def showClass ():
    if (len(classTable) != 0):
        for student in classTable:
            print (student)
    else:
        print ("----- Table is empty -----")
 
def loadData (pID, pLast, pFirst, pBirth, pBalance):
    aRecord = []
 
    # Make a single student record
    aRecord.append (pID)
    aRecord.append(pLast)
    aRecord.append(pFirst)
    aRecord.append(pBirth)
    aRecord.append(pBalance)
 
    # Append it to the class table
    classTable.append (aRecord)
 
def insertRecord (pID, pLast, pFirst, pBirth, pBalance, pIndex):
    aRecord = []
 
    # Make a single student record
    aRecord.append (pID)
    aRecord.append(pLast)
    aRecord.append(pFirst)
    aRecord.append(pBirth)
    aRecord.append(pBalance)
 
    # Insert into the class table at index
    classTable.insert (pIndex, aRecord)
 
def deleteRecord (pIndex):
    del classTable[pIndex]
 
# -----------------------------------------------------------------
# Main program
# -----------------------------------------------------------------
 
showClass()
print ("\n... Appending three records ...")
loadData (384, "Collins", "Ivy", 2010, 15.34)
loadData (405, "Brown", "James", 2011, 18.87)
loadData (410, "Jones", "Karen", 2010, 12.98)
showClass()
print ("\n... Inserting a record at position [1] ...")
insertRecord (813, "Lee", "Charles", 2009, 5.47, 1)
showClass()
print ("\n... Deleting record at position [2] ...")
deleteRecord (2)
showClass()
