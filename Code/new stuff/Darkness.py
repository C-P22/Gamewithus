import pygame
from config import *

from Block import *


class Darkness(Block):
    def __init__(self, game, x, y):

        Block.__init__(self, x, y, (game.all_sprites, game.darkness))

        Block.set_color(self, BLACK)