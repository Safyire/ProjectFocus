from datetime import datetime
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [480, 320]
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)
    
    now = datetime.now()
    time_hour = now.strftime("%H")
    time_hour_2 = int(time_hour)
    time_minute = now.strftime("%M")
    
    if (time_hour_2 > 12):
        time_hour_2 -= 12
        time_hour = ("0" + str(time_hour_2))
        
    
    
    current_time = time_hour + ":" + time_minute
    
    #draw start
    font = pygame.font.SysFont('Calibri', 275, True, False)
    text = font.render(current_time, True, WHITE)
    screen.blit(text, [7, 50])
    #draw end
    
    pygame.display.flip()
    
pygame.quit()