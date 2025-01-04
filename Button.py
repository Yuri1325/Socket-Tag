import pygame

class Button:
    def __init__(self,x,y,img,hoverImg,win,scale):
        self.scale= scale
        self.isHovered = False
        self.isClicked = False
        if self.isHovered:
            img = hoverImg
        else:
            img = img
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = pygame.transform.scale(img,(int(self.width*scale), int(self.height*scale)))
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
        
    