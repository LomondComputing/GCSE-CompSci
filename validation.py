def checkingInput():
    while True:
        try:
            a = input('enter')
            if a == 'y' or 1 <= int(a) <= 10:
                return a
            else:
                print('Invalid input!')
        except ValueError:
                  print('Value error! Please try again..')

