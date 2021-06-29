import string
import random

# Cody Wiebe
# RockPaperScissors.py
# Simple rock paper scissors game
# Working on input/output, randomization, while loops and if else
# Same thing as the other rps except this one the player can't win

# Determines who won the round
def roundWinner(pPlay):
    if(pPlay == 'rock'):
        print('I picked paper so I won that round. Better luck next time.')
        return 2
    elif(pPlay == 'scissors'):
        print('I picked rock so I won that round. Better luck next time.')
        return 2
    elif(pPlay == 'paper'):
        print('I picked scissors so I won that round. Better luck next time.')
        return 2

#Basic intro to the game
name = input('What is your name?: ')
print(f'\nAlright {name} let\'s play a game of rock paper scissors.')
print('The game is best of 5. If you win 3 rounds you win the game.\n')

# Intitializing the variables needed to determine end of game
gameOver = False
player = 0
comp = 0

# Main bulk of the game running
while(gameOver == False):
    # Gathering the players play and determining if it's valid
    pPlay = input('rock, paper or scissors?: ')
    if(pPlay != 'rock' and pPlay != 'paper' and pPlay != 'scissors'):
        print('\nThat\'s not a valid play. You lose. Bye')
        exit()
    
    # Generating computers play and who won the round
    winner = roundWinner(pPlay=pPlay)

    # Tallying the number of round wins
    if(winner == 1):
        player = player + 1
    elif(winner == 2):
        comp = comp + 1

    # Determining if someone has won
    if(player == 3):
        print('\nYou win! You outplayed me. Congratulations. Bye.')
        gameOver = True
    elif(comp == 3):
        print('\nI win! Take that. Bye')
        gameOver = True