import sys
import random
from enum import Enum

class rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
 
    
print("")

playerchoice = input("Enter...\n1 forRock, \n2 for Paper, \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Invalid choice. Please enter 1, 2, or 3.")
    
computerchoice = random.choice("123")
computer = int(computerchoice)
print("you chose: " +str(rps(player)).replace('rps.', '') + ".")
print("python chose: " + str(rps(computer)).replace('rps.', '') + ".")

print("")

if player == 1 and computer == 3:
    print("you win.")
elif player == 2 and computer == 1:
    print("you win.")
elif player == 3 and computer == 2:
    print("you win.")
elif player == computer:
    print("it's a tie.")
else:
    print("python wins.")