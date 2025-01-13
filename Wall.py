import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, horizontal):
        super().__init__()
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()  # Fixed this line
        self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
