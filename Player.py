import pygame
import pickle

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.speed = 0.1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        self.update()

    def update(self):
        self.rect.center = (self.x, self.y)

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
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)