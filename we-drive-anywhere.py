days = [100, 700, 600, 700, 800, 1000, 1500]
print('Do you want to enter another day (yes or no)?')
use = input()
while use == 'yes':
    print('Enter day number (Sunday = 0)')
    dayNumber = int(input())
    journeys = days[dayNumber]
    driversNeeded = journeys//60
    partTime = driversNeeded - 3
    print('drivers needed: ',driversNeeded)
    print('part time: ',partTime)
    print('Do you want to enter another day (yes or no)?')
    use = input()

