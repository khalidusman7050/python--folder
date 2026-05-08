import sys
import random
from enum import Enum

game_count = 0


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    while True:
        playerchoice = input(
            "\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors:\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            continue

        player = int(playerchoice)
        computer = random.randint(1, 3)

        print("You chose:", RPS(player).name)
        print("Python chose:", RPS(computer).name)
        def decide_winner(player,computer):
            if player == computer:
                return"It's a tie."
            elif (player == 1 and computer == 3) or \
                (player == 2 and computer == 1) or \
                (player == 3 and computer == 2):
                return"You win!"
            else:
                return"Python wins!"
            
        game_result =decide_winner(player,computer)
        
        print(game_result)
            
        global game_count
        game_count += 1
            
        print ("\nGame count: "+ str(game_count))

        # play again?
        playagain = input("\nPlay again? (y/q): ").lower()
        if playagain == "q":
            print("Thanks for playing!")
            sys.exit()
        elif playagain != "y":
            print("Invalid input, exiting.")
            sys.exit()

# start game
play_rps()