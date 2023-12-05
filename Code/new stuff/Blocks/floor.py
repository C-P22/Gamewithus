import pygame
from config import *

from Blocks.block import *


class Floor(Block):
    def __init__(self, game, x, y):

        Block.__init__(self, x, y, game.all_sprites)

        Block.set_sprite(self, FLOOR_SPRITE_PATH)
