import pygame
import pickle
import time
from images import*

# pygame.init()
# pygame.display.set_mode((800,600))
idleAnimation = ["images/Idle/tile000.png","images/Idle/tile001.png","images/Idle/tile002.png","images/Idle/tile003.png","images/Idle/tile004.png","images/Idle/tile005.png","images/Idle/tile006.png","images/Idle/tile007.png","images/Idle/tile008.png","images/Idle/tile009.png"]
runAnimation = ["images/Run/tile000.png","images/Run/tile001.png","images/Run/tile002.png","images/Run/tile003.png","images/Run/tile004.png","images/Run/tile005.png","images/Run/tile006.png","images/Run/tile007.png"]
rollAnimation = ["images/Roll/tile000.png","images/Roll/tile001.png","images/Roll/tile002.png","images/Roll/tile003.png","images/Roll/tile004.png","images/Roll/tile005.png","images/Roll/tile006.png"]
vector = pygame.math.Vector2
playerIdle = False
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,facingRight = True):
        super().__init__()
        self.currentImage = 0
        self.currentAnimation = idleAnimation

        self.image = pygame.transform.scale(pygame.image.load(self.currentAnimation[self.currentImage]),(92,92))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        
        self.x = x
        self.y = y
        self.pos = vector(self.x,self.y)
        self.velocity = vector(0,0)
        self.aceleration = vector(0,0)
        self.H_aceleration =3
        self.H_friction = 0.25
        self.V_aceleration =3
        self.V_friction = 0.25
        self.last_roll_time = 0  
        self.roll_cooldown = 3   
        self.is_rolling = False 
        self.roll_duration = 0.5
        self.roll_speed = 10
        self.speed = 10
        self.facingRight = facingRight
        self.collidingFromUnder = False
        self.collidingFromTop = False
        self.collidingFromLeft = False
        self.collidingFromRight = False
        
        
        self.offX = self.pos.x - self.rect.left
        self.offY = self.pos.y - self.rect.top
    def setAnimation_Idle(self):
        self.currentAnimation = idleAnimation
    def setAnimation_Run(self):
        self.currentAnimation = runAnimation
        
    def setAnimation_Roll(self):
        self.currentAnimation = rollAnimation
    def move(self,win):
        keys = pygame.key.get_pressed()

        # Initialize acceleration
        self.aceleration = vector(0, 0)

        # Get current time
        current_time = time.time()

        # Handle rolling
    
        if keys[pygame.K_SPACE] and not self.is_rolling and current_time - self.last_roll_time >= self.roll_cooldown:
            self.last_roll_time = current_time
            self.is_rolling = True
            self.setAnimation_Roll()

            # Set rolling velocity based on facing direction
            if self.facingRight:
                self.velocity.x = self.roll_speed
            else:
                self.velocity.x = -self.roll_speed

            # Optional: Set vertical velocity for vertical rolls
            self.velocity.y = 0

        # End rolling after the roll duration
        if self.is_rolling and current_time - self.last_roll_time >= self.roll_duration:
            self.is_rolling = False
            self.velocity.x = 0  # Stop horizontal rolling movement

        # Handle normal movement if not rolling
        if not self.is_rolling:
            # Horizontal movement

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                if not self.collidingFromRight:
                    self.aceleration.x = -self.H_aceleration 
                else:
                    self.aceleration.x = self.H_aceleration
                
                self.facingRight = False
                self.setAnimation_Run()
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                #put code here to detect if the player is touching a wall while moving right
                #if the player touches a wall while moving right, change the player position
                #by the x acceleration multiplied by negative one, so when they move right
                #by like 10 steps, then they move back 10 steps, meaning they dont move at all
                if not self.collidingFromLeft:
                    self.aceleration.x = self.H_aceleration
                else:
                   self.aceleration.x = -self.H_aceleration
                self.facingRight = True
                
                self.setAnimation_Run()

        # Vertical movement
            if (keys[pygame.K_UP] or keys[pygame.K_w]):
                
                if not self.collidingFromUnder:
                    self.aceleration.y = -self.V_aceleration
                else: 
                    self.aceleration.y = self.V_aceleration
                
                
                self.setAnimation_Run()
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
               
                if not self.collidingFromTop:
                    self.aceleration.y = self.V_aceleration
                else:
                    self.aceleration.y = -self.V_aceleration
                
                self.setAnimation_Run()

            # Normalize diagonal movement
            if self.aceleration.x != 0 and self.aceleration.y != 0:
                self.aceleration = self.aceleration.normalize() * self.H_aceleration

            # Set idle animation if no movement
            if self.aceleration.x == 0 and self.aceleration.y == 0:
                self.setAnimation_Idle()

        # Update position and render
        self.update(win)

            
        
            

       
    
        
       
            
           
            
            
           
            
            
            
    def update(self,win):
        
        if not self.is_rolling:
            self.aceleration.x -= self.velocity.x * self.H_friction
            self.aceleration.y -= self.velocity.y * self.V_friction
       
        
        self.velocity+= self.aceleration
        self.pos += self.velocity + (self.aceleration)/2
        self.rect.center = self.pos
        self.currentImage+=1
        if self.currentImage>= len(self.currentAnimation):
            self.currentImage = 0
            
        
        
        
        self.image = pygame.image.load(self.currentAnimation[self.currentImage]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        if self.facingRight:
            win.blit(self.image,self.rect)
        else:
           win.blit(pygame.transform.flip(self.image,True,False),self.rect) 
        self.offX = self.pos.x - self.rect.left
        self.offY = self.pos.y - self.rect.top
    
           
        
    # Custom methods for pickling
    def __getstate__(self):
        state = self.__dict__.copy()
        # Exclude the non-serializable attributes
        del state['image']
        del state['rect']
        del state['mask']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Recreate the non-serializable attributes
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x,self.pos.y)
        self.mask = pygame.mask.from_surface(self.image)
    
    


  