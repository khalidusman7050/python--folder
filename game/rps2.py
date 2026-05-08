import sys
import random
from enum import Enum

def rps():
    game_count = 0
    
    player_win =0
    python_win =0


    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def play_rps():
        nonlocal player_win
        nonlocal python_win
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
                nonlocal player_win
                nonlocal python_win
                if player == 1 and computer == 3:
                    player_win +=1
                    return 'you win'
                elif player == 2 and computer ==  1:
                    player_win +=1
                    return "you win"
                elif player == 3 and computer ==  2:
                    player_win +=1
                    return "you win"
                elif player == computer:
                    return "Tie game!"
                else:
                    python_win +=1
                    return "python wins!"
                
            game_result =decide_winner(player,computer)
            
            print(game_result)
                
            nonlocal game_count
            game_count += 1
                
            print ("\nGame count: "+ str(game_count))
            print ("\n player wins: "+ str(player_win))
            print ("\n python wins: "+ str(python_win))

            # play again?
            playagain = input("\nPlay again? (y/q): ").lower()
            if playagain == "q":
                print("Thanks for playing!")
                sys.exit()
            elif playagain != "y":
                print("Invalid input, exiting.")
                sys.exit()
    return play_rps

    # start game
play = rps() 

play()