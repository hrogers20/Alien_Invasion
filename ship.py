
import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False


        self.rect = pygame.Rect(0, 0, 60, 40)
        self.rect.midbottom = self.screen.get_rect().midbottom


    def update(self):
        if self.moving_right:
            self.rect.x += 1


        if self.moving_left:
            self.rect.x -= 1


    
    def draw_ship(self):
        pygame.draw.rect(self.screen, (0, 100, 255), self.rect)
