import pygame
import time
import random

#---------------colors---------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREY = (128, 128, 128)
BROWN = (128, 64, 64)

#---------------set up the screen---------------
size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)
pygame.display.set_mode(size, pygame.NOFRAME)

#---------------rock---------------
#class
class Rock:
    #initialize the rock
    def __init__(self):
        self.x = 0
        self.y = 0
    #draw function
    def draw_rock(self):
        pygame.draw.circle(screen, GREY, [self.x, self.y], 35)
#function to make
def make_rock(x, y):
    rock = Rock()
    rock.x = x
    rock.y = y
    return rock

#---------------scissors---------------
#class
class Scissors:
    #initialize the scissors
    def __init__(self):
        self.x = 0
        self.y = 0
    #draw function
    def draw_scissors(self):
        #blades
        pygame.draw.polygon(screen, GREY, [(self.x - 5, self.y + 10), (self.x + 5, self.y + 10), (self.x, self.y + 70)]) #straight
        pygame.draw.polygon(screen, GREY, [(self.x - 33, self.y + 23), (self.x - 18, self.y + 18), (self.x + 33, self.y + 52)]) #diagonal
        #right circle
        pygame.draw.circle(screen, BROWN, [self.x - 25, self.y + 25], 15)
        pygame.draw.circle(screen, CYAN, [self.x - 25, self.y + 25], 8)
        #left circle
        pygame.draw.circle(screen, BROWN, [self.x, self.y], 15)
        pygame.draw.circle(screen, CYAN, [self.x, self.y], 8)
#function to make
def make_scissors(x, y):
    scissors = Scissors()
    scissors.x = x
    scissors.y = y
    return scissors

#---------------paper---------------
#class
class Paper:
    #initialize the paper
    def __init__(self):
        self.x = 0
        self.y = 0
    #draw function
    def draw_paper(self):
        pygame.draw.polygon(screen, WHITE, [(self.x, self.y), (self.x + 65, self.y - 15), (self.x + 80, self.y + 75), (self.x + 15, self.y + 90)])
#function to make
def make_paper(x, y):
    paper = Paper()
    paper.x = x
    paper.y = y
    return paper

#---------------main function---------------
def main():
    #initialize pygame
    pygame.init()
    
    #initialize the clock
    clock = pygame.time.Clock()
    
    #this boolean will be used to tell when to stop the game
    done = False
    
    #---------------make the rocks, papers, and scissors, two of each---------------
    rock1 = make_rock(100, 160)
    paper1 = make_paper(60, 120)
    scissors1 = make_scissors(100, 130)
    rock2 = make_rock(380, 160)
    paper2 = make_paper(340, 120)
    scissors2 = make_scissors(380, 130)
    
    #make the background cyan
    screen.fill(CYAN)
    
    #---------------GAME---------------
    while not done:
        #---------------choosing screen---------------
        #title
        font = pygame.font.SysFont('Calibri', 55, True, False)
        screen.blit(font.render("Rock, Paper, or Scissors?", True, WHITE), [10, 25])
        font = pygame.font.SysFont('Calibri', 30, True, False)
        #choose rock
        pygame.draw.circle(screen, RED, [70, 200], 50)
        screen.blit(font.render("Rock", True, WHITE), [45, 190])
        #choose paper
        pygame.draw.circle(screen, GREEN, [240, 200], 50)
        screen.blit(font.render("Paper", True, WHITE), [210, 190])
        #choose scissors
        pygame.draw.circle(screen, BLUE, [410, 200], 50)
        screen.blit(font.render("Scissors", True, WHITE), [368, 190])
        
        chosen = False #will end the loop that is waiting for one of the choices to be pressed
        choice = 0 #will hold 1, 2, or 3 depending on whatthe player chose
        pygame.display.flip()
        
        #-----waits for the player to choose-----
        while not chosen:
            for event in pygame.event.get():
                #---if the mouse is clicked---
                if pygame.mouse.get_pressed()[0]:
                    #get the mouse position
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    #---if it is on the "rock" circle---
                    if mouse_x > 20 and mouse_x < 120 and mouse_y > 150 and mouse_y < 250:
                        choice = 1 #1 corresponds to rock
                        chosen = True #end the loop
                    #---if it is on the "paper" circle---
                    elif mouse_x > 190 and mouse_x < 290 and mouse_y > 150 and mouse_y < 250:
                        choice = 2 #2 corresponds to paper
                        chosen = True #end the loop
                    #---if it is on the "scissor" circle---
                    elif mouse_x > 360 and mouse_x < 460 and mouse_y > 150 and mouse_y < 250:
                        choice = 3 #3 corresponds to scissors
                        chosen = True #end the loop
        
        #---------------move to actual game---------------
        screen.fill(CYAN) #make the screen blank
        font = pygame.font.SysFont('Calibri', 55, True, False) #change the font
        screen.blit(font.render("Rock, Paper, or Scissors?", True, WHITE), [10, 25]) #print the title
        font = pygame.font.SysFont('Calibri', 30, True, False) #change the font again
        #---if the player chose rock---
        if choice == 1:
            #draw the "rock" circle
            pygame.draw.circle(screen, RED, [70, 200], 50)
            screen.blit(font.render("Rock", True, WHITE), [45, 190])
        #---if the player chose paper---
        elif choice == 2:
            #draw the "paper" circle
            pygame.draw.circle(screen, GREEN, [240, 200], 50)
            screen.blit(font.render("Paper", True, WHITE), [210, 190])
        #---if the player chose scissors---
        elif choice == 3:
            #draw the "scissors" circle
            pygame.draw.circle(screen, BLUE, [410, 200], 50)
            screen.blit(font.render("Scissors", True, WHITE), [368, 190])
        pygame.display.flip()
        time.sleep(1) #display the player's choice for one second
        
        #---countdown from 3---
        for i in range(3, 0, -1):
            screen.fill(CYAN) #make the screen blank
            font = pygame.font.SysFont('Calibri', 200, True, False) #change the font
            screen.blit(font.render(str(i), True, WHITE), [200, 25]) #print the number
            pygame.display.flip()
            time.sleep(1) #wait one second
        
        screen.fill(CYAN)#make the screen blank
        cpu_choice = random.randrange(1, 4) #randomize the cpu's choice
        #---draw the player's choice---
        if choice == 1:
            rock1.draw_rock()
        elif choice == 2:
            paper1.draw_paper()
        elif choice == 3:
            scissors1.draw_scissors()
        #---draw the cpu's choice---
        if cpu_choice == 1:
            rock2.draw_rock()
        elif cpu_choice == 2:
            paper2.draw_paper()
        elif cpu_choice == 3:
            scissors2.draw_scissors()
        
        pygame.display.flip()
        time.sleep(1) #wait one second
        
        #---------------win or lose---------------
        font = pygame.font.SysFont('Calibri', 55, True, False)#change the font
        #---if there's a tie---
        if choice == cpu_choice:
            screen.blit(font.render("TIE", True, WHITE), [210, 55])
        #---if the player won---
        elif (choice == 1 and cpu_choice == 3) or (choice == 2 and cpu_choice == 1) or (choice == 3 and cpu_choice == 2):
            screen.blit(font.render("YOU WON", True, WHITE), [150, 55])
        #---if the cpu won---
        elif (cpu_choice == 1 and choice == 3) or (cpu_choice == 2 and choice == 1) or (cpu_choice == 3 and choice == 2):
            screen.blit(font.render("YOU LOST", True, WHITE), [140, 55])
        
        #---draw the close game button---
        pygame.draw.rect(screen, BLUE, (154, 240, 172, 35))#draw the rectangle
        font = pygame.font.SysFont('Calibri', 35, True, False)#change the font
        screen.blit(font.render("CLOSE GAME", True, WHITE), [159, 245])#print "CLOSE GAME" on the rectangle
        pygame.display.flip()
        
        #-----wait until the player clicks the "CLOSE GAME" button-----
        close = False
        while not close:
            for event in pygame.event.get():
                #---if the mouse is clicked---
                if pygame.mouse.get_pressed()[0]:
                    #get the mouse position
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    #---if it is on the "CLOSE GAME" button---
                    if mouse_x > 154 and mouse_x < 326 and mouse_y > 240 and mouse_y < 275:
                        close = True #end this while loop
                        done = True #end the while loop controlling the game
                        
        clock.tick(60)
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()