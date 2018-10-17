#Rock, Paper, Scissors game (with abstraction)

import random

#Set up our variables
Options = ["Rock","Paper","Scissors","Draw"]
Player1=0
Player2=0

#Abtract pattern selection function, two parameter inputs and one output
def whoWins(p1,p2) :
    Diff = p1-p2
    if Diff == 0 :
        return 3    # represents "Draw" in our list
    elif Diff == -1 or Diff == 2 :
        return p2
    else :
        return p1

#Main program: testing our selection by running 30 Computer vs Computer games
print('Rock-Paper-Scissors Game')
numGames = int(input("How many RPS games do you want: "))
for game in range(1,numGames+1):
    Player1 = random.randint(0,2)
    Player2 = random.randint(0,2)
    print("Game",game,Options[Player1],"vs",Options[Player2],
           "Winner is:",Options[whoWins(Player1,Player2)]) #one line split

    
# Possible extensions:
# - allow user to choose number of games
# - count the number of times each option wins
# - allow user to play against the computer and keep the score
