#Name: Vanessa Tan
#Title <Face.py
#Description: find the largest number in a list of numbers
import pygame
pygame.init()  # initializes the pygame
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0,255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)
PURPLE = (240,0,255)
gameWindow.fill(WHITE)
pygame.display.set_caption("clown")
CENTERX = WIDTH/2
CENTERY = HEIGHT/2
#Clowns ears
pygame.draw.ellipse(gameWindow, PURPLE, (CENTERX-200, CENTERY-35, 50,70),0)
pygame.draw.ellipse(gameWindow, PURPLE, (CENTERX+150, CENTERY-35, 50,70),0)
#Clowns face
pygame.draw.ellipse(gameWindow,GREEN, (CENTERX-180, CENTERY-200,360,400),0)
#Clown eyes
pygame.draw.ellipse(gameWindow, PURPLE, (CENTERX-65,CENTERY-65,50,50))
pygame.draw.ellipse(gameWindow, PURPLE, (CENTERX+15,CENTERY-65,50,50))
#Clown's nose
pygame.draw.ellipse(gameWindow, BLUE, (CENTERX-25,CENTERY-25,50,50))
#Clown's mouth
pygame.draw.arc(gameWindow, RED, (CENTERX-100,CENTERY-25,200,100 ),3.14,6.28)

pygame.display.update()
