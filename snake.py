import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 480
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
        
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass
        

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # The head will be the front of the snake
        self.body.append(self.head)  # We will add head (which is a cube object)
        # to our body list

        # These will represent the direction our snake is moving
        self.dirnx = 0 
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if user hit the red x
                pygame.quit()

            keys = pygame.key.get_pressed()  # See which keys are being pressed

            for key in keys:  # Loop through all the keys
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        

    def reset(self, pos):
        pass

    def addCube(self):
        pass
        

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Gives us the distance between the lines

    x = 0  # Keeps track of the current x
    y = 0  # Keeps track of the current y
    for l in range(rows):  # We will draw one vertical and one horizontal line each loop
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
        

def redrawWindow(surface):
    surface.fill((0,0,0))  # Fills the screen with black
    drawGrid(surface)  # Will draw our grid lines
    pygame.display.update()  # Updates the screen


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 480  # Width of our screen
    height = 20  # Height of our screen
    rows = 20  # Amount of rows

    win = pygame.display.set_mode((width, height), pygame.NOFRAME)  # Creates our screen object

    s = snake((255,0,0), (10,10))  # Creates a snake object which we will code later
  
    clock = pygame.time.Clock() # creating a clock object

    flag = True
    # STARTING MAIN LOOP
    while flag:
        pygame.time.delay(50)  # This will delay the game so it doesn't run too quickly
        clock.tick(10)  # Will ensure our game runs at 10 FPS
        redrawWindow(win)  # This will refresh our screen  
main()