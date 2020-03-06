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
    x_base = 110
    y_base = 35
    main_dimensions = [110, 35, 250, 250] # [x, y, h, w]
    
    # draw start
    pygame.draw.rect(screen, WHITE, main_dimensions, 3)
    
    pygame.draw.line(screen, WHITE, [x_base*1.755, y_base], [x_base*1.755, 320-y_base], 3)
    pygame.draw.line(screen, WHITE, [x_base*2.5, y_base], [x_base*2.5, 320-y_base], 3)
    
    pygame.draw.line(screen, WHITE, [x_base, y_base+(250/3)], [x_base*3.25, y_base+(250/3)], 3)
    pygame.draw.line(screen, WHITE, [x_base, y_base+(500/3)], [x_base*3.25, y_base+(500/3)], 3)
    
    # (For testing) Exit if the mouse is clicked on the window (tap)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True
            
    # draw end
    pygame.display.flip()
    
pygame.quit()