# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
numbers = [2,13,24,35,46,57,68,79,80,91,112]
median = 0
startIndex = 0
endIndex = 0
target = 0
found = False
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
target = 24
startIndex = 0
endIndex = len(numbers) - 1
 
while ((not found) and (startIndex <= endIndex)):
    median = (startIndex + endIndex) // 2   # Integer division
    print (startIndex, endIndex, median)
 
    if (numbers[median] == target):
        found = True
        print ("Found " + str(target) + " at index: " + str(median))
    elif (target < numbers[median]):
        endIndex = median - 1
    else:
        startIndex = median + 1
