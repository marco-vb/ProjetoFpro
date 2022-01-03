import pygame

from constants import BULLETSPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = pos)
        self.bulletspeed = BULLETSPEED
    
    def update(self):
        self.rect.y -= self.bulletspeed