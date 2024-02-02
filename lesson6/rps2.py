#Improving the RPS_Game

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def loadgame():
    load1 = "*****************************************"
    load3 = "*          ROCK PAPER SCISSORS          *"
    load2 = "*****************************************"

    print(load1)
    print(load3)
    print(load2)
   

def winner():
    load1 = "*****************************************"
    load4 = "*              GAME WINNER              *"
    load2 = "*****************************************"

    print(load1)
    print(load4)
    print(load2)


loadgame()          #LOADING GAME SCREEN..

playagain = True

playerwins = 0
computerwins = 0

while playagain:
    #
    playerchoice = input("Enter.. \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must Enter 1, 2 or 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    #
    print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer Chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
    #


    if player == 1 and computer == 3:
        print("You Win 🎉")
        playerwins += 1
        
    elif player == 2 and computer == 1:
        print("You Win 🎉")
        playerwins += 1

    elif player == 3 and computer == 2:
        print("You Win 🎉")
        playerwins += 1

    elif player == computer:
        print("Tie Game 😮")

    else:
        print("🐍 Python Wins")
        computerwins += 1

    
    playagain = input("\nY -To Continue\nQ -To Quit \n\n")
    if playagain.lower() == "y":
        continue
    else: 
        print("🎉🎉✨✨")

        winner()    #LOADING WINNER SCREEN..
        print(f"Python: {0}", computerwins) if (computerwins > playerwins) else print(f"Player: {0}", playerwins)
    
        playagain = False

sys.exit("Bye Boy 🤣😁😂💔")
