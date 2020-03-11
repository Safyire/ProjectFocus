import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (65, 105, 225)
colors = [WHITE, RED, BLUE]
color = random(colors)

pygame.init()

size = [480, 320]  # RPi screen size
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)

pygame.mouse.set_visible(False)

done = False

clock = pygame.time.Clock()

gravity = 1

def Variables():
    global dead
    dead = False
    global score
    score = -2
    global run
    run = True
    global started
    started = False
    global runs
    runs = 0
    global pipes
    pipes = []
    Bird.x = 240
    Bird.y = 160
    Bird.velocity = 0


def update():

    if started:
        if Bird.y < 320:
            Bird.y += Bird.velocity
            Bird

        else:
            Bird.y = 320


class Bird:

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):

        if started:
            if Bird.y < 320:
                Bird.y += Bird.velocity
            else:
                Bird.y = 320

#class Pilar:




while not done:
    # initialization
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.fill(BLACK)
    # draw start
    screen.fill(BLACK)

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
