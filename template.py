import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [480, 320]  # RPi screen size
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)

done = False

while not done:
    # initialization
    dimensions = [50, 50, 50, 50]
    
    # draw start
    pygame.draw.rect(screen, WHITE, dimensions)
    
    # draw end
    pygame.display.flip()
    # initialization
    
    # draw start
    
    # draw end
    
pygame.quit()