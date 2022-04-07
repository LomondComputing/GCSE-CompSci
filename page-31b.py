# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
theWelcome = "Welcome to my program"
thePlayer = ""                          # Empty string
newMessage = ""                         # Holds concatenated message
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
thePlayer = input(
    "What is your name? ")
newMessage = theWelcome + " " + \
             thePlayer
print (newMessage)
