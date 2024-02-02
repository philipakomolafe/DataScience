#Welcome to RPS.....
import sys
import random
from enum import Enum

load1 = "*****************************************"
load2 = "*                                       *"
load3 = "*          ROCK PAPER SCISSORS          *"

print(" ")
print(load1)
print(load2)
print(load3)
print(load2)
print(load1)

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerchoice = input("Enter.. \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must Enter 1, 2 or 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer Chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")


if player == 1 and computer == 3:
    print("You Win 🎉")

elif player == 2 and computer == 1:
    print("You Win 🎉")

elif player == 3 and computer == 2:
    print("You Win 🎉")

elif player == computer:
    print("Tie Game 😮")

else:
    print("🐍 Python Wins")
        


#create folder
#youtube channel 



