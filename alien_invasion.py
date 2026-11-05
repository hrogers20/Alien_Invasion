import sys
import pygame
from ship import Ship

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    ship = Ship(screen)

    while True:
        screen.fill(bg_color)
        ship.update()
        ship.draw_ship()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

                
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False




        pygame.display.flip()