import random

def displayScores(s):
    print('\tPOS\tPLAYER\tSCORE')
    for p in s:
        print('\t',s.index(p)+1,'\t',p[0],'\t',p[1])


names = ['Hi','Fy','Di','Ed','Al','Go','Ma','Mi','Ha','Lo']
numScores = len(names)

points = []
for p in range(numScores):
    points.append(random.randint(100,1000))
points.sort()
    
scores = []
for s in range(numScores):
    scores.append((names[s],points[numScores-1-s]))
      
displayScores(scores)

player = input('Enter player name: ')  # get name and score
points = int(input('Enter score: '))
print('Thank you',player)
print('You score was',points)

length = len(scores)

p = 0
while p < length and scores[p][1] > points:    # find pos to insert at
    p += 1

if p < length-1:    # if not in last place
    for x in range(length-2,p-1,-1):    # then need to move up other scores
        scores[x+1] = scores[x]

if p <= length-1:       # if they qualify for top ten table       
    scores[p] = (player,points)  # insert them
    print('Well done, you qualify for the Top Ten table in position',p+1)
    displayScores(scores)
else:
    print('Sorry, you do not qualify for the Top Ten table this time')


