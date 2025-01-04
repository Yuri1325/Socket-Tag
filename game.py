import pygame
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
clock = pygame.time.Clock()
run = True

leftWall = Wall(0,300,10,600,False)
rightWall = Wall(800,300,10,600,False)
topWall = Wall(400,0,800,10,True)
bottomWall = Wall(400,600,800,10,True)
wallList = [leftWall,rightWall,topWall,bottomWall]
startTime = time.time()
arial = pygame.font.SysFont("Arial",15)
pxlf1 = pygame.font.Font("Fonts\yoster.ttf",40)
creatingNewServer = True
def intro(timeElapsed):
        global introFinished,serverSelected
        if (timeElapsed < 5):
            presentsCard = Text("Computer Science 1 2024-2025",pxlf1,(255,255,255),70,200,screen)
            presentsCard2 = Text("Presents",pxlf1,(255,255,255),300,250,screen)
        else:
            titleCard = Text("TAG",pygame.font.Font("Fonts\yoster.ttf",100),(255,255,255),290,100,screen)
            startButton = Button(400,250,pygame.image.load("images\Buttons\start.png").convert_alpha(),pygame.image.load("images\Buttons\starthighlight.png").convert_alpha(),screen,0.3)
            
            if startButton.isClicked:
                introFinished = True
                
    
def serverMenu():
    global serverSelected
    startNewServer = Button(400,200,pygame.image.load("images\Buttons\strtnewserverbutton.png").convert_alpha(),pygame.image.load("images\Buttons\highlightedsns.png").convert_alpha(),screen,0.5)
    if startNewServer.isClicked:
                creatingNewServer = True
                serverSelected = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    currentTime = time.time() 
    timeElapsed = int(currentTime - startTime)  
    clock.tick(25)
    screen.fill((0,0,0))   
    displayTime = Text(f"Time Elapsed({timeElapsed})",arial,(255,255,255),100,10,screen)
    isplayTime = Text(f"Mouse Pos ({pygame.mouse.get_pos()})",arial,(255,255,255),200,10,screen)   
    if inGame:
        
        n = Network()
        
        player = n.startingPos
       
        
        playerCords = Text(f"X({round(player.pos.x)})  Y({round(player.pos.y)})",arial,(255,255,255),10,10,screen)
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
    if introFinished and not serverSelected:
        serverMenu()       
                
   
    
    
    
    
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit() 

