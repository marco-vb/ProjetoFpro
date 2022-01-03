import pygame
from images import *
from constants import *
from bullets import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = SPACESHIP
        self.rect = self.image.get_rect(midbottom = pos)
        self.ready = True
        self.bullet_time = 0
        self.bullet_cooldown = COOLDOWN
        self.bullets = pygame.sprite.Group()



    def get_input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.x - SPEED > 0:
            self.rect.x -= SPEED
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.x + SPEED + SPWID < WID:
            self.rect.x += SPEED
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.ready:
            self.shoot()
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()
    
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.bullet_cooldown:
                self.ready = True

    def shoot(self):
        self.bullets.add(Bullet(self.rect.center))

    def update(self):
        self.get_input()
        self.recharge()
        self.bullets.update()

