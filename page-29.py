# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
myName = ""             # Empty string
heightMeters = 99.0     # Invalid height
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
print ("This demonstrates the use of the input() function.")
myName = input ("Please type your name and press the enter key. ")
heightMeters = float(input("Please enter your height in meters. "))
print (myName, "is", heightMeters, "meters tall.")
