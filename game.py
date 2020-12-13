import pygame
from actor import Player

pygame.init()
win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

bg = pygame.image.load('img/bg.jpg')

def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw(win)

    pygame.display.update()


if __name__ == "__main__":
    player = Player(200, 410, 64, 64)
    player.setup()

    while True:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.x > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
        elif keys[pygame.K_d] and player.x < 500 - player.width - player.vel:
            player.x += player.vel
            player.right = True
            player.left = False
        else:
            player.right = False
            player.left = False
            player.walkCount = 0

        if not(player.isJump):
            if keys[pygame.K_SPACE]:
                player.isJump = True
                player.right = False
                player.left = False
                player.walkCount = 0
        else:
            if player.jumpCount >= -10:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg
                player.jumpCount -= 1
            else:
                player.isJump = False
                player.jumpCount = 10

        redrawGameWindow()

    pygame.quit()
