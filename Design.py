
import pygame
pygame.init()  # initializes the pygame
WIDTH = 400
HEIGHT = 400
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0,255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)
gameWindow.fill(BLACK)
pygame.display.set_caption("design")
pygame.draw.circle(gameWindow,RED, (WIDTH//2,HEIGHT//2), 100,1)
pygame.draw.rect(gameWindow, RED, (WIDTH//2-100,HEIGHT//2-100,+100,+100),1)
pygame.draw.rect(gameWindow, RED, (WIDTH//2-100,HEIGHT//2-100,+100,+100),1)
pygame.draw.rect(gameWindow, RED, (WIDTH//2,HEIGHT//2-100,+100,+100),1)
pygame.draw.rect(gameWindow, RED, (WIDTH//2,HEIGHT//2,+100,+100),1)
pygame.draw.circle(gameWindow,RED, (WIDTH//2+50,HEIGHT//2-50), 50,1)

pygame.display.update()
