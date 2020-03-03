import pygame
import random

#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#variables
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
BALL_SIZE = 25

#ball class
class Ball:
    #initialize the ball
    def __init__(self):
        self.x = 0 #starting coords
        self.y = 0
        self.change_x = 4 #how fast the ball moves
        self.change_y = 4
        self.color = RED #color

#function to make a ball
    #param: color - one of the color variables made at the beginning
def make_ball(color):
    ball = Ball()
    #randomize the coords
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
    #set the color of the ball
    ball.color = color
    
    return ball

def main():
    #initialize pygame
    pygame.init()
    
    #set up the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_mode(size, pygame.NOFRAME)
    
    #this boolean will be used to tell when to stop the game
    done = False
    
    #initialize the clock
    clock = pygame.time.Clock()
    
    #make a list and store 3 balls in it
    ball_list = []
    ball = make_ball(RED)
    ball_list.append(ball)
    ball = make_ball(GREEN)
    ball_list.append(ball)
    ball = make_ball(BLUE)
    ball_list.append(ball)
    
    #counts how many times you made every ball disappear
    games_played = 0
    
    #game
    while not done:
        for event in pygame.event.get():
            #if the mouse is clicked and it is on a ball, make the ball disappear
            if pygame.mouse.get_pressed()[0]:
                #get mouse coords
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                #cycle through the list of balls
                for ball in ball_list:
                    #if the mouse is on that ball, remove it
                    if mouse_x > ball.x - 25 and mouse_x < ball.x + 25 and mouse_y > ball.y - 25 and mouse_y < ball.y + 25:
                        ball_list.remove(ball)
        #if all the balls have been clicked
        if len(ball_list) == 0:
            #add 1 to games_played
            games_played += 1
            #check if you've won three games and end the game if you have
            if games_played == 3:
                done = True
            else:
                #restart the game by adding the balls back into the list
                ball = make_ball(RED)
                ball_list.append(ball)
                ball = make_ball(GREEN)
                ball_list.append(ball)
                ball = make_ball(BLUE)
                ball_list.append(ball)
        #move the balls
        for ball in ball_list:
            #change the coords
            ball.x += ball.change_x
            ball.y += ball.change_y
            #if the ball is touching or oustside the boundaries, bounce it off the wall
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
            #draw over the old balls
            screen.fill(BLACK)
            
        #draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)
        
        #limit to 60 fps
        clock.tick(60)
            
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    