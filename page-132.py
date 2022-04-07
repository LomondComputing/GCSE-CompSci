# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
POSTCODE_MIN = 6            # Constant
POSTCODE_MAX = 8            # Constant
 
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
postCode = ""               # Initialise to empty string
length = 0                  # Invalid length
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
 
postCode = input ("Enter a postcode: ")
length = len(postCode)      # For easier reading
 
if ((length >= POSTCODE_MIN) and (length <=
                                  POSTCODE_MAX)):
    print ("Valid postcode")
else:
    print ("Invalid postcode")
