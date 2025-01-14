import pygame
import pickle
import time
from images import*

# pygame.init()
# pygame.display.set_mode((800,600))
idleAnimation = ["images/Idle/tile000.png","images/Idle/tile001.png","images/Idle/tile002.png","images/Idle/tile003.png","images/Idle/tile004.png","images/Idle/tile005.png","images/Idle/tile006.png","images/Idle/tile007.png","images/Idle/tile008.png","images/Idle/tile009.png"]
runAnimation = ["images/Run/tile000.png","images/Run/tile001.png","images/Run/tile002.png","images/Run/tile003.png","images/Run/tile004.png","images/Run/tile005.png","images/Run/tile006.png","images/Run/tile007.png"]
rollAnimation = ["images/Roll/tile000.png","images/Roll/tile001.png","images/Roll/tile002.png","images/Roll/tile003.png","images/Roll/tile004.png","images/Roll/tile005.png","images/Roll/tile006.png"]
tagAnimation = ["images/Tag/tile000.png","images/Tag/tile001.png","images/Tag/tile002.png","images/Tag/tile003.png","images/Tag/tile004.png","images/Tag/tile005.png","images/Tag/tile006.png","images/Tag/tile007.png","images/Tag/tile008.png"]
vector = pygame.math.Vector2
playerIdle = False
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,id,won,tagger,gr,facingRight = True,):
        super().__init__()
        self.currentImage = 0
        self.currentAnimation = idleAnimation
        self.id = id 
        self.gr =gr
        self.isTagger = tagger
        self.image = pygame.transform.scale(pygame.image.load(self.currentAnimation[self.currentImage]),(92,92))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.won = won
        self.x = x
        self.y = y
        self.pos = vector(self.x,self.y)
        self.velocity = vector(0,0)
        self.aceleration = vector(0,0)
        self.H_aceleration =3
        self.H_friction = 0.2
        self.V_aceleration =3
        self.V_friction = 0.2
        self.last_roll_time = 0  
        self.roll_cooldown = 3   
        self.is_rolling = False 
        self.roll_duration = 0.28
        self.roll_speed = 15
        #--------------------
        self.last_tag_time = 0  
        self.tag_cooldown = 3   
        self.is_tagging = False 
        self.tag_duration = 0.28
        self.tag_speed = 50

        self.speed = 10
        self.facingRight = facingRight
        
        
        
        self.offX = self.pos.x - self.rect.left
        self.offY = self.pos.y - self.rect.top
    def setAnimation_Idle(self):
        self.currentAnimation = idleAnimation
    def setAnimation_Run(self):
        self.currentAnimation = runAnimation
        
    def setAnimation_Roll(self):
        self.currentAnimation = rollAnimation
    def setAnimation_Tag(self):
        self.currentAnimation = tagAnimation
    def move(self,win,walls):
        keys = pygame.key.get_pressed()

        # Initialize acceleration
        self.aceleration = vector(0, 0)

        # Get current time
        current_time = time.time()

        # Handle rolling
    
        if (keys[pygame.K_x]or keys[pygame.K_k]) and (not self.is_rolling and not self.is_tagging) and current_time - self.last_roll_time >= self.roll_cooldown:
            self.last_roll_time = current_time
            self.is_rolling = True
            self.setAnimation_Roll()

            # Set rolling velocity based on facing direction
            if self.facingRight:
                self.velocity.x = self.roll_speed
            else:
                self.velocity.x = -self.roll_speed

            # Optional: Set vertical velocity for vertical rolls
            # self.velocity.y = 0

        # End rolling after the roll duration
        if self.is_rolling and current_time - self.last_roll_time >= self.roll_duration:
            self.is_rolling = False
            self.velocity.x = 0  # Stop horizontal rolling movement
        #----------------------------------------------------------------------------
        if (keys[pygame.K_z]or keys[pygame.K_j]) and (not self.is_tagging and not self.is_rolling) and current_time - self.last_tag_time >= self.tag_cooldown:
            self.last_tag_time = current_time
            self.is_tagging = True
            self.setAnimation_Tag()

            # Set rolling velocity based on facing direction
            if self.facingRight:
                self.velocity.x = self.tag_speed
            else:
                self.velocity.x = -self.tag_speed

            # Optional: Set vertical velocity for vertical rolls
            

        # End rolling after the roll duration
        if self.is_tagging and current_time - self.last_tag_time >= self.tag_duration:
            self.is_tagging = False
            self.velocity.x = 0  # Stop horizontal rolling movement
        # Handle normal movement if not rolling
        if not self.is_rolling and not self.is_tagging:
            # Horizontal movement

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                
                self.aceleration.x = -self.H_aceleration 
                
                
                self.facingRight = False
                self.setAnimation_Run()
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                #put code here to detect if the player is touching a wall while moving right
                #if the player touches a wall while moving right, change the player position
                #by the x acceleration multiplied by negative one, so when they move right
                #by like 10 steps, then they move back 10 steps, meaning they dont move at all
                
                self.aceleration.x = self.H_aceleration
                
                self.facingRight = True
                
                self.setAnimation_Run()

        # Vertical movement
            if (keys[pygame.K_UP] or keys[pygame.K_w]):
                
                
                self.aceleration.y = -self.V_aceleration
                
                
                
                self.setAnimation_Run()
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
               
                
                self.aceleration.y = self.V_aceleration
                
                
                self.setAnimation_Run()

            # Normalize diagonal movement
            if self.aceleration.x != 0 and self.aceleration.y != 0:
                self.aceleration = self.aceleration.normalize() * self.H_aceleration

            # Set idle animation if no movement
            if self.aceleration.x == 0 and self.aceleration.y == 0:
                self.setAnimation_Idle()
        self.check_wall_collision(walls)
        # Update position and render
        self.update(win)

            
        
            

       
    
        
       
            
           
            
            
           
            
    def check_wall_collision(self, walls):
        # Horizontal movement collision
              # Update rect's horizontal position
             
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if self.velocity.x > 0 and self.pos.x < wall.rect.x:  # Moving right
                        
                        self.pos.x -= self.velocity.x + (self.aceleration.x)/2
                        
                    elif self.velocity.x < 0 and self.pos.x > wall.rect.x:  # Moving left
                        
                        self.pos.x -= self.velocity.x + (self.aceleration.x)/2
                        
                    self.velocity.x =0
                    
                    break  # Only resolve the first collision

            # Vertical movement collision
            
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if self.velocity.y > 0 and self.pos.y < wall.rect.y:  # Moving down
                       
                        self.pos.y -= self.velocity.y + (self.aceleration.y)/2
                        
                    elif self.velocity.y < 0 and self.pos.y > wall.rect.y:  # Moving up
    
                        self.pos.y -= self.velocity.y + (self.aceleration.y)/2
                    
                    self.velocity.y = 0
                    break  # Only resolve the first collision
            
                     
                    
                     
                    
                

            # Update rect to match corrected position
            self.rect.center = self.pos

                
                    

            
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
    
    


  