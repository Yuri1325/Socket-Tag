import pygame
from network import Network
from Player import Player
n = Network()
pygame.init()



screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))

run = True
player = n.startingPos


while run:
    screen.fill((255,255,255))
    player2 = n.Send(player)
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            run = False
            n.Send("/?/")
    
    player.draw(screen)
    player.move()
    player2.draw(screen)
    pygame.display.update()
    

pygame.quit()