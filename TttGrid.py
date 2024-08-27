
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

keepRunning = True 

while keepRunning: # this line is optional
  pygame.event.clear()                # remove all events from the queue
  gameWindow.fill(BLACK)
  pygame.draw.line(gameWindow, WHITE, (100,0), (100,300), 1) 
  pygame.draw.line(gameWindow, WHITE, (200, 0), (200,300), 1)
  pygame.draw.line(gameWindow, WHITE, (0,100),(300,100),1)
  pygame.draw.line(gameWindow, WHITE, (0,200),(300,200),1)
  pygame.display.update()
pygame.quit()