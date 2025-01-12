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

z = False
introFinished = False
serverSelected = False
inGame = False
watingForPlayers = True
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("PyTag Online")
pygame.display.set_icon(pygame.image.load("images\Run/tile003.png").convert_alpha())
clock = pygame.time.Clock()
run = True
gameOver = False
plyr1Won = False
leftWall = Wall(0,300,10,600,False)
rightWall = Wall(800,300,10,600,False)
topWall = Wall(400,0,800,10,True)
bottomWall = Wall(400,600,800,10,True)
startbutton = None
wallList = [leftWall,rightWall,topWall,bottomWall]
startTime = time.time()
arial = pygame.font.SysFont("Arial",15,True)
pxlf1 = pygame.font.Font("Fonts\yoster.ttf",40)
creatingNewServer = True
snap = None

n = Network()

def intro(timeElapsed):
        global introFinished,serverSelected
        if (timeElapsed < 3):
            presentsCard = Text("Computer Science 1 2024-2025",pxlf1,(255,255,255),50,200,screen)
            presentsCard2 = Text("Presents",pxlf1,(255,255,255),280,250,screen)
        else:
            titleCard = Text("PYTAG ONLINE",pygame.font.Font("Fonts\yoster.ttf",70),(255,255,255),150,100,screen)
            startButton = Button(400,250,pygame.image.load("images\Buttons/5811aefe875733a49f167ca73a33c02a.png").convert_alpha(),pygame.image.load("images\Buttons\Screenshot 2025-01-08 134028.png").convert_alpha(),screen,0.5)
            startButton.update(screen)
            if startButton.isClicked:
                introFinished = True
                serverSelected = True
    

while run:
    global startButton 
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
            player2 = n.Send(player)
            countdown = 0
            
            if player2.gr == True:
                 watingForPlayers=False
            if watingForPlayers:
                 wfp = Text("Waiting for players..",pygame.font.Font("Fonts\yoster.ttf",40),(255,255,255),170,230,screen)
            if not gameOver:
                
                playerCords = Text(f"Player Pos {round(player.pos)}",arial,(255,255,255),10,50,screen)

                if not watingForPlayers :
                    if snap ==None:
                        snap = timeElapsed
                    tm = timeElapsed -snap
                    countdown = 3 - tm

                    if countdown > 0:
                        cntdwn = Text(str(countdown),pygame.font.Font("Fonts\yoster.ttf",40),(255,255,255),370,50,screen)

                    if countdown<=0: 
                        displayTime.txt = str(abs(countdown))
                        player.move(screen)
                        if countdown > -5:
                            if player.isTagger:
                                role = Text("You're the tagger",pygame.font.Font("Fonts\yoster.ttf",30),(255,255,255),270,50,screen)
                            else:
                                role = Text("You're the runner",pygame.font.Font("Fonts\yoster.ttf",30),(255,255,255),270,50,screen)
                        playerId = Text("You",pygame.font.Font("Fonts\yoster.ttf",10),(255,255,255),player.pos.x -10,player.pos.y - 30,screen)
                        player2Id = Text("Enemy",pygame.font.Font("Fonts\yoster.ttf",10),(255,255,255),player2.pos.x -20,player2.pos.y - 30,screen)
                        player2.update(screen)
            for wall in wallList:
                wall.draw(screen)   
            if countdown < -20:
                 if not player.isTagger:
                      player.won = True
                 else:
                    player2.won = True
                
            if(player.mask.overlap(player2.mask,(player2.pos.x - player.pos.x,player2.pos.y - player.pos.y))):
                if player.is_tagging and player.isTagger:
                    
                    
                    player.won = True
                    
                elif player2.is_tagging and player2.isTagger:
                    player2.won=True
                    
                    
            if player.won:
                gmtxt = Text("GAME OVER",pygame.font.Font("Fonts\yoster.ttf",100),(255,255,255),100,150,screen)
                gmtxgmwho = Text("You Won!!",pygame.font.Font("Fonts\yoster.ttf",30),(255,255,255),290,290,screen)
                gameOver = True
            elif player2.won:         
                gmtxt = Text("GAME OVER",pygame.font.Font("Fonts\yoster.ttf",100),(255,255,255),100,150,screen)
                gmtxgmwho = Text("You Lost  ",pygame.font.Font("Fonts\yoster.ttf",30),(255,255,255),290,290,screen)
                gameOver = True      
            if gameOver:
                 player.pos = pygame.math.Vector2(900,900)
                 player2.pos = pygame.math.Vector2(900,-900)  

        
        
        
            
            
               
                
                    

            
            
    if ((introFinished==True)and(serverSelected==True)):
                inGame = True 
    if not introFinished:
                intro(timeElapsed) 
         
                
   
    
    
    
    
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit() 

