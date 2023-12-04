import pygame
from config import *

from Block import *


class Portal(Block):
    def __init__(self, game, x, y):

        Block.__init__(self, x, y, (game.all_sprites, game.portal))

        Block.set_sprite(self, PORTAL_SPRITE_PATH)
