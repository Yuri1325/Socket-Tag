import pygame

class Button:
    def __init__(self,x,y,img,img2,win,scale):
        self.scale= scale
        self.isHovered = False
        self.isClicked = False
        self.imgs =[img,img2]
        self.currentimage = 0
        self.scale = scale  
        
        self.width = self.imgs[self.currentimage].get_width()
        self.height = self.imgs[self.currentimage].get_height()
        self.img = pygame.transform.scale(self.imgs[self.currentimage],(int(self.width*scale), int(self.height*scale)))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        
        self.createButton(win)
    def createButton(self,win):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.isHovered = True
            if pygame.mouse.get_pressed()[0]==1:
                self.isClicked = True
            else:
                self.isClicked = False
        else:
            self.isHovered = False
        win.blit(self.img,(self.rect.x,self.rect.y))
        
    def update(self,win):
        self.width = self.imgs[self.currentimage].get_width()
        self.height = self.imgs[self.currentimage].get_height()
        self.img = pygame.transform.scale(self.imgs[self.currentimage],(int(self.width*self.scale), int(self.height*self.scale)))
        self.rect = self.img.get_rect()
        self.currentimage+=1
        if self.currentimage > 1:
            self.currentimage = 0

    