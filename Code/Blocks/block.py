import pygame
from config import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, groups,game, layer):
        self.orginal_x = x
        self.orginal_y = y 
        # allow for overriding the layer
        self._layer = layer
        self.game = game 
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)

    def set_sprite(self, sprite_path):
        image_to_load = pygame.image.load(sprite_path)
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0, 0))

        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def set_color(self, color, alpha = 255):
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_alpha(self, alpha):
        self.image.set_alpha(alpha)

    def get_alpha(self):
        return self.image.get_alpha()
    
    def update(self):
        if self.health <= 0:
            self.killing()
    def killing(self):
        self.game.is_wall_matrix[self.orginal_x][self.orginal_y] = 0
        self.kill()

