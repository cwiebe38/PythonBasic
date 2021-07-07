# Cody Wiebe
# sudokuSimple.py
# simple text version of a sudoku solver
# Uses the source code from the Github repo https://github.com/techwithtim/Sudoku-GUI-Solver/blob/master/solver%20(text).py
# Also uses partial direction from the video https://www.youtube.com/watch?v=jl5yUEdekEM&t=328s

# Finds the next unsolved box in the puzzle
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if(bo[i][j] == 0):
                return(i, j)
    return None

# Returns if the given move is valid
def valid(bo, pos, num):
    # Checking the column
    for i in range(len(bo)):
        if bo[pos[0]][i] == num:
            return False
    
    # Checking the row
    for j in range(len(bo[0])):
        if bo[j][pos[1]] == num:
            return False
    
    rbox = pos[0]//3
    cbox = pos[1]//3

    # Checking the box
    for i in range(rbox*3, rbox*3 + 3):
        for j in range(cbox*3, cbox*3 + 3):
            if(bo[i][j] == num and i != pos[0] and j != pos[1]):
                print(str(i) + ' ' + str(j))
                return False

    
    return True

# Solving the sudoku using backtracking
def solver(bo):
    
    # Checking if there are empty cells in the puzzle
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    # Go through the array and fill in numbers that work
    # If a number doesn't work then yo backtrack until you can refill
    # the numbers in a manner that it can work
    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i
        
        if solver(bo):
            return True

        bo[row][col] = 0

    return False

    
    


# Prints the board
def print_board(bo):
    for i in range(len(bo)):
        if(i%3 == 0):
            print('- - - - - - - - - - - -')
        for j in range(len(bo[0])):
            if(j%3 == 0 and j != 8):
                print('| ' + str(bo[i][j]) + ' ', end = '')
            elif(j == 8):
                print(str(bo[i][j]) + ' |')
            else:
                print(str(bo[i][j]) + ' ', end='')

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

print_board(board)
print('Now we bout to solve this jaunt')
solver(board)
print_board(board)

# pos = [0, 2]

# if valid(board,pos, 5):
#    print('This jaunt passed')
# else:
#    print('This jaunt ain\'t not passed')

