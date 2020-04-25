import pygame
import random
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
        self.b = [] #will hold the values that determine the colors of each square on the grid
    def draw(self):
        for i in range(0, 30):  #cycle through y
            for k in range(0, 15):   #cycle through x
                if self.b[i][k] == 1:   #if it is piece 1
                    pygame.draw.rect(screen, RED, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 2:   #if it is piece 2
                    pygame.draw.rect(screen, YELLOW, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 3:   #if it is piece 3
                    pygame.draw.rect(screen, GREEN, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 4:   #if it is piece 4
                    pygame.draw.rect(screen, BLUE, (20+k*10, 10+i*10, 10, 10))
                elif self.b[i][k] == 5:   #if it is piece 5
                    pygame.draw.rect(screen, CYAN, (20+k*10, 10+i*10, 10, 10))
                else:   #if it isn't anyof those
                    pygame.draw.rect(screen, BLACK, (20+k*10, 10+i*10, 10, 10))
    #checks whether a line is ready to be cleared
    def check(self):
        #cycle through y
        for i in range(0, 30):
            #start by assuming it is full
            full = True
            #cycle through x
            for k in range(0, 15):
                #if there is an empty spot, change full to false
                if self.b[i][k] == 0:
                    full = False
            #if it is full, remove the line and add a new one to the beginning
            if full == True:
                self.b.pop(i)
                self.b.insert(0, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        #return true or false
        return full
def make_board():
    board = Board()
    board.b = []
    #make the grid
    for i in range(31):
        board.b.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    return board

board = make_board()
#    ----
class Piece1:
    def __init__(self):
        self.x = 0   #x pos on the grid
        self.y = 0   #y pos on the grid
        self.color = RED   #color
        self.rotation = 0   #what rotation it is in
    #changes the rotation value
    def rotate(self):
        if self.rotation == 1:
            self.rotation = 2
        elif self.rotation == 2:
            self.rotation = 1
    #moves the piece across the x-axis the entered amount of times
    def move_x(self, num):
        #check if it will go out of bounds first
        if self.rotation == 1:
            if self.x+num > -1 and self.x+num+3 < 15:
                if num < 0 and board.b[self.y][self.x+num] == 0:
                    self.erase()
                    self.x = self.x+num
                elif num > 0 and board.b[self.y][self.x+num+3] == 0:
                    self.erase()
                    self.x = self.x+num
        else:
            if self.x+num > -1 and self.x+num < 15:
                blocked = False
                for i in range(0, 4):
                    if not(board.b[self.y+i][self.x+num] == 0):
                        blocked = True
                if not(blocked):
                    self.erase()
                    self.x = self.x+num
    #moves the piece across the y-axis the entered amount of times
    def move_y(self, num):
        #check if it will go out of bounds first
        if self.rotation == 1:
            if self.y+num > -1 and self.y+num < 30:
                blocked = False
                for i in range(0, 4):
                    if not(board.b[self.y+num][self.x+i] == 0):
                        blocked = True
                if blocked:
                    return False
                else:
                    self.erase()
                    self.y = self.y+num
                    return True
            else:
                return False
        else:
            if self.y+num > -1 and self.y+num+3 < 30 and board.b[self.y+num+3][self.x] == 0:
                self.erase()
                self.y = self.y+num
                return True
            else:
                return False
    #draws the piece by changing the values in the grid
    def draw(self):
        if self.rotation == 1:
            #for rotation one, its shaped like: ----
            for i in range(0, 4):
                board.b[self.y][self.x+i] = 1
        elif self.rotation == 2:
            #for rotation two, its shaped like: -
                                               #-
                                               #-
                                               #-
            for i in range(0, 4):
                board.b[self.y+i][self.x] = 1
    #used to clear the space the piece is in in order to move it to a different spot
    def erase(self):
        if self.rotation == 1:
            for i in range(0, 4):
                board.b[self.y][self.x+i] = 0
        elif self.rotation == 2:
            for i in range(0, 4):
                board.b[self.y+i][self.x] = 0
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
        if self.x+num > -1 and self.x+num+1 < 15:
            if num < 1 and board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num] == 0:
                self.erase()
                self.x = self.x+num
            elif board.b[self.y][self.x+num+1] == 0 and board.b[self.y+1][self.x+num+1] == 0:
                self.erase()
                self.x = self.x+num
    def move_y(self, num):
        if self.y+num > -1 and self.y+num+1 < 30 and board.b[self.y+num+1][self.x] == 0 and board.b[self.y+num+1][self.x+1] == 0:
            self.erase()
            self.y = self.y+num
            return True
        else:
            return False
    def draw(self):
        board.b[self.y][self.x] = 2
        board.b[self.y][self.x+1] = 2
        board.b[self.y+1][self.x] = 2
        board.b[self.y+1][self.x+1] = 2
    def erase(self):
        board.b[self.y][self.x] = 0
        board.b[self.y][self.x+1] = 0
        board.b[self.y+1][self.x] = 0
        board.b[self.y+1][self.x+1] = 0
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
            if not(self.x == 28):
                self.rotation = 1
    def move_x(self, num):
        if self.rotation == 1:
            if self.x+num > -1 and self.x+num+2 < 15:
                if num < 1 and board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num+1] == 0:
                    self.erase()
                    self.x = self.x+num
                elif board.b[self.y][self.x+num+1] == 0 and board.b[self.y+1][self.x+num+2] == 0:
                    self.erase()
                    self.x = self.x+num
        else:
            if self.x+num > -1 and self.x+num+1 < 15:
                if num < 0:
                    blocked = False
                    if not(board.b[self.y][self.x+num+1] == 0):
                        blocked = True
                    for i in range(1, 3):
                        if not(board.b[self.y+i][self.x+num] == 0):
                            blocked = True
                    if not(blocked):
                        self.erase()
                        self.x = self.x+num
                else:
                    blocked = False
                    for i in range(0, 2):
                        if not(board.b[self.y+i][self.x+num+1] == 0):
                            blocked = True
                    if not(board.b[self.y+2][self.x+num] == 0):
                        blocked = True
                    if not(blocked):
                        self.erase()
                        self.x = self.x+num
    def move_y(self, num):
        if self.rotation == 1:
            if self.y+num > -1 and self.y+num+1 < 30:
                blocked = False
                if not(board.b[self.y+num][self.x] == 0):
                    blocked = True
                for i in range(1, 3):
                    if not(board.b[self.y+num+1][self.x+i] == 0):
                        blocked = True
                if blocked:
                    return False
                else:
                    self.erase()
                    self.y = self.y+num
                    return True
            else:
                return False
        else:
            if self.y+num > -1 and self.y+num+2 < 30 and board.b[self.y+num+2][self.x] == 0 and board.b[self.y+num+1][self.x+1] == 0:
                self.erase()
                self.y = self.y+num
                return True
            else:
                return False
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
    def erase(self):
        if self.rotation == 1:
            board.b[self.y][self.x] = 0
            board.b[self.y][self.x+1] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y+1][self.x+2] = 0
        elif self.rotation == 2:
            board.b[self.y][self.x+1] = 0
            board.b[self.y+1][self.x] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y+2][self.x] = 0
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
            if not(self.x == 28):
                self.rotation = 1
    def move_x(self, num):
        if self.rotation == 1:
            if self.x+num > -1 and self.x+num+2 < 15:
                if num < 1:
                    if board.b[self.y][self.x+num+1] == 0 and board.b[self.y+1][self.x+num] == 0:
                        self.erase()
                        self.x = self.x+num
                elif board.b[self.y][self.x+num+2] == 0 and board.b[self.y+1][self.x+num+1] == 0:
                    self.erase()
                    self.x = self.x+num
        else:
            if self.x+num > -1 and self.x+num+1 < 15:
                if num < 1:
                    if board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num] == 0 and board.b[self.y+2][self.x+num+1] == 0:
                        self.erase()
                        self.x = self.x+num
                elif board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num+1] == 0 and board.b[self.y+2][self.x+num+1] == 0:
                    self.erase()
                    self.x = self.x+num
    def move_y(self, num):
        if self.rotation == 1:
            if self.y+num > -1 and self.y+num+1 < 30:
                blocked = False
                for i in range(0, 2):
                    if not(board.b[self.y+num+1][self.x+i] == 0):
                        blocked = True
                if not(board.b[self.y+num][self.x+2] == 0):
                    blocked = True
                if blocked:
                    return False
                else:
                    self.erase()
                    self.y = self.y+num
                    return True
            else:
                return False
        else:
            if self.y+num > -1 and self.y+num+2 < 30 and board.b[self.y+num+1][self.x] == 0 and board.b[self.y+num+2][self.x+1] == 0:
                self.erase()
                self.y = self.y+num
                return True
            else:
                return False
    def draw(self):
        if self.rotation == 1:
            board.b[self.y][self.x+1] = 4
            board.b[self.y][self.x+2] = 4
            board.b[self.y+1][self.x] = 4
            board.b[self.y+1][self.x+1] = 4
        elif self.rotation == 2:
            board.b[self.y][self.x] = 4
            board.b[self.y+1][self.x] = 4
            board.b[self.y+1][self.x+1] = 4
            board.b[self.y+2][self.x+1] = 4
    def erase(self):
        if self.rotation == 1:
            board.b[self.y][self.x+1] = 0
            board.b[self.y][self.x+2] = 0
            board.b[self.y+1][self.x] = 0
            board.b[self.y+1][self.x+1] = 0
        elif self.rotation == 2:
            board.b[self.y][self.x] = 0
            board.b[self.y+1][self.x] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y+2][self.x+1] = 0
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
        if self.rotation == 1:
            self.rotation = 2
        elif self.rotation == 2 and not(self.x == 28):
            self.rotation = 3
        elif self.rotation == 3:
            self.rotation = 4
        elif self.rotation == 4 and not(self.x == 28):
            self.rotation = 1
    def move_x(self, num):
        if self.rotation == 1:
            if self.x+num > -1 and self.x+num+2 < 15:
                if num < 1:
                    if board.b[self.y][self.x+num+1] == 0 and board.b[self.y+1][self.x+num] == 0:
                        self.erase()
                        self.x = self.x+num
                elif board.b[self.y][self.x+num+1] == 0 and board.b[self.y+1][self.x+num+2] == 0:
                    self.erase()
                    self.x = self.x+num
        elif self.rotation == 2:
            if self.x+num > -1 and self.x+num+1 < 15:
                if num < 1:
                    if board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num] == 0 and board.b[self.y+2][self.x+num] == 0:
                        self.erase()
                        self.x = self.x+num
                elif board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num+1] == 0 and board.b[self.y+2][self.x+num] == 0:
                    self.erase()
                    self.x = self.x+num
        elif self.rotation == 3:
            if self.x+num > -1 and self.x+num+2 < 15:
                if num < 1:
                    if board.b[self.y][self.x+num] == 0 and board.b[self.y+1][self.x+num+1] == 0:
                        self.erase()
                        self.x = self.x+num
                elif board.b[self.y][self.x+num+2] == 0 and board.b[self.y+1][self.x+num+1] == 0:
                    self.erase()
                    self.x = self.x+num
        else:
            if self.x+num > -1 and self.x+num+1 < 15:
                if num < 1:
                    if board.b[self.y][self.x+num+1] == 0 and board.b[self.y+1][self.x+num] == 0 and board.b[self.y+2][self.x+num+1] == 0:
                        self.erase()
                        self.x = self.x+num
                elif board.b[self.y][self.x+num+1] == 0  and board.b[self.y+1][self.x+num+1] == 0 and board.b[self.y+2][self.x+num+1] == 0:
                    self.erase()
                    self.x = self.x+num
    def move_y(self, num):
        if self.rotation == 1:
            if self.y+num > -1 and self.y+num+1 < 30:
                blocked = False
                for i in range(0, 3):
                    if not(board.b[self.y+num+1][self.x+i] == 0):
                        blocked = True
                if blocked:
                    return False
                else:
                    self.erase()
                    self.y = self.y+num
                    return True
            else:
                return False
        elif self.rotation == 2:
            if self.y+num > -1 and self.y+num+2 < 30 and board.b[self.y+num+2][self.x] == 0 and board.b[self.y+num+1][self.x+1] == 0:
                self.erase()
                self.y = self.y+num
                return True
            else:
                return False
        elif self.rotation == 3:
            if self.y+num > -1 and self.y+num+1 < 30:
                blocked = False
                if not(board.b[self.y+num][self.x] == 0):
                    blocked = True
                if not(board.b[self.y+num+1][self.x+1] == 0):
                    blocked = True
                if not(board.b[self.y+num][self.x+2] == 0):
                    blocked = True
                if blocked:
                    return False
                else:
                    self.erase()
                    self.y = self.y+num
                    return True
            else:
                return False
        else:
            if self.y+num > -1 and self.y+num+2 < 30 and board.b[self.y+num+1][self.x] == 0 and board.b[self.y+num+2][self.x+1] == 0:
                self.erase()
                self.y = self.y+num
                return True
            else:
                return False
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
    def erase(self):
        if self.rotation == 1:
            board.b[self.y][self.x+1] = 0
            board.b[self.y+1][self.x] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y+1][self.x+2] = 0
        elif self.rotation == 2:
            board.b[self.y][self.x] = 0
            board.b[self.y+1][self.x] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y+2][self.x] = 0
        elif self.rotation == 3:
            board.b[self.y][self.x] = 0
            board.b[self.y][self.x+1] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y][self.x+2] = 0
        elif self.rotation == 4:
            board.b[self.y][self.x+1] = 0
            board.b[self.y+1][self.x] = 0
            board.b[self.y+1][self.x+1] = 0
            board.b[self.y+2][self.x+1] = 0
def make_piece5(start_x, start_y):
    p = Piece5()
    p.x = start_x
    p.y = start_y
    p.rotation = 1
    return p

def draw_screen(piece):
    pygame.draw.rect(screen, BLACK, (220, 100, 230, 80))
    font = pygame.font.SysFont('Calibri', 25, True, False)
    screen.blit(font.render("NEXT:", True, WHITE), [230, 110])
    if isinstance(piece, Piece1):
        pygame.draw.rect(screen, RED, (295, 140, 80, 20))
    elif isinstance(piece, Piece2):
        pygame.draw.rect(screen, YELLOW, (315, 120, 40, 40))
    elif isinstance(piece, Piece3):
        pygame.draw.rect(screen, GREEN, (305, 120, 40, 20))
        pygame.draw.rect(screen, GREEN, (325, 140, 40, 20))
    elif isinstance(piece, Piece4):
        pygame.draw.rect(screen, BLUE, (325, 120, 40, 20))
        pygame.draw.rect(screen, BLUE, (305, 140, 40, 20))
    elif isinstance(piece, Piece5):
        pygame.draw.rect(screen, CYAN, (325, 120, 20, 20))
        pygame.draw.rect(screen, CYAN, (305, 140, 60, 20))
    
    pygame.draw.rect(screen, BLUE, (220, 220, 70, 30))
    pygame.draw.rect(screen, BLUE, (300, 220, 70, 30))
    pygame.draw.rect(screen, BLUE, (380, 220, 70, 30))
    font = pygame.font.SysFont('Calibri', 28, True, False)
    screen.blit(font.render("LEFT", True, WHITE), [230, 225])
    screen.blit(font.render("RIGHT", True, WHITE), [385, 225])
    font = pygame.font.SysFont('Calibri', 20, True, False)
    screen.blit(font.render("ROTATE", True, WHITE), [308, 228])
    
def choose_piece():
    num = random.randrange(1, 6)
    if num == 1:
        piece = make_piece1(7, 0)
        return piece
    elif num == 2:
        piece = make_piece2(7, 0)
        return piece
    elif num == 3:
        piece = make_piece3(7, 0)
        return piece
    elif num == 4:
        piece = make_piece4(7, 0)
        return piece
    else:
        piece = make_piece5(7, 0)
        return piece
        
#---------------main function---------------

#initialize pygame
pygame.init()
    
#initialize the clock
clock = pygame.time.Clock()
board = make_board()
    
screen.fill(GRAY)
board.draw()
count = 0
next_piece = choose_piece()
current_piece = choose_piece()
    
lines_cleared = 0
done = False
    
while not done:
    #if caption is being used, so will this
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if pygame.mouse.get_pressed()[0]:
            #get the mouse position
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            if mouse_x > 220 and mouse_x < 290 and mouse_y > 220 and mouse_y < 250:
                current_piece.move_x(-1)
            elif mouse_x > 300 and mouse_x < 370 and mouse_y > 220 and mouse_y < 250:
                current_piece.erase()
                current_piece.rotate()
            elif mouse_x > 380 and mouse_x < 450 and mouse_y > 220 and mouse_y <250:
                current_piece.move_x(1)
    end = False
    if lines_cleared == 2:
        screen.fill(BLUE)
        font = pygame.font.SysFont('Calibri', 80, True, False)
        screen.blit(font.render("YOU WON", True, WHITE), [100, 80])
        pygame.draw.rect(screen, PURPLE, (154, 240, 172, 35))#draw the rectangle
        font = pygame.font.SysFont('Calibri', 35, True, False)#change the font
        screen.blit(font.render("CLOSE GAME", True, WHITE), [159, 245])#print "CLOSE GAME" on the rectangle
        pygame.display.flip()
        close = False
        while not close:
            for event in pygame.event.get():
                #---if the mouse is clicked---
                if pygame.mouse.get_pressed()[0]:
                    #get the mouse position
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    #---if it is on the "CLOSE GAME" button---
                    if mouse_x > 154 and mouse_x < 326 and mouse_y > 240 and mouse_y < 275:
                        close = True #end this while loop
                        end = True
    if not(end):
        count = count + 1
        if count == 15:
            count = 0
            if not(current_piece.move_y(1)):
                if board.check():
                    lines_cleared = lines_cleared+1
                current_piece = next_piece
                next_piece = choose_piece()
            
        screen.fill(GRAY)
        current_piece.draw()
        board.draw()
        draw_screen(next_piece)
        pygame.display.flip()
        
        clock.tick(60)
    else:
        pygame.quit()