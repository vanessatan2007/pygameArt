
import pygame
pygame.init()  # initializes the pygame
WIDTH = 600
HEIGHT = 800
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0,255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)
gameWindow.fill(BLACK)
pygame.draw.rect(gameWindow, GREEN, (100,100,75,+75), 1) 
pygame.draw.rect(gameWindow, GREEN, (25,25,+75,+75), 1)
pygame.draw.rect(gameWindow, GREEN, (175,25,+75,+75), 1)
pygame.draw.line(gameWindow, GREEN,(25,25),(175,175))
pygame.draw.line(gameWindow, GREEN,(100,175),(175,100))
pygame.display.update()
