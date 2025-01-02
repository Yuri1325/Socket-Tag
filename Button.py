import pygame

class Button:
    def __init__(self,x,y,img,win,scale,mpos):
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = pygame.transform.scale(img,(int(self.width*scale), int(self.height*scale)))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        self.createButton(win,mpos)
    def createButton(self,win,mpos):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                print("click")
        win.blit(self.img,(self.rect.x,self.rect.y))