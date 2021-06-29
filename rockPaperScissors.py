import string
import random

# Cody Wiebe
# RockPaperScissors.py
# Simple rock paper scissors game
# Working on input/output, randomization, while loops and if else



# Uses random number generation to create the computers play
def generatePlay():
    compPlay = random.randint(0,3)
    if(compPlay == 1):
        return 'rock'
    elif(compPlay == 2):
        return 'paper'
    else:
        return 'scissors'

# Determines who won the round
def roundWinner(pPlay, cPlay):
    if(pPlay == cPlay):
        print('We picked the same play. Redo')
        return 0
    elif(pPlay == 'rock' and cPlay == 'scissors'):
        print('I chose scissors. You win that round. Nice job.')
        return 1
    elif(pPlay == 'scissors' and cPlay == 'paper'):
        print('I chose scissors. You win that round. Nice job.')
        return 1
    elif(pPlay == 'paper' and cPlay == 'rock'):
        print('I chose scissors. You win that round. Nice job.')
        return 1
    else:
        print(f'I picked {cPlay} so I win. Better luck next time.')
        return 2

#Basic intro to the game
name = input('What is your name?: ')
print(f'Alright {name} let\'s play a game of rock paper scissors.')
print('The game is best of 5. If you win 3 rounds you win the game.')

# Intitializing the variables needed to determine end of game
gameOver = False
player = 0
comp = 0

# Main bulk of the game running
while(gameOver == False):
    # Gathering the players play and determining if it's valid
    pPlay = input('rock, paper or scissors? :')
    if(pPlay != 'rock' or pPlay != 'paper', pPlay != 'scissors'):
        print('That\'s not a valid play. You lose. Bye')
        exit()
    
    # Generating computers play and who won the round
    cPlay = generatePlay()
    winner = roundWinner(pPlay=pPlay, cPlay= cPlay)

    # Tallying the number of round wins
    if(winner == 1):
        player = player + 1
    elif(winner == 2):
        comp = comp + 1

    # Determining if someone has won
    if(player == 3):
        print('You win! You outplayed me. Congratulations. Bye.')
        gameOver = True
    elif(comp == 3):
        print('I win! Take that. Bye')
        gameOver = True