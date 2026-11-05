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
        ship.draw_ship()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()