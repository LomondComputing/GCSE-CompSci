# Function to find the day number of any date in the year

def countDays(day, month, year):
    if year % 4 == 0:
        leap = True
    else:
        leap = False

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    dayNum = 0

    if month == 1:
        dayNum = day
    else:
        for m in range(0,month-1):
            if m == 1 and leap:
                dayNum += days[m]+1  # add on one for a leap year
            else:
                dayNum += days[m]    # add on days for that month
                
        dayNum = dayNum + day   # add on day of current month
        
    return dayNum
