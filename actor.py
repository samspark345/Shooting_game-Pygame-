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
        self.walkRight = []
        self.walkLeft = []
        self.standing = None
        self.role = role

    #create walkRight image array
    def setup(self):
        for num in range(1,10) :
            self.walkRight.append(pygame.image.load('img/'+self.role +'/right_walk/R'+str(num)+'.png'))
        
        for num in range(1,10) :
            self.walkLeft.append(pygame.image.load('img/'+self.role +'/left_walk/L'+str(num)+'.png'))
        
        #there is no standing for the enemy though?
        self.standing = pygame.image.load('img/'+self.role +'/standing.png')

    def draw(self, win):
        # why this 27?
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.standing, (self.x, self.y))

    def walkLeft(self):
        pass

    def walkRight(self):
        pass

    def jump(self):
        pass

class Player(Actor):
    def __init__(self, x, y, width, height):
        Actor.__init__(self, x, y, width, height, "player")


class Enemy(Actor):
    def __init__(self, x, y, width, height):
        Actor.__init__(self, x, y, width, height, "enemy")