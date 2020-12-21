import pygame
from actor import Player, projectile

pygame.init()
win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

bg = pygame.image.load('img/bg.jpg')

def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw(win)

    pygame.display.update()

if __name__ == "__main__":
    player = Player(200, 410, 64, 64)
    player.setup()
    run = True
    
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s] and len(player.bullets) < 5:
            player.bullets.append(projectile(round(player.x + player.width//2), round(player.y + player.height//2), 3, player.facing))
        
        for bullet in player.bullets:
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                player.bullets.remove(bullet)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.facing = -1
            player.walkLeft()
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.facing = 1
            player.walkRight()
        elif keys[pygame.K_x]:
            run = False
        else:
            player.stop()

        player.jump(keys)

        redrawGameWindow()

    pygame.quit()
