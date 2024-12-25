import pygame
from network import Network
from Player import Player
from _thread import *
import time
n = Network()
pygame.init()



screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()
run = True
player = n.startingPos


while run:
    clock.tick(60)
    screen.fill((255,255,255))
    player2 = n.Send(player)
    
    
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            run = False
            n.Send("/?/")
    
   
    player.move(screen)
    player2.update(screen)
    pygame.display.update()
    

pygame.quit()