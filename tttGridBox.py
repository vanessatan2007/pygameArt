
import pygame
pygame.init()  # initializes the pygame
WIDTH = 300
HEIGHT = 300
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0,255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)
gameWindow.fill(BLACK)
pygame.draw.rect(gameWindow, WHITE, (100,0,+10,+300), 10) 
pygame.draw.rect(gameWindow, WHITE, (200,0,+10,+300), 10)
pygame.draw.rect(gameWindow, WHITE, (0,100,+300,+10), 10)
pygame.draw.rect(gameWindow, WHITE, (0,200,+300,+10), 10)

pygame.display.update()
