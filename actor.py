import pygame

class Actor(object):
    def __init__(self, x, y, width, height, role):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 5
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
        self.role = role

    #create walkRight image array
    def setup(self):
        for num in range(1,10) :
            self.walkRightSprites.append(pygame.image.load('img/'+self.role +'/right_walk/R'+str(num)+'.png'))
        
        for num in range(1,10) :
            self.walkLeftSprites.append(pygame.image.load('img/'+self.role +'/left_walk/L'+str(num)+'.png'))
        

    def draw(self, win):
        # why this 27?
        if self.walkCount + 1 >= 27 and self.role == "player":
            self.walkCount = 0
        
        else:
            if self.walkCount + 1 >= 28:
             self.walkCount = 0

        if self.left:
            win.blit(self.walkLeftSprites[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRightSprites[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.facing == 1:
                win.blit(self.walkRightSprites[0], (self.x, self.y))

            else:
                win.blit(self.walkLeftSprites[0], (self.x, self.y))
        self.hitbox = (self.x + 16, self.y+12, self.width-24, self.height-10)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

    def walkLeft(self):
        if self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.facing = -1

    def walkRight(self):
        if self.x < 500 - self.width - self.vel:
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
        
class projectile(object):

    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = 8 * facing 

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x, self.y), self.radius)


class Player(Actor):
    def __init__(self, x, y, width, height):
        Actor.__init__(self, x, y, width, height, "player")


class Enemy(Actor):
    def __init__(self, x, y, width, height):
        Actor.__init__(self, x, y, width, height, "enemy")
    
    def move(self):
        if self.left:
            self.walkLeft()
        else:
            self.walkRight()
    
    