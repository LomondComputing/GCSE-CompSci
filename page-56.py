# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numStudents = 0             # Number of students
numTests = 0                # Number of tests per student
countStudents = 0           # Used to count outside loop
countTests = 0              # Used to count inside loop
studentTest = 0             # Score on a test
studentTotal = 0            # Total of test for a student
studentAverage = 0.0        # Average score for a student
 
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
 
numStudents = int (input ("How many students do you have? "))
numTests = int (input ("How many tests per student? "))
 
# Loop for all the students
while (countStudents < numStudents):
    print ("Working with student number: " + str (countStudents + 1))
 
    # Loop for all tests for a single student
    countTests = 0                  # Reset for each student
    studentTotal = 0
    while (countTests < numTests):
        studentTest = int (input ("Enter a test score "))
        studentTotal = studentTotal + studentTest       # Run the sum
        countTests = countTests + 1                     # One more test seen
 
    # Calculate and print average, rounded to a whole integer
    studentAverage = studentTotal / numTests
    print ("The average for " + str(countStudents + 1) + " is " +
           str(int(round(studentAverage,0))))
 
    countStudents = countStudents + 1       # One more student seen
 
print ("Goodbye")
