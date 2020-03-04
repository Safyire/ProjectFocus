import pygame
import math
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

PI = 3.141592653

pygame.init()

size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)
done = False

#draw setup
angle = 0
area_width = random.randint(50, 100)
area_x = 235 #original value: 235
area_y = 155 #original value: 155

while not done:
    dimensions = [110, 30, 250, 250]
    
    #draw start
    pygame.draw.ellipse(screen, GREEN, dimensions, 2) #Main circle
    
    angle += .1
    
    x = 125 * math.sin(angle) + 235
    y = 125 * math.cos(angle) + 155
    
    for a in range(0, area_width): #Shaded area of the main circle
        pygame.draw.line(screen, (0, 100, 0), [235, 155], [125 * math.sin(a * .01) + area_x, 125 * math.cos(a * .01) + area_y], 3)
    
    pygame.draw.line(screen, GREEN, [235, 155], [x, y], 2) #Main line
    
    if angle > 2 * PI:
        angle = angle - 2 * PI
    
    #Exit if the mouse is clicked on the window (tap)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True
        
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    pygame.draw.line(screen, BLACK, [235, 155], [x, y], 2)
    #draw end

pygame.quit()