import pygame
from math import pi

pygame.init()  # initializes the pygame engine
# --- initialize variables  ------------
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

# the MAIN program begins here
pygame.event.pump()
pygame.display.set_caption("Canadian Flag")
gameWindow.fill(WHITE)

CENTREX = WIDTH/2
CENTREY = HEIGHT /2

#flag at the bottom
pygame.draw.rect(gameWindow, GREY, (CENTREX-64, CENTREY-32, +5,+332),0)
y = 200
pygame.draw.rect(gameWindow, WHITE, (CENTREX-32,CENTREY-32+y,+64,+64))
#red squares
pygame.draw.rect(gameWindow, RED, (CENTREX-64, CENTREY-32+y, +32,+64),0)
pygame.draw.rect(gameWindow, RED, (CENTREX+32, CENTREY-32+y, +32,+64),0)
#Maple leaf
pygame.draw.polygon(gameWindow, RED, ((CENTREX-15,CENTREY+20+y),(CENTREX-15,CENTREY+15+y), (CENTREX-25,CENTREY+10+y),(CENTREX-22,CENTREY+5+y),(CENTREX-28,CENTREY-1+y), (CENTREX-20,CENTREY+y), (CENTREX-20,CENTREY-5+y), (CENTREX-8,CENTREY+y),(CENTREX-10,CENTREY-20+y), (CENTREX-5,CENTREY-15+y), (CENTREX,CENTREY-25+y),(CENTREX+5,CENTREY-15+y),(CENTREX+10,CENTREY-20+y),(CENTREX+8,CENTREY+y), (CENTREX+20,CENTREY-5+y),(CENTREX+20,CENTREY+y),
(CENTREX+28,CENTREY-1+y) ,(CENTREX+22,CENTREY+5+y),(CENTREX+25,CENTREY+10+y),(CENTREX+15,CENTREY+15+y), (CENTREX+15,CENTREY+20+y),(CENTREX+1,CENTREY+20+y),(CENTREX+1,CENTREY+28+y), (CENTREX-1,CENTREY+28+y), (CENTREX-1,CENTREY+20+y)  ), 0) 

pygame.display.update()   #display must be updated to show what you are drawing
pygame.time.delay(700)  # millisecond
gameWindow.fill(WHITE) #clear the whole window or just draw a white box over the leaf


#move flag up 2
pygame.draw.rect(gameWindow, GREY, (CENTREX-64, CENTREY-32, +5,+332),0)
y = y - 50
pygame.draw.polygon(gameWindow, RED, ((CENTREX-15,CENTREY+20+y),(CENTREX-15,CENTREY+15+y), (CENTREX-25,CENTREY+10+y),(CENTREX-22,CENTREY+5+y),(CENTREX-28,CENTREY-1+y), (CENTREX-20,CENTREY+y), (CENTREX-20,CENTREY-5+y), (CENTREX-8,CENTREY+y),(CENTREX-10,CENTREY-20+y), (CENTREX-5,CENTREY-15+y), (CENTREX,CENTREY-25+y),(CENTREX+5,CENTREY-15+y),(CENTREX+10,CENTREY-20+y),(CENTREX+8,CENTREY+y), (CENTREX+20,CENTREY-5+y),(CENTREX+20,CENTREY+y),
(CENTREX+28,CENTREY-1+y) ,(CENTREX+22,CENTREY+5+y),(CENTREX+25,CENTREY+10+y),(CENTREX+15,CENTREY+15+y), (CENTREX+15,CENTREY+20+y),(CENTREX+1,CENTREY+20+y),(CENTREX+1,CENTREY+28+y), (CENTREX-1,CENTREY+28+y), (CENTREX-1,CENTREY+20+y)  ), 0) 
pygame.draw.rect(gameWindow, RED, (CENTREX-64, CENTREY-32+y, +32,+64),0)
pygame.draw.rect(gameWindow, RED, (CENTREX+32, CENTREY-32+y, +32,+64),0)
pygame.display.update()   #display must be updated to show what you are drawing
pygame.time.delay(700)  # millisecond#move flag up
gameWindow.fill(WHITE) #clear the whole window or just draw a white box over the leaf

#move flag up 3
pygame.draw.rect(gameWindow, GREY, (CENTREX-64, CENTREY-32, +5,+332),0)
y = y - 50
pygame.draw.polygon(gameWindow, RED, ((CENTREX-15,CENTREY+20+y),(CENTREX-15,CENTREY+15+y), (CENTREX-25,CENTREY+10+y),(CENTREX-22,CENTREY+5+y),(CENTREX-28,CENTREY-1+y), (CENTREX-20,CENTREY+y), (CENTREX-20,CENTREY-5+y), (CENTREX-8,CENTREY+y),(CENTREX-10,CENTREY-20+y), (CENTREX-5,CENTREY-15+y), (CENTREX,CENTREY-25+y),(CENTREX+5,CENTREY-15+y),(CENTREX+10,CENTREY-20+y),(CENTREX+8,CENTREY+y), (CENTREX+20,CENTREY-5+y),(CENTREX+20,CENTREY+y),
(CENTREX+28,CENTREY-1+y) ,(CENTREX+22,CENTREY+5+y),(CENTREX+25,CENTREY+10+y),(CENTREX+15,CENTREY+15+y), (CENTREX+15,CENTREY+20+y),(CENTREX+1,CENTREY+20+y),(CENTREX+1,CENTREY+28+y), (CENTREX-1,CENTREY+28+y), (CENTREX-1,CENTREY+20+y)  ), 0) 
pygame.draw.rect(gameWindow, RED, (CENTREX-64, CENTREY-32+y, +32,+64),0)
pygame.draw.rect(gameWindow, RED, (CENTREX+32, CENTREY-32+y, +32,+64),0)

pygame.display.update()   #display must be updated to show what you are drawing
pygame.time.delay(500)  # millisecond#move flag up
gameWindow.fill(WHITE) #clear the whole window or just draw a white box over the leaf

#move flag up 4
pygame.draw.rect(gameWindow, GREY, (CENTREX-64, CENTREY-32, +5,+332),0)
y = y - 50
pygame.draw.polygon(gameWindow, RED, ((CENTREX-15,CENTREY+20+y),(CENTREX-15,CENTREY+15+y), (CENTREX-25,CENTREY+10+y),(CENTREX-22,CENTREY+5+y),(CENTREX-28,CENTREY-1+y),(CENTREX-20,CENTREY+y), (CENTREX-20,CENTREY-5+y), (CENTREX-8,CENTREY+y),(CENTREX-10,CENTREY-20+y), (CENTREX-5,CENTREY-15+y),(CENTREX,CENTREY-25+y), (CENTREX+5,CENTREY-15+y),(CENTREX+10,CENTREY-20+y),(CENTREX+8,CENTREY+y), (CENTREX+20,CENTREY-5+y),(CENTREX+20,CENTREY+y),
  (CENTREX+28,CENTREY-1+y) ,(CENTREX+22,CENTREY+5+y), (CENTREX+25,CENTREY+10+y),(CENTREX+15,CENTREY+15+y), (CENTREX+15,CENTREY+20+y),(CENTREX+1,CENTREY+20+y),(CENTREX+1,CENTREY+28+y), (CENTREX-1,CENTREY+28+y), (CENTREX-1,CENTREY+20+y)   ), 0)
pygame.draw.rect(gameWindow, RED, (CENTREX-64, CENTREY-32+y, +32,+64),0)
pygame.draw.rect(gameWindow, RED, (CENTREX+32, CENTREY-32+y, +32,+64),0)

pygame.display.update()   #display must be updated to show what you are drawing
pygame.time.delay(500)  # millisecond#move flag up
gameWindow.fill(WHITE) #clear the whole window or just draw a white box over the leaf

#move flag up 5
pygame.draw.rect(gameWindow, GREY, (CENTREX-64, CENTREY-32, +5,+332),0)
y = y - 50
pygame.draw.polygon(gameWindow, RED, ((CENTREX-15,CENTREY+20+y),(CENTREX-15,CENTREY+15+y), (CENTREX-25,CENTREY+10+y),(CENTREX-22,CENTREY+5+y),(CENTREX-28,CENTREY-1+y),(CENTREX-20,CENTREY+y), (CENTREX-20,CENTREY-5+y), (CENTREX-8,CENTREY+y),(CENTREX-10,CENTREY-20+y), (CENTREX-5,CENTREY-15+y),(CENTREX,CENTREY-25+y),(CENTREX+5,CENTREY-15+y),(CENTREX+10,CENTREY-20+y),(CENTREX+8,CENTREY+y), (CENTREX+20,CENTREY-5+y),(CENTREX+20,CENTREY+y),(CENTREX+28,CENTREY-1+y) ,(CENTREX+22,CENTREY+5+y), (CENTREX+25,CENTREY+10+y),(CENTREX+15,CENTREY+15+y), (CENTREX+15,CENTREY+20+y),  (CENTREX+1,CENTREY+20+y),(CENTREX+1,CENTREY+28+y), (CENTREX-1,CENTREY+28+y), (CENTREX-1,CENTREY+20+y) ), 0)
pygame.draw.rect(gameWindow, RED, (CENTREX-64, CENTREY-32+y, +32,+64),0)
pygame.draw.rect(gameWindow, RED, (CENTREX+32, CENTREY-32+y, +32,+64),0)

#Oh Canada
word = "Oh Canada!" 
font1 =pygame.font.SysFont ("Courier New Bold", 36)  
graphics = font1.render (word, 0, RED)  
gameWindow.blit (graphics,( 400, 400) )

pygame.display.update()   #display must be updated to show what you are drawing
pygame.time.delay(5000)  # millisecond#move flag up
gameWindow.fill(WHITE) #clear the whole window or just draw a white box over the leaf


#pygame.quit()  # must put in quit, so you don't get an NO-responding window



