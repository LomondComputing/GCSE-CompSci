names = ['Hi','Fy','Di','Ed','Al','Go','Ma','Mi','Ha','Lo']
scores = [900,800,700,600,550,499,450,425,390,123]

print('NAMES =',names)      
print('SCORES =',scores)

player = input('Enter player name: ')  # get name and score
points = int(input('Enter score: '))
print('Thank you',player)
print('You score was',points)

p = 0
while (p < len(names)) and (scores[p] > points):    # find pos to insert at
    p += 1

if p < len(names)-1:    # if not in last place
    for x in range(len(names)-2,p-1,-1):    # then need to move up other scores
        names[x+1] = names[x]
        scores[x+1] = scores[x]

if p <= len(names)-1:       # if they qualify for top ten table
    names[p] = player       # insert them
    scores[p] = points
    print('Well done, you qualify for the Top Ten table in position',p+1)
    print('NAMES =',names)
    print('SCORES =',scores)
else:
    print('Sorry, you do not qualify for the Top Ten table this time')


