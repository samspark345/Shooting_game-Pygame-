import pygame
from pygame import sprite

screen_width, screen_height = 1000, 480


class Actor(sprite.Sprite):
    def __init__(self, x, y, width, height, role):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.walkRightSprites = []
        self.walkLeftSprites = []
        self.standing = None
        self.facing = 1
        self.bullets = []
        self.hitbox = (self.x + 16, self.y + 12, self.width-24, self.height-10)
        self.image_set = False
        self.role = role

    #create walkRight image array
    def setup(self):
        if self.role == "player":
            for num in range(1, 10):
                self.walkRightSprites.append(pygame.image.load('img/'+self.role +'/right_walk/R'+str(num)+'.png'))

            for num in range(1, 10):
                self.walkLeftSprites.append(pygame.image.load('img/'+self.role +'/left_walk/L'+str(num)+'.png'))
        else:
            for num in range(1, 12):
                self.walkRightSprites.append(pygame.image.load('img/'+self.role +'/right_walk/R'+str(num)+'.png'))

            for num in range(1, 12):
                self.walkLeftSprites.append(pygame.image.load('img/'+self.role +'/left_walk/L'+str(num)+'.png'))

    def update(self):
        # why this 27?
        self.image_set = True
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            self.image = self.walkLeftSprites[self.walkCount//3]
            self.rect, self.rect.x, self.rect.y = self.image.get_rect(), self.x, self.y
            self.walkCount += 1
        elif self.right:
            self.image = self.walkRightSprites[self.walkCount//3]
            self.rect, self.rect.x, self.rect.y = self.image.get_rect(), self.x, self.y
            self.walkCount += 1
        else:
            if self.facing == 1:
                self.image = self.walkRightSprites[0]
                self.rect, self.rect.x, self.rect.y = self.image.get_rect(), self.x, self.y

            else:
                self.image = self.walkLeftSprites[0]
                self.rect, self.rect.x, self.rect.y = self.image.get_rect(), self.x, self.y

    def walkLeft(self):
        if self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.facing = -1

    def walkRight(self):
        if self.x < screen_width - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
            self.facing = 1

    def stop(self):
        self.walkCount = 0

    def jump(self, keys):
        if not(self.isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def life_update(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x-1, self.y, 62, 10), 1)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 60, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.life, 10))

class Player(Actor):
    def __init__(self, x, y, width, height):
        Actor.__init__(self, x, y, width, height, "player")
        self.life = 60


class Enemy(Actor):
    def __init__(self, x, y, width, height):
        Actor.__init__(self, x, y, width, height, "enemy")
        self.facing = -1
        self.life = 60
        self.endpos = screen_width - self.width - self.vel
        self.left = True
        self.right = False

    def move(self):
        if self.left:
            self.walkLeft()
        else:
            self.walkRight()

    def enemy_tracking(self):
        if self.x >= self.endpos and self.facing == 1 and self.right:
            self.right, self.left = False, True
        elif self.x <= 0+self.vel and self.facing == -1 and self.left:
            self.right, self.left = True, False

    def update(self):
        # why this 27?
        self.image_set = True
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.left:
            self.image = self.walkLeftSprites[self.walkCount//3]
            self.image.set_colorkey((0, 0, 0))
            self.rect, self.rect.x, self.rect.y = self.image.get_rect(), self.x, self.y
            self.walkCount += 1
        elif self.right:
            self.image = self.walkRightSprites[self.walkCount//3]
            self.image.set_colorkey((0, 0, 0))
            self.rect, self.rect.x, self.rect.y = self.image.get_rect(), self.x, self.y
            self.walkCount += 1
