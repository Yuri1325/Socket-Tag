import pygame
import pygame.locals
from network import Network
from Player import Player
from Wall import Wall
from Text import Text
from _thread import *
from Button import Button
import math
import time
import socket



pygame.init()
pygame.mouse.set_visible(True)


introFinished = False
serverSelected = False
inGame = False
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Tag")
pygame.display.set_icon(pygame.image.load("images\Run/tile003.png").convert_alpha())
clock = pygame.time.Clock()
run = True

leftWall = Wall(0,300,10,600,False)
rightWall = Wall(800,300,10,600,False)
topWall = Wall(400,0,800,10,True)
bottomWall = Wall(400,600,800,10,True)
w1= Wall(400,100,10,75,False)
wallList = [leftWall,rightWall,topWall,bottomWall,w1]
startTime = time.time()
arial = pygame.font.SysFont("Arial",15,True)
pxlf1 = pygame.font.Font("Fonts\yoster.ttf",40)
creatingNewServer = True
n = Network()
def intro(timeElapsed):
        global introFinished,serverSelected
        if (timeElapsed < 3):
            presentsCard = Text("Computer Science 1 2024-2025",pxlf1,(255,255,255),50,200,screen)
            presentsCard2 = Text("Presents",pxlf1,(255,255,255),280,250,screen)
        else:
            titleCard = Text("TAG",pygame.font.Font("Fonts\yoster.ttf",100),(255,255,255),290,100,screen)
            startButton = Button(400,250,pygame.image.load("images\Buttons/5811aefe875733a49f167ca73a33c02a.png").convert_alpha(),pygame.image.load("images\Buttons\starthighlight.png").convert_alpha(),screen,0.5)
            
            if startButton.isClicked:
                introFinished = True
                serverSelected = True
    

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    currentTime = time.time() 
    timeElapsed = int(currentTime - startTime)  
    clock.tick(25)
    screen.fill((0,0,0))   
    displayTime = Text(f"Time Elapsed({timeElapsed})",arial,(255,255,255),10,10,screen)
    mosPos = Text(f"Mouse Pos {pygame.mouse.get_pos()}",arial,(255,255,255),10,30,screen)   
    if inGame:
        
        
        
        player = n.startingPos
       
        
        playerCords = Text(f"Player Pos {round(player.pos)}",arial,(255,255,255),10,50,screen)
        player2 = n.Send(player)
        player.move(screen)
        player2.update(screen)
        for wall in wallList:
            wall.draw(screen)
            player.collideWith(wall)
    
    if ((introFinished==True)and(serverSelected==True)):
        inGame = True 
    if not introFinished:
        intro(timeElapsed) 
         
                
   
    
    
    
    
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit() 

