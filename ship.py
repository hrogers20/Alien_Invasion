
import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("Assets/images/ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.moving_right = False
        self.moving_left = False

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom


    
    def update(self):
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.rect.x += 1

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1



      
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

