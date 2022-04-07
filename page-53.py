# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# Test with 1, 22; 1, -2.25; 6, -2.25; 7, 35; 5, 25; 5, 25.5
day = 5                     # Day of the week
temp = 25.5                 # Temperature (real number)
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
if (day >= 1) and (day <=5):
    # Weekday
    if (temp < 20.0) or (temp > 25.0):
        # Adjust temperature
        print ("Weekday - Need to adjust temperature")
elif (day == 6) or (day == 7):
    # Weekend
    if (temp < 15.0) or (temp > 30.0):
        # Adjust temperature
        print ("Weekend - Need to adjust temperature")
