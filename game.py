import pygame
from network import Network
from Player import Player
from Wall import Wall
from _thread import *
import time
n = Network()
pygame.init()
pygame.mouse.set_visible(False)


screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()
run = True
player = n.startingPos
wall = Wall(200,200,10,200)

while run:
    clock.tick(25)
    screen.fill((0,0,0))
    player2 = n.Send(player)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
                
   
    player.move(screen)
    player2.update(screen)
    wall.draw(screen)
    
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit()