import pygame
from pygame import sprite

class projectile(sprite.Sprite):

    def __init__(self, x, y, facing):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("img/fireball.png")
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
        self.image2 = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.vel = 8 * facing

    def update(self):
        if self.vel < 0:
            self.image = self.image2
        self.rect.x, self.rect.y = self.x, self.y-28