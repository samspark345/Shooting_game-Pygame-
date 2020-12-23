import pygame, random
from actor import Player, projectile, Enemy

pygame.init()
win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

bg = pygame.image.load('img/bg.jpg')

def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw(win)
    if len(enemy) > 0:
        enemy[0].draw(win)
    for bullet in player.bullets:
        bullet.draw(win)

    pygame.display.update()

if __name__ == "__main__":
    player = Player(200, 410, 64, 64)
    player.setup()
    enemy = []
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
            if len(enemy) > 0 and(bullet.y - bullet.radius < enemy[0].hitbox[1] + enemy[0].hitbox[3]) and (bullet.y + bullet.radius > enemy[0].hitbox[1]):
                if  (bullet.x - bullet.radius > enemy[0].hitbox[0]) and (bullet.x - bullet.radius < enemy[0].hitbox[0] + enemy[0].hitbox[2]):
                    player.bullets.remove(bullet)
                    enemy[0].life -= 12
                    print("you have been hit")

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


        #### enemy ####
        endpos = 500 - player.width - player.vel
        if len(enemy) < 1:
            xpos = ([endpos, player.vel])
            enemy.append(Enemy(xpos[random.randint(0, 1)], 410, 64, 64))
            if xpos == endpos:
                enemy[0].facing, enemy[0].left, enemy[0].right = -1, True, False
            else:
                enemy[0].facing, enemy[0].left, enemy[0].right = 1, False, True
            enemy[0].setup()
        else:
            if enemy[0].x >= endpos and enemy[0].facing == 1 and enemy[0].right:
                enemy[0].right, enemy[0].left = False, True
            elif enemy[0].x <= 0+player.vel and enemy[0].facing == -1 and enemy[0].left:
                enemy[0].right, enemy[0].left = True, False
        
        if enemy[0].life == 0:
            enemy.pop()
        else:
            enemy[0].move()

        redrawGameWindow()

    pygame.quit()
