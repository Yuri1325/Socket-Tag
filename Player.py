import pygame
import pickle
from images import*
# pygame.init()
# pygame.display.set_mode((800,600))
idleAnimation = ["images/Idle/tile000.png","images/Idle/tile001.png","images/Idle/tile002.png","images/Idle/tile003.png","images/Idle/tile004.png","images/Idle/tile005.png","images/Idle/tile006.png","images/Idle/tile007.png","images/Idle/tile008.png","images/Idle/tile009.png"]
runAnimation = ["images/Run/tile000.png","images/Run/tile001.png","images/Run/tile002.png","images/Run/tile003.png","images/Run/tile004.png","images/Run/tile005.png","images/Run/tile006.png","images/Run/tile007.png"]

playerIdle = False
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,facingRight = True):
        super().__init__()
        self.currentImage = 0
        self.currentAnimation = idleAnimation
        self.image = pygame.image.load(self.currentAnimation[self.currentImage])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.speed = 5
        self.facingRight = facingRight
    def setAnimation_Idle(self):
        self.currentAnimation = idleAnimation
    def setAnimation_Run(self):
        self.currentAnimation = runAnimation

    def move(self,win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 5:
            self.facingRight = False
            self.setAnimation_Run()
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x<780:
            self.facingRight = True
            self.setAnimation_Run()
            self.x += self.speed
        if keys[pygame.K_UP] and self.y >20:
            self.setAnimation_Run()
            self.y -= self.speed
        if keys[pygame.K_DOWN]and self.y < 560:
            self.setAnimation_Run()
            self.y += self.speed
        if not(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] or keys[pygame.K_UP]):
            self.setAnimation_Idle()
        
            

        self.update(win)

    def update(self,win):
        self.rect.center = (self.x, self.y)
        self.currentImage+=1
        if self.currentImage>= len(self.currentAnimation):
            self.currentImage = 0

        
        self.image = pygame.image.load(self.currentAnimation[self.currentImage]).convert_alpha()
        if self.facingRight:
            win.blit(self.image,self.rect)
        else:
           win.blit(pygame.transform.flip(self.image,True,False),self.rect) 
        
    # Custom methods for pickling
    def __getstate__(self):
        state = self.__dict__.copy()
        # Exclude the non-serializable attributes
        del state['image']
        del state['rect']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Recreate the non-serializable attributes
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    