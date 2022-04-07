1	# --------------------------------------------------------------
2	# Constants
3	# --------------------------------------------------------------
4	MAXTRIES = 3                    # Only three tries allowed
5	 
6	# --------------------------------------------------------------
7	# Global variables
8	# --------------------------------------------------------------
9	userTable = [["ABC123", "ABC"], ["DEF456", "456"],
10	             ["GHI789", "GHI"], ["JKL012", "012"],
11	             ["MNO345", "345"], ["PQR678", "PQR"],
12	             ["STU901", "901"], ["VWX234", "VWX"]]
13	 
14	# --------------------------------------------------------------
15	# Subprograms
16	# --------------------------------------------------------------
17	def findPair (pUser, pPass):
18	    found = False                     # Don't let anyone in
19	    index = 0
20	    length= 0
21	 
22	    length = len (userTable)          # Max records to look at
23	 
24	    # Look at all records until found or no more records
25	    while ((not found) and (index < length)):
26	        # Check name match
27	        if (userTable[index][0] == pUser):
28	            # Check password match
29	            if (userTable[index][1] == pPass):
30	                found = True
31	        index = index + 1
32	 
33	    return (found)
34	 
35	def authenticate ():
36	    valid = False                   # Everything is invalid
37	    tries = 0                       # Current try count
38	    userName = ""
39	    password = ""
40	 
41	    while ((not valid) and (tries < MAXTRIES)):
42	        userName = input ("Enter your username: ")
43	        password = input ("Enter your password: ")
44	        if (not findPair (userName, password)):
45	            tries = tries + 1
46	            print ("Invalid login.  You have " +
47	                   str(MAXTRIES - tries) + " left.")
48	        else:
49	            valid = True                        # It's a match
50	 
51	    return (valid)
52	 
53	# --------------------------------------------------------------
54	# Main program
55	# --------------------------------------------------------------
56	 
57	if (authenticate ()):       # Call to check username and password
58	    print ("Welcome to the system.")

