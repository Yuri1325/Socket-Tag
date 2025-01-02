import pygame
from network import Network
from Player import Player
from Wall import Wall
from Text import Text
from _thread import *
from Button import Button
import math
import time


pygame.init()
pygame.mouse.set_visible(True)

introFinished = False
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

def intro(timeElapsed):
   
    
    displayTime = Text(f"Time Elapsed({timeElapsed})",arial,(255,255,255),100,10,screen)
    isplayTime = Text(f"Mouse Pos ({pygame.mouse.get_pos()})",arial,(255,255,255),200,10,screen)
    if not introFinished:
        if (timeElapsed < 5):
            presentsCard = Text("Computer Science 1 2024-2025",pxlf1,(255,255,255),70,200,screen)
            presentsCard2 = Text("Presents",pxlf1,(255,255,255),300,250,screen)
        else:
            titleCard = Text("TAG",pygame.font.Font("Fonts\yoster.ttf",100),(255,255,255),290,100,screen)
            playButton = Button(400,200,pygame.image.load("images/titleButton.png").convert_alpha(),screen,0.3,1)
            
        
    

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    currentTime = time.time() 
    timeElapsed = int(currentTime - startTime)  
    clock.tick(25)
    screen.fill((0,0,0))      
    if introFinished:
        n = Network()
        player = n.startingPos
       
        
        playerCords = Text(f"X({round(player.pos.x)})  Y({round(player.pos.y)})",arial,(255,255,255),10,10,screen)
        player2 = n.Send(player)
        player.move(screen)
        player2.update(screen)
        for wall in wallList:
            wall.draw(screen)
        player.collideWith(wall)
    
    
    
    intro(timeElapsed)        
                
   
    
    
    
    
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit() 

