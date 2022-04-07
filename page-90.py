# -----------------------------------------------------------------
# Global variables
# -----------------------------------------------------------------
widths = [1, 2, 3]              # Dimensions of multiple tanks
heights = [4, 5, 6]
lengths = [7, 8, 9]
index = 0                       # For looping
layout = ""                     # For printing in columns
theArea = 0
 
# -----------------------------------------------------------------
# Subprograms
# -----------------------------------------------------------------
def calcCuboid (pWidth, pHeight, pLength):
 
    wh = 0              # Initialise all variables
    wl = 0
    hl = 0
    area = 0            # Result
 
    wh = pWidth * pHeight       # Calculation of parts
    wl = pWidth * pLength
    hl = pHeight * pLength
    area = 2 * (wh + wl + hl)   # Final calculation
 
    # Alternative, using fewer local variables
    # area = 2 * ((pWidth * pHeight) + (pWidth * pLength) +
    #             (pHeight * pLength))
 
    # Alternative, using no local variables
    # return (2 * ((pWidth * pHeight) + (pWidth * pLength) +
    #              (pHeight * pLength)))
 
    return (area)
 
# -----------------------------------------------------------------
# Main program
# -----------------------------------------------------------------
 
index = 0
print ("Width  Height  Length  SurfaceArea")
layout = "{:^6d}  {:^6d}  {:^6d}  {:^11d}"
while (index < len(widths)):
    theArea = calcCuboid(widths[index],
                         heights[index],
                         lengths[index])
    print (layout.format(widths[index],
                         heights[index],
                         lengths[index],
                         theSurfaceArea))
    index = index + 1
