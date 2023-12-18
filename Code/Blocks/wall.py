import pygame
from config import *

from Blocks.block import *


class Wall(Block):
    def __init__(self, game, x, y, transparent):

        if transparent:
            groups = game.all_sprites, game.blocks
        else:
            groups = game.all_sprites, game.blocks,game.destroyable
        Block.__init__(self, x, y, groups,game)

        Block.set_color(self, SAND_COLOR)
    