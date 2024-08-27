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
gameWindow.fill(WHITE)
pygame.display.set_caption("car")
CENTERX = WIDTH/2
CENTERY = HEIGHT/2
#large oval
pygame.draw.ellipse(gameWindow,BLUE,(CENTERX-75,CENTERY-50,150,100),0)
#draw rectangle
pygame.draw.rect(gameWindow, RED, (CENTERX-150,CENTERY,+300,+100),0)
#draw 2 bottom circles
pygame.draw.ellipse(gameWindow, BLUE, (CENTERX-100,CENTERY+80,50,40))
pygame.draw.ellipse(gameWindow, BLUE, (CENTERX+100-40,CENTERY+80,50,40))
pygame.display.update()
