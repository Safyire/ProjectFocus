import pygame
import random
#import time

#---------------colors---------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

R_COLOR = (50, 50, 50)
G_COLOR = (68, 180, 0)
W_COLOR = (25, 178, 255)

#---------------set up the screen---------------
size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)
pygame.display.set_mode(size, pygame.NOFRAME)
#pygame.display.set_caption("crossy road")

#---------------classes and functions go here---------------
#-----car-----
class Car:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
    def draw(self):
        pygame.draw.rect(screen, PURPLE, [self.x_pos, self.y_pos*40, 70, 40])
    def change_x(self, amount):
        self.x_pos = self.x_pos + amount
        if self.x_pos > 480:
            self.x_pos = -70
    def change_y(self, new_y):
        self.y_pos = new_y
def make_car(x, y):
    car = Car()
    car.x_pos = x
    car.y_pos = y
    return car

#-----road-----
class Road:
    def __init__(self):
        self.pos = 0
        self.car = 0
    def draw(self):
        pygame.draw.rect(screen, R_COLOR, [0, self.pos*40, 480, 40])
        self.car.draw()
    def change_pos(self, new_pos):
        self.pos = new_pos
        self.car.change_y(new_pos)
    def get_pos(self):
        return self.pos
def make_road(position):
    road = Road()
    road.pos = position
    road.car = make_car(0, position)
    return road

#-----grass-----
class Grass:
    def __init__ (self):
        self.pos = 0
    def draw(self):
        pygame.draw.rect(screen, G_COLOR, [0, self.pos*40, 480, 40])
    def change_pos(self, new_pos):
        self.pos = new_pos
    def get_pos(self):
        return self.pos
def make_grass(position):
    grass = Grass()
    grass.pos = position
    return grass

#-----lilypad-----
class Lilypad:
    def __init__(self):
        self.y_pos = 0
        self.x_pos = 0
    def draw(self):
        pygame.draw.rect(screen, GREEN, [20+self.x_pos*40, self.y_pos*40, 40, 40])
    def change_y(self, new_y):
        self.y_pos = new_y
def make_lily(y):
    lily = Lilypad()
    lily.y_pos = y
    lily.x_pos = random.randrange(0, 11)
    return lily

#-----water-----
class Water:
    def __init__(self):
        self.pos = 0
        self.lily1 = 0
        self.lily2 = 0
    def draw(self):
        pygame.draw.rect(screen, W_COLOR, [0, self.pos*40, 480, 40])
        self.lily1.draw()
        self.lily2.draw()
    def change_pos(self, new_pos):
        self.pos = new_pos
        self.lily1.change_y(new_pos)
        self.lily2.change_y(new_pos)
    def get_pos(self):
        return self.pos
def make_water(position):
    water = Water()
    water.pos = position
    water.lily1 = make_lily(position)
    water.lily2 = make_lily(position)
    return water

#-----player-----
class Player:
    def __init__(self):
        self.pos = 5
    def draw(self):
        pygame.draw.rect(screen, RED, [20+self.pos*40, 280, 40, 40])
        pygame.draw.circle(screen, BLACK, [30+self.pos*40, 300], 3)
        pygame.draw.circle(screen, BLACK, [50+self.pos*40, 300], 3)
    def get_pos(self):
        return self.pos
    def left(self):
        if self.pos > 0:
            self.pos = self.pos-1
    def right(self):
        if self.pos < 10:
            self.pos = self.pos+1
def make_player(position):
    player = Player()
    player.pos = position
    return player

#-----controls-----
def draw_controls():
    pygame.draw.rect(screen, RED, [395, 0, 50, 20])
    pygame.draw.rect(screen, RED, [365, 21, 30, 20])
    pygame.draw.rect(screen, RED, [445, 21, 35, 20])
    font = pygame.font.SysFont('Calibri', 20, True, False)
    screen.blit(font.render("forward", True, WHITE), [397, 2])
    screen.blit(font.render("left", True, WHITE), [369.5, 23])
    screen.blit(font.render("right", True, WHITE), [447, 23])

#---------------main function---------------
def main():
    #initialize pygame
    pygame.init()
    
    #initialize the clock
    clock = pygame.time.Clock()
    
    p1 = make_player(5)
    
    board = []
    for i in range(7):
        num = random.randrange(1, 4)
        if num == 1:
            board.append(make_road(i))
        elif num == 2:
            board.append(make_grass(i))
        elif num == 3:
            if not(i == 0):
                if isinstance(board[i-1], Water):
                    board.append(make_grass(i))
                else:
                    board.append(make_water(i))
            else:
                board.append(make_water(i))
    board.append(make_grass(7))
    
    screen.fill(BLUE)
    
    counter = 0
    died = False
    won = False
    done = False
    
    for place in board:
            place.draw()
    p1.draw()
    draw_controls()
    
    while not done:
        for place in board:
            if isinstance(place, Road):
                place.car.change_x(1)
                if place.pos == 7 and place.car.x_pos + 70 > 20+p1.pos*40 and place.car.x_pos < 60+p1.pos*40:
                    died = True
                    done = True
        if isinstance(board[7], Water):
            if not(p1.pos == board[7].lily1.x_pos or p1.pos == board[7].lily2.x_pos):
                died = True
                done = True
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                #get the mouse position
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                if mouse_x > 395 and mouse_x < 445 and mouse_y > 0 and mouse_y < 20:
                    temp = board[7]
                    for i in range (7, 0, -1):
                        board[i] = board[i-1]
                        board[i].change_pos(i)
                    board[0] = temp
                    board[0].change_pos(0)
                    if not(died == True):
                        counter = counter + 1
                        if counter == 25:
                            won = True
                            done = True
                elif mouse_x > 365 and mouse_x < 395 and mouse_y > 21 and mouse_y < 41:
                    p1.left()
                elif mouse_x > 445 and mouse_x < 480 and mouse_y > 21 and mouse_y < 41:
                    p1.right()
        for place in board:
            place.draw()
        p1.draw()
        draw_controls()
        
        clock.tick(60)
        pygame.display.flip()
   
   
    font = pygame.font.SysFont('Calibri', 80, True, False)
    screen.fill(BLUE)
    if died == True:
        screen.blit(font.render("YOU LOST", True, WHITE), [100, 80])
    elif won == True:
        screen.blit(font.render("YOU WON", True, WHITE), [100, 80])
    #---draw the close game button---
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
                    done = True #end the while loop controlling the game
        
    pygame.quit()
    
if __name__ == "__main__":
    main()