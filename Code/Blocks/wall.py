import pygame
from config import *

from Blocks.block import *


class Wall(Block):
    def __init__(self, game, x, y, is_transparent, is_hidden = False):
        
        self.health = 3

        if is_transparent:
            groups = game.all_sprites, game.blocks
        else:
            groups = game.all_sprites, game.blocks ,game.destroyable
        
        if (is_hidden):
            layer = HIDDEN_WALL_LAYER
        else:
            layer = WALL_LAYER

        Block.__init__(self, x, y, groups, game, layer)

        Block.set_color(self, SAND_COLOR)
    
