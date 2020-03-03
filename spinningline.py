import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

PI = 3.141592653

pygame.init()

size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)
done = False
angle = 0
spinning = True #Contribution by Crockett
event = pygame.key.get_pressed()

while not done:
    dimensions = [110, 30, 250, 250]
    
    #draw start
    pygame.draw.ellipse(screen, GREEN, dimensions, 2)
    
    angle += .1
    
    x = 125 * math.sin(angle) + 235
    y = 125 * math.cos(angle) + 155
    
    pygame.draw.line(screen, GREEN, [235, 155], [x, y], 2)
    
    if angle > 2 * PI:
        angle = angle - 2 * PI
    
    if event[pygame.K_SPACE]:
        done = True
        
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    pygame.draw.line(screen, BLACK, [235, 155], [x, y], 2)
    #draw end
    
pygame.quit()
