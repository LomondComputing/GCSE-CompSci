# Create a Python program that will output the complete lyrics of the Christmas song
# THE TWELVE DAYS OF CHRISTMAS
# using as few lines of code as possible
# Use the LIST below as the data source for the song
# You may want to define a FUNCTION that outputs the lines for a particular day

gifts = [
    'Partridge in a Pear Tree',
    'Turtle Doves',
    'French Hens',
    'Calling Birds',
    'Gold Rings',
    'Geese a-Laying',
    'Swans a-Swimming',
    'Maids a-Milking',
    'Ladies Dancing',
    'Lords a-Leaping',
    'Pipers Piping',
    'Drummers Drumming'
]

ords = ['first','second','third','fourth','fifth','sixth','seventh','eighth', 'ninth','tenth','eleventh','twelth']
nums = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']

def day(n):
    print('On the %s day of Christmas my true love sent to me' %(ords[n-1]))
    for d in range(n,0,-1):
        if d==1:
            if n>1:
                print('And a %s' %(gifts[d-1]))
            else:
                print('A %s' %(gifts[d-1]))
        else:
            print('%s %s' %(nums[d-1].capitalize(), gifts[d-1]))

# Main program
for d in range(1, len(gifts)+1):
    day(d)
    print('')


    
