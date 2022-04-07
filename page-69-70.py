# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
furniture = []
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
# Worked example 1
print (furniture)               # It's empty
furniture.append ("chair")
furniture.append ("table")
print (furniture)               # It has two items
print (furniture[0])            # This is the first item
print (furniture[1])            # This is the second item
 
# Worked example 2
furniture.append ("stool")
furniture.append ("dresser")
print (furniture)
furniture.insert(0, "bed")
print (furniture)
furniture.insert(3, "sofa")
print (furniture)
 
# Worked example 3
print (furniture)
del furniture[2]
print (furniture)
