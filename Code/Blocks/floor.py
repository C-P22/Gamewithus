import pygame
from config import *

from Blocks.block import *


class Floor(Block):
    def __init__(self, game, x, y, is_hidden_floor = False):

        if is_hidden_floor:
            layer = HIDDEN_FLOOR_LAYER
        else:
            layer = FLOOR_LAYER
        
        Block.__init__(self, x, y, game.all_sprites, game, layer)

        Block.set_sprite(self, FLOOR_SPRITE_PATH)
