import pygame
from config import *

from Blocks.block import *


class Portal(Block):
    def __init__(self, game, x, y):

        Block.__init__(self, x, y, (game.all_sprites, game.portal), game, PORTAL_LAYER)

        Block.set_sprite(self, PORTAL_SPRITE_PATH)
