
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship, screen):
        super().__init__()
        self.screen = screen
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.midbottom = ship.rect.midtop

    def update(self):
        self.rect.y -= 2

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




