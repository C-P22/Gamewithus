import pygame
import math 
from config import *
import random

class Player(pygame.sprite.Sprite):

    def __init__(self,game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER # important when we have more objekts so we know which is on top of which
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x *TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE 

        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect() # hitbox = image the same 
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        pass
