import pygame
from config import *


class TitleScreen(pygame.sprite.Sprite):
    def __init__(self, groups):
        # self.orginal_x = x
        # self.orginal_y = y 
        # # allow for overriding the layer
        # self._layer = layer
        # self.game = game 
        # self.x = x * TILE_SIZE
        # self.y = y * TILE_SIZE
        # self.width = TILE_SIZE
        # self.height = TILE_SIZE

        # self.groups = groups
        pygame.sprite.Sprite.__init__(self, groups)