# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
FORM_LEN = 4            # Constants for name length
 
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
formName = ""               # User types
valid = False               # Assume everything is invalid
 
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
while (not valid):
    formName = input ("Enter a form name: ")
    if (len(formName) == FORM_LEN):        # Length is good
        if (formName.isalnum()):   # Letters and digits only
            # Check first character is 7, 8, or 9
            if ((formName[0] == "7") or
                (formName[0] == "8") or
                (formName[0] == "9")):
                # Good first char, check remaining three
                if (formName[1].isalpha() and
                    formName[2].isalpha() and
                    formName[3].isalpha()):
                    valid = True
                    print ("Your entry is valid.", formName)
                else:
                    print ("Last three characters must be letters")
            else:
                print ("First character must be 7, 8, or 9")
        else:
            print ("Your entry is not valid")
    else:
        print ("Form name is not correct length")
