# Program to input and validate: name, age & e-mail

# Boolean flag to control main acceptance loop
accept = False
while not accept:   # Main acceptance loop
    # Flags for three data items - assume all are False to begin with
    validName = False
    validAge = False
    validEmail = False
    
    # Validate name
    while not validName:
        print('Please enter the data requested ...')
        name = input('Please enter your full name: ')
        print('You entered the name %s' % (name))
        
        # Check for valid length
        if 3 <= len(name) <= 20:
            print('This name has a valid length')
            validLength = True
        else:
            print('ERROR: Name must be between 3 and 20 characters')
            validLength = False
            
        # Check for valid characters
        validChars = True       # Assume characters to be valid at start
        charPos = 0
        while validChars and charPos < len(name):
            char = name[charPos].lower()    # Get lower case version of current character
            if char < 'a' or char >'z':
                print('ERROR: Name can only contain characters a-z and A-Z')
                validChars = False          # Stop loop when we find first invalid char
            charPos += 1

        # Check if name is valid overall
        if validLength and validChars: 
            print('This is a valid name')
            validName = True
        else:
           print('ERROR: This is not a valid name.  Please re-enter')               

    # Validate age
    while not validAge:
        age = input('Please enter your age in years: ')
        print('You entered the age %s' % (age))

        # Try to convert string input to integer
        try:
            age = int(age)
        except ValueError:
            print('ERROR: age must be an integer value')
            validInt = False
        else:
            print('This age is an integer')
            validInt = True

        # Check age is in valid range, but only if it's an integer
        if validInt:
            if 1 <= age <= 120:
                print('This age is in a valid range')
                validRange = True
            else:
                print('ERROR: This age is not in a valid range')
                validRange = False

        # Check if age is valid overall
        if validInt and validRange:
            print('This is a valid age')
            validAge = True
        else:
            print('ERROR: This is not a valid age. Please re-enter')
            
    # Validate E-mail
    while not validEmail:
        email = input('Please enter your e-mail address: ')
        print('You entered the e-mail %s' % (email))

        # Start checks only is something has been entered...
        if len(email) > 0:

            # Check it contains exactly one @
            if email.count('@') == 1:
                print('This e-mail contains one @')
                oneAt = True
            else:
                print('ERROR: This e-mail does not contain one @')
                oneAt = False

            # Check does not start with @
            if email[0] != '@':
                print('This e-mail does not start with @')
                startAt = True
            else:
                print('ERROR: This e-mail starts with @')
                startAt = False

            # Check contains a dot after the @, but only if there is one @
            if startAt:
                if email.count('.') == 0 or email.find('.') < email.find('@'):
                    print('ERROR: This e-mail does not contain a . after the @')
                    dot = False
                else:
                    print('This e-mail contains a . after the @')
                    dot = True

            # Check if e-mail is valid overall
            if oneAt and startAt and dot:
                print('This is a valid e-mail address')
                validEmail = True
            else:
                print('ERROR: This is not a valid e-mail address. Please re-enter')
        else:
            print('ERROR: This e-mail is empty!')

    # Print summary of data
    print('\nHere is the data you entered:')
    print('Name: %s' % (name))
    print('Age: %s'  % (age))
    print('E-mail: %s' % (email))

    # Get a valid response for acceptance
    validResponse = False
    while not validResponse:
        response = input('\nAre you happy with this data? ')
        if response.lower() in ['y','yes','n','no']:
            validResponse = True
        else:
            print('Please enter one of y, Y, Yes, n, N, No')

    # Check if data has been accepted       
    if response.lower() in ['y','yes']:
        accept = True
        print('Thank you, goodbye')
        
    
            
    
