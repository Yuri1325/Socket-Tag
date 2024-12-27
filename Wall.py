import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255,255,255)
        self.image = pygame.Surface((self.width,self.height))
        self.rect = pygame.Surface.get_rect(self.image)
    def draw(self,win):
        self.rect.center = (self.x,self.y)
        pygame.draw.rect(win,self.color,self.rect)

