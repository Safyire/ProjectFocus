import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (65, 105, 225)
colors = [WHITE, RED, BLUE]
color = random.choice(colors)

pygame.init()

size = [480, 320]  # RPi screen size
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size, pygame.NOFRAME)

pygame.mouse.set_visible(False)

done = False

clock = pygame.time.Clock()

gravity = 1

pillar = pygame.draw.rect(screen, color, [0, 0, 10, 10])
font = pygame.font.SysFont('Comic Sans MS', 30)


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


def jump():
    Bird.vel = -10


class Bird(pygame.sprite.Sprite):
    x = 240
    y = 160

    def update(self):
        if started:
            if Bird.y < 320:
                Bird.y += Bird.velocity
                Bird.velocity += gravity
            else:
                Bird.y = 320
                die()
            if Bird.y < 0:
                Bird.y = 0
                Bird.velocity = 0
        else:
            Bird.y = 250 + math.sin(runs / 10) * 15

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [0, 0, 10, 10])

        self.rect = self.image.get_rect()


def die():
    global dead
    dead = True
    run = False


def pipePair():
    r = random.randint(75, 350)
    pipes.append(pillar("DOWN", 900, r))
    pipes.append(pillar("UP", 900, 600 - (r + 125)))
    global score
    score += 1


def animateGround():
    screen.blit(screen, ((runs % 111) * -7, 500))


class Pillar:
    def __init__(self, dir, x, len):
        self.dir = dir
        self.x = x
        self.len = len

    def update(self):
        if self.dir == "UP":
            screen.blit(pillar, (self.x, 6 - self.len))
        else:
            screen.blit(pygame.transform.rotate(pillar, 180)), (self.x, self.len - 431)
        if not dead:
            self.x -= 7

    def checkCollide(self):
        if self.dir == "DOWN":
            if self.x < Bird.x < self.x + 75:
                if Bird.y + 2 < self.len:
                    die()
        else:
            if Bird.x + 48 > self.x and self.x + 75 > Bird.x:
                if Bird.y + 45 > 600 - self.len:
                    die()

    Variables()


while not done:
    # initialization
    pygame.mouse.set_visible(False)
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                if not started:
                    started = True
                if not dead:
                    jump()
        elif event.type == pygame.QUIT:
            run = False

    screen.blit(screen, (0, 0))
    if runs % 45 == 0 and started:
        pipePair()
    for p in pipes:
        p.update()
        p.checkCollide()
    Bird.update()
    animateGround()

    scoreboard = font.render(str(score), False, (0, 0, 0))
    while score < 3:
        scorebase = pygame.draw.rect(screen, (255, 255, 255), (7, 5, len(str(score)) * 15 + 10, 35))
        screen.blit(scoreboard, (10, 0))
    pygame.display.update()
    if not dead:
        runs += 1

pygame.quit()
