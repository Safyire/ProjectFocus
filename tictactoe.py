import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)

done = False

while not done:
    #initialization
    dimensions = [110, 35, 250, 250]
    
    #draw start
    pygame.draw.rect(screen, WHITE, dimensions, 3)
    
    #Exit if the mouse is clicked on the window (tap)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True
            
    #draw end
    pygame.display.flip()
    
pygame.quit()