# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
userName = ""              # Initialise to empty string
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
userName = input ("Enter your name: ")
while (userName == ""):
    userName = input ("Enter your name: ")
print ("Your name is: ", userName)
