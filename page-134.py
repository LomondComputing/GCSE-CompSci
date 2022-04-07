1	# ------------------------------------------------------------
2	# Global variables
3	# ------------------------------------------------------------
4	allForms = ["7AXB", "7PBD", "7ARL", "7JEH"]
5	userForm = ""           # User types in
6	validForm = False
7	 
8	# ------------------------------------------------------------
9	# Subprograms
10	# ------------------------------------------------------------
11	def isValidForm (pForm):
12	    valid = False           # Always assume invalid
13	    index = 0
14	 
15	    # Keep looping until found or run out of options
16	    while (not valid) and (index < len(allForms)):
17	        if (pForm == allForms[index]):
18	            valid = True        # Found it
19	        index = index + 1       # Increment
20	 
21	    return (valid)          # Tell caller
22	 
23	# ------------------------------------------------------------
24	# Main program
25	# ------------------------------------------------------------
26	userForm = input ("Enter a user form: ")
27	userForm = userForm.upper()             # Easier to work with
28	 
29	validForm = isValidForm (userForm)      # Call look up
30	if (not validForm):
31	    print ("The form you entered does not exist.")
32	else:
33	    print ("The form you entered is valid.")
Worked example – Page 135
1	# --------------------------------------------------------------
2	# Global variables
3	# --------------------------------------------------------------
4	validChoice = False            # Assume everything is invalid
5	userChoice = 0                 # Set to an invalid value
6	 
7	# --------------------------------------------------------------
8	# Subprograms
9	# --------------------------------------------------------------
10	def showMenu():
11	    print ("Option 1: Find the highest value")
12	    print ("Option 2: Find the lowest value")
13	    print ("Option 3: Calculate the average")
14	 
15	# --------------------------------------------------------------
16	# Main program
17	# --------------------------------------------------------------
18	 
19	while (not validChoice):
20	    showMenu()
21	    userChoice = int (input ("Enter an option: "))
22	    if (userChoice >= 1) and (userChoice <= 3):
23	        validChoice = True
24	    else:
25	        print ("Invalid option, try again ")
26	 
27	print ("You entered option " + str(userChoice))
