import pygame

class Text:
    def __init__(self,txt,font,color,x,y,screen):
        self.txt = txt
        self.font = font
        
        self.color = color
        self.x = x
        self.y = y
        self.screen = screen
        self.img = ""
        self.createText()
    def createText(self):
        self.img = self.font.render(self.txt,True,self.color)
        self.screen.blit(self.img,(self.x,self.y))
        
        
