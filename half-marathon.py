# Half Marathon

import random
numParts = 450
teamSize = 5
numTeams = 450 // teamSize
participants = []
teams = []
teamArray = []

def member(a, l):
    for i in l:
        if i == a:
            return True
    return False

def count(a, l):
    c = 0
    for i in l:
        if i == a:
            c += 1
    return c

# Generate list of valid team names
for t in range(numTeams):
    validTeam = False
    while not validTeam:
        team = chr(random.randint(65,90)) + chr(random.randint(65,90))
        if not member(team,teams):
            validTeam = True
            teams.append(team)

teams.sort()
print("Number of teams:",numTeams)
print("Teams:",teams)

# Generate list of participants
for p in range(numParts):
    validTeam = False
    while not validTeam:
        team = teams[random.randint(0,numTeams-1)]
        if count(team,participants) < 5:
            validTeam = True
            participants.append(team)

# Generate list of TEAM
for t in range(numParts):
    teamArray.append('999')
    
print("Participants:",participants)
print("TEAM\tNUM PARTICIPANTS")
for t in range(numTeams):
    print(teams[t],"\t",count(teams[t],participants))

print("TEAM",teamArray)
    
    
