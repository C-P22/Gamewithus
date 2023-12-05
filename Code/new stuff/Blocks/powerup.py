import pygame
from config import *

from Blocks.block import *


class Powerup(Block):
    def __init__(self, game, x, y):

        Block.__init__(self, x, y, (game.all_sprites, game.powerup))
        
        Block.set_color(self, BOOST_COLOR)
