# Temperature conversion program

def menu():
    print('Yemperature Conversion Menu')
    print('1 Celsius to Fahrenheit')
    print('2 Fahrenheit to Celsium')
    print('3 Quit')
    option = int(input('Which option? '))
    return option

def CtoF(c):
    print('CtoF')
    return c*(9/5)+32

def FtoC(f):
    print('FtoC')
    return (f-32)*5/9

# Main program

option = menu()

while option != 3:
    if option == 1:
        c = int(input('Enter temp in Celsius'))
        f = CtoF(c)
        print(c,'degrees Celsius = ',f,'degrees Fahreinheit')
    elif option == 2:
        f = int(input('Enter temp in Fahrenheit'))
        c = FtoC(f)
        print(f,'degrees Fahrenheit = ',c,'degrees Celsius')        
    if option != 3:
        option = menu()

print('Thank you for using this program... goodbye!')


