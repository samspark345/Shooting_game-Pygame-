import pygame, random
from actor import Player, Enemy
from pygame import sprite
from projectile import projectile

screen_width, screen_height = 1000, 580


pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

bg = pygame.image.load('img/bg.jpg')
bg_size = bg.get_size()
bg = pygame.transform.scale(bg, (int(bg_size[0]*2), int(bg_size[1])+100))


def redrawGameWindow():
    win.blit(bg, (0, 0))
    enemy.life_update(win), player.life_update(win)
    allsprites.update()
    allsprites.draw(win)

    pygame.display.update()

if __name__ == "__main__":
    player = Player(200, 500, 64, 64)
    player.setup()
    enemy = Enemy(screen_width - player.width - player.vel, 500, 64, 64)
    enemy.setup()
    shoottimer = 0
    bullets = sprite.Group()
    allsprites = sprite.Group()
    allsprites.add(player, enemy)
    hit_timer = 0
    font = pygame.font.SysFont('comicsans', 60, True)
    Gameover = False
    run = True

    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if Gameover:
            text = font.render("GAME OVER", 1, (0, 0, 0))
            win.blit(text, (350, screen_height//2))
            pygame.display.update()
        else:
            keys = pygame.key.get_pressed()

            if shoottimer >= 3:
                shoottimer = 0
            elif shoottimer > 0:
                shoottimer += 1

            if keys[pygame.K_s] and len(bullets) < 3 and shoottimer == 0:
                bullet = projectile(round(player.x + player.width//2), round(player.y + player.height//2), player.facing)
                bullets.add(bullet)
                allsprites.add(bullet)
                shoottimer += 1

            for bullet in bullets:
                if bullet.x < screen_width and bullet.x > 0:
                    bullet.x += bullet.vel
                    collision = sprite.collide_rect(bullet, enemy)
                    if collision:
                        allsprites.remove(bullet), bullets.remove(bullet)
                        enemy.life -= 12

                else:
                    bullets.remove(bullet)
                    allsprites.remove(bullet)

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


            # player hit ####
            if (player.image_set and enemy.image_set) and sprite.collide_rect(player, enemy) and hit_timer == 0:
                player.life -= 6
                hit_timer += 1
            if hit_timer > 0:
                if hit_timer + 1 > 5:
                    hit_timer = 0
                else:
                    hit_timer += 1
            if player.life <= 0:
                Gameover = True

            #### enemy ####
            endpos = screen_width - player.width - player.vel
            if not(allsprites.has(enemy)):
                xpos = ([endpos, player.vel])
                enemy = Enemy(xpos[random.randint(0, 1)], 500, 64, 64)
                if xpos == endpos:
                    enemy.facing, enemy.left, enemy.right = -1, True, False
                else:
                    enemy.facing, enemy.left, enemy.right = 1, False, True
                enemy.setup()
                allsprites.add(enemy)
            else:
                enemy.enemy_tracking()

            if enemy.life == 0:
                allsprites.remove(enemy)
                enemy.image_set = False
            else:
                enemy.move()

            redrawGameWindow()

    pygame.quit()
