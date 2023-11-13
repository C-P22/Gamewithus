import pygame
import math 
from config import *
import random

class Player(pygame.sprite.Sprite):

    def __init__(self,game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER # important when we have more objekts so we know which is on top of which
        self.groups = self.game.all_sprites# add it to all sprite group
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x *TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE 
        self.x_change = 0 
        self.y_change = 0 
        self.facing = "down" # movments of the caracter
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect() # hitbox = image the same 
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0 
        self.y_change = 0 
    def movement(self):
        key = pygame.key.get_pressed()#checks which keys are being pressed
        if key[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if key[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if key[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if key[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'