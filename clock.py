from datetime import datetime
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [480, 320]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("YOOOOOOO")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    #draw start
    font = pygame.font.SysFont('Calibri', 275, True, False)
    text = font.render(current_time, True, WHITE)
    screen.blit(text, [0, 50])
    #draw end
    
    pygame.display.flip()
    
pygame.quit()