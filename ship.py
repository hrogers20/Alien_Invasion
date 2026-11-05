
import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 60, 40)
        self.rect.midbottom = self.screen.get_rect().midbottom
    
    def draw_ship(self):
        pygame.draw.rect(self.screen, (0, 100, 255), self.rect)
