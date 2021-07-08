import pygame
import time

pygame.font.init()

# The grid of the sudoku
class Grid:
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

    # Initializing the grid
    def __init__(self, rows, cols, width, height, win):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.win = win
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.selected = None

    #Drawing out the lines of the grid, eventually will draw the numbers/blanks/corner numbers in
    def draw(self):
        #Drawing out sudoku lines, darker lines work to denote the boxes
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.win, (0, 0, 0), (50 + i*(self.width/self.rows),50), 
                                    (50 + i*(self.width/self.rows), self.height + 50), 4)
                pygame.draw.line(self.win, (0, 0, 0), (50, 50 + i*(self.height/self.cols)), 
                                    (self.width + 50, 50 + i*(self.height/self.cols)), 4)
            else:
                pygame.draw.line(self.win, (100, 100, 100), (50 + i*(self.width/self.rows),50), 
                                    (50 + i*(self.width/self.rows), self.height + 50), 4)
                pygame.draw.line(self.win, (100, 100, 100), (50, 50 + i*(self.height/self.cols)), 
                                    (self.width + 50, 50 + i*(self.height/self.cols)), 4)

        for i in range(0 ,self.rows):
            for j in range(0, self.cols):
                self.cubes[i][j].draw(self.win)



class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
    
    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5 + 50, y+5 + 50))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2) + 50, y + (gap/2 - text.get_height()/2) + 50))

    def draw_change(self, win, g = True):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap/2 - text.get_width()/2) + 50, y + (gap/2 - text.get_height()/2) + 50))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, temp):
        self.temp = temp

def main():

    screen = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 500, 500, screen)

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  

        screen.fill((255, 255, 255))
        board.draw()
        # pygame.draw.line(screen, (0, 0, 0), (50,50), (50, 450), 4)

        pygame.display.flip()

    pygame.quit()

main()

