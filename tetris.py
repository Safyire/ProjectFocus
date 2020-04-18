import pygame
#import random
#import time

#---------------colors---------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

#---------------set up the screen---------------
size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)
#pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption("caption")

#---------------classes and functions go here---------------
#board
class Board:
    def __init__(self):
        self.b = []
    def draw(self):
        for i in range(0, 30):
            for k in range(0, 15):
                if self.b[i][k] == 1:
                    pygame.draw.rect(screen, RED, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 2:
                    pygame.draw.rect(screen, YELLOW, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 3:
                    pygame.draw.rect(screen, GREEN, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 4:
                    pygame.draw.rect(screen, BLUE, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 5:
                    pygame.draw.rect(screen, CYAN, (20+k*10, 10+i*10, 10, 10))
                else:
                    pygame.draw.rect(screen, BLACK, (20+k*10, 10+i*10, 10, 10))
                    
def make_board():
    board = Board()
    board.b = []
    for i in range(31):
        board.b.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    return board

#    ----
class Piece1:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = RED
        self.rotation = 0
    def rotate(self):
        if self.rotation == 1:
            self.rotation = 2
        elif self.rotation == 2:
            self.rotation = 1
    def move_x(self, num):
        self.x = self.x+num
    def move_y(self, num):
        self.y = self.y+num
    def draw(self):
        if self.rotation == 1:
            for i in range(0, 4):
                board.b[self.y][self.x+i] = 1
        if self.rotation == 2:
            for i in range(0, 4):
                board.b[self.y+i][self.x] = 1
def make_piece1(start_x, start_y):
    p = Piece1()
    p.x = start_x
    p.y = start_y
    p.rotation = 1
    return p
    
#    --
#    --
class Piece2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = YELLOW
        self.rotation = 1
    def rotate(self):
        #can't rotate, but this command is needed in every piece
        self.rotation = 1
    def move_x(self, num):
        self.x = self.x+num
    def move_y(self, num):
        self.y = self.y+num
    def draw(self):
        for i in range(0, 2):
            board.b[self.y][self.x+i]
            board.b[self.y+i, self.x]
def make_piece2(start_x, start_y):
    p = Piece2()
    p.x = start_x
    p.y = start_y
    p.rotation = 1
    return p

#    --
#     --
class Piece3:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = GREEN
        self.rotation = 0
    def rotate(self):
        if self.rotation == 1:
            self.rotation = 2
        elif self.rotation == 2:
            self.rotation = 1
    def move_x(self, num):
        self.x = self.x+num
    def move_y(self, num):
        self.y = self.y+num
    def draw(self):
        if self.rotation == 1:
            board.b[self.y][self.x] = 3
            board.b[self.y][self.x+1] = 3
            board.b[self.y+1][self.x+1] = 3
            board.b[self.y+1][self.x+2] = 3
        elif self.rotation == 2:
            board.b[self.y][self.x+1] = 3
            board.b[self.y+1][self.x] = 3
            board.b[self.y+1][self.x+1] = 3
            board.b[self.y+2][self.x] = 3
def make_piece3(start_x, start_y):
    p = Piece3()
    p.x = start_x
    p.y = start_y
    p.rotation = 1
    return p

#     --
#    --
class Piece4:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = BLUE
        self.rotation = 0
    def rotate(self):
        if self.rotation == 1:
            self.rotation = 2
        elif self.rotation == 2:
            self.rotation = 1
    def move_x(self, num):
        self.x = self.x+num
    def move_y(self, num):
        self.y = self.y+num
    def draw(self):
        if self.rotation == 1:
            board.b[self.y][self.x+1] = 4
            board.b[self.y][self.x+2] = 4
            board.b[self.y+1][self.x] = 4
            board.b[self.y+1][self.x+1] = 4
        elif self.roatation == 2:
            board.b[self.y][self.x] = 4
            board.b[self.y+1][self.x] = 4
            board.b[self.y+1][self.x+1] = 4
            board.b[self.y+2][self.x+1] = 4
def make_piece4(start_x, start_y):
    p = Piece4()
    p.x = start_x
    p.y = start_y
    p.rotation = 1
    return p

#     -
#    ---
class Piece5:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = CYAN
        self.rotation = 0
    def rotate(self):
        if not(self.rotation == 4):
            self.rotation = self.rotation+1
        else:
            self.rotation = 1
    def move_x(self, num):
        self.x = self.x+num
    def move_y(self, num):
        self.y = self.y+num
    def draw(self):
        if self.rotation == 1:
            board.b[self.y][self.x+1] = 5
            board.b[self.y+1][self.x] = 5
            board.b[self.y+1][self.x+1] = 5
            board.b[self.y+1][self.x+2] = 5
        elif self.rotation == 2:
            board.b[self.y][self.x] = 5
            board.b[self.y+1][self.x] = 5
            board.b[self.y+1][self.x+1] = 5
            board.b[self.y+2][self.x] = 5
        elif self.rotation == 3:
            board.b[self.y][self.x] = 5
            board.b[self.y][self.x+1] = 5
            board.b[self.y+1][self.x+1] = 5
            board.b[self.y][self.x+2] = 5
        elif self.rotation == 4:
            board.b[self.y][self.x+1] = 5
            board.b[self.y+1][self.x] = 5
            board.b[self.y+1][self.x+1] = 5
            board.b[self.y+2][self.x+1] = 5
def make_piece5(start_x, start_y):
    p = Piece5()
    p.x = start_x
    p.y = start_y
    p.rotation = 1
    return p

def draw_screen():
    pygame.draw.rect(screen, RED, (220, 30, 30, 10))
    pygame.draw.rect(screen, RED, (230, 40, 10, 30))
    
    pygame.draw.rect(screen, YELLOW, (260, 30, 10, 40))
    pygame.draw.rect(screen, YELLOW, (270, 30, 20, 10))
    pygame.draw.rect(screen, YELLOW, (270, 45, 20, 10))
    pygame.draw.rect(screen, YELLOW, (270, 60, 20, 10))
    
    pygame.draw.rect(screen, GREEN, (300, 30, 30, 10))
    pygame.draw.rect(screen, GREEN, (310, 40, 10, 30))
    
    pygame.draw.rect(screen, BLUE, (340, 30, 10, 40))
    pygame.draw.rect(screen, BLUE, (350, 30, 20, 10))
    pygame.draw.rect(screen, BLUE, (360, 40, 10, 5))
    pygame.draw.rect(screen, BLUE, (350, 45, 20, 10))
    pygame.draw.polygon(screen, BLUE, [(340, 45), (350, 45), (370, 70), (360, 70)])
    
    pygame.draw.rect(screen, CYAN, (380, 30, 30, 10))
    pygame.draw.rect(screen, CYAN, (390, 40, 10, 20))
    pygame.draw.rect(screen, CYAN, (380, 60, 30, 10))
    
    pygame.draw.rect(screen, PURPLE, (420, 30, 30, 10))
    pygame.draw.rect(screen, PURPLE, (420, 40, 10, 5))
    pygame.draw.rect(screen, PURPLE, (420, 45, 30, 10))
    pygame.draw.rect(screen, PURPLE, (440, 55, 10, 5))
    pygame.draw.rect(screen, PURPLE, (420, 60, 30, 10))
    
    pygame.draw.rect(screen, BLACK, (220, 100, 230, 80))
    font = pygame.font.SysFont('Calibri', 25, True, False)
    screen.blit(font.render("NEXT:", True, WHITE), [230, 110])
    
    pygame.draw.rect(screen, BLUE, (220, 220, 70, 30))
    pygame.draw.rect(screen, BLUE, (300, 220, 70, 30))
    pygame.draw.rect(screen, BLUE, (380, 220, 70, 30))
    font = pygame.font.SysFont('Calibri', 28, True, False)
    screen.blit(font.render("LEFT", True, WHITE), [230, 225])
    screen.blit(font.render("RIGHT", True, WHITE), [385, 225])
    font = pygame.font.SysFont('Calibri', 20, True, False)
    screen.blit(font.render("ROTATE", True, WHITE), [308, 228])
    
#---------------main function---------------
def main():
    #initialize pygame
    pygame.init()
    
    #initialize the clock
    clock = pygame.time.Clock()
    board = make_board()
    
    screen.fill(GRAY)
    board.draw()
    
    lines_cleared = 0
    done = False
    
    while not done:
        #if caption is being used, so will this
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(GRAY)
        board.draw()
        draw_screen()
        clock.tick(60)
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()