import sys
import pygame
from ship import Ship
from bullet import Bullet


if __name__ == '__main__':
    pygame.init()
    laser_sound = pygame.mixer.Sound("Assets/sound/laser.mp3")
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    ship = Ship(screen)
    bullets = pygame.sprite.Group()

    while True:
        screen.fill(bg_color)
        ship.update()
        ship.draw_ship()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)


        for bullet in bullets:
            bullet.draw_bullet()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True 
                elif event.key == pygame.K_SPACE:
                    bullets.add(Bullet(ship, screen))
                    laser_sound.play()




            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False                
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False




       