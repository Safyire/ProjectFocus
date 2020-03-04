import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 480
    def __init__(self, start, dirx, diry, color=(255,0,0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color
        
    def move(self, dirx, diry):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)  # change position     
    
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Width/Height of each cube
        i = self.pos[0] # Current row
        j = self.pos[1] # Current Column

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        
        if eyes: # Draws the eyes
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
            
class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  #Head will be the front of the snake
        self.body.append(self.head)  #Adds head (which is a cube object)
        # to our body list

        # These will represent the direction our snake is moving
        self.dirx = 0 
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pos = pygame.mouse.get_pos()
        dirx = pos[0]
        diry = pos[1]
        
        self.snake.dirx = dirx
        self.snake.diry = diry
        
        for i, c in enumerate(self.body):  # Loop through every cube in body
            p = c.pos[:]  #Stores the cubes position on the grid
            if p in self.turns:  # If the cubes current position is one where turned
                turn = self.turns[p]  # Get the direction should turn
                c.move(turn[0],turn[1])  # Move cube in that direction
                if i == len(self.body)-1:  # If this is the last cube in body remove the turn from the dict
                    self.turns.pop(p)
            else: 
                # If the cube reaches the edge of the screen we will make it appear on the opposite side
                if c.dirx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirx,c.diry)  # If we haven't reached the edge just move in current direction

    def reset(self, pos):
        pass

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  
                c.draw(surface, True)  # adding the true as an argument will tell us to draw eyes
            else:
                c.draw(surface)  # otherwise we will just draw a cube 
        

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Gives us the distance between the lines

    x = 0  # Keeps track of the current x
    y = 0  # Keeps track of the current y
    for l in range(rows):  # Draw one vertical and one horizontal line each loop
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
        

def redrawWindow(surface):
    global rows, width, s
    surface.fill((0,0,0))  # Fills the screen with black
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)  # Draw grid lines
    pygame.display.update()  # Updates the screen


def randomSnack(rows, item):
    positions = item.body #positions of cubes in snake
    
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos ==  (x,y), positions))) > 0: #check if position generated is same as snake
            continue
        else:
            break
        return (x,y)


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 480  # Width of screen
    height = 20  # Height of screen
    rows = 20  # Amount of rows

    win = pygame.display.set_mode((width, height), pygame.NOFRAME)  # Creates screen object

    pygame.mouse.set_visible(False)
    
    s = snake((255,0,0), (10,10))  
  
    clock = pygame.time.Clock() 
    snack = cube(randomSnack(rows, s), color = (0,255,0))
    flag = True
    # STARTING MAIN LOOP
    while flag:
        pygame.time.delay(50)  # Delays the game so it doesn't run too quickly
        clock.tick(10)  # Game runs at 10 FPS
        s.move()
        redrawWindow(win)  # Refresh screen
        if s.body[0] == snake.post:
            s.addCube()
            snack = cube(randomSnack(rows,s), color = (0, 255, 0)) #new snack object
main()