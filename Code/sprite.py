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

        self.x = x *BOXSIZE
        self.y = y * BOXSIZE
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
        key = pygame.key.get_pressed()
        self.rect.x += self.x_change
        if key[pygame.K_c]:
            pass
        else:
            self.collide_block('x')

        self.rect.y += self.y_change

        if key[pygame.K_c]:
            pass
        else:
            self.collide_block('y')
        self.x_change = 0 
        self.y_change = 0 
    def movement(self):
        key = pygame.key.get_pressed()#checks which keys are being pressed
        if key[pygame.K_g]:#freez 
            pass
        else:

            if key[pygame.K_LEFT]:
                #for sprite in self.game.all_sprites:
                #    sprite.rect.x += PLAYER_SPEED
                    
                self.x_change -= PLAYER_SPEED
                self.facing = 'left'
            if key[pygame.K_RIGHT]:
                #for sprite in self.game.all_sprites:
                #    sprite.rect.x  -= PLAYER_SPEED
                self.x_change += PLAYER_SPEED
                self.facing = 'right'
            if key[pygame.K_UP]:
                #for sprite in self.game.all_sprites:
                #   sprite.rect.y += PLAYER_SPEED
                self.y_change -= PLAYER_SPEED
                self.facing = 'up'
            if key[pygame.K_DOWN]:
                #for sprite in self.game.all_sprites:
                #   sprite.rect.y -= PLAYER_SPEED
                self.y_change += PLAYER_SPEED
                self.facing = 'down'
    def collide_block(self,direction):

        if direction == "x":
            # False ist ob wir den Sprite llschen wollen 
            hits = pygame.sprite.spritecollide(self,self.game.blocks,False) # prüft obt die rect zweier Sprites miteinander collidieren 
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left -self.rect.width# wir setzen self.rect.x zu Linke Ecke und dann rechenn wir minus width von unserem player
                    #for sprite in self.game.all_sprites:
                    #    sprite.rect.x += PLAYER_SPEED 
                if self.x_change < 0:  
                    self.rect.x = hits[0].rect.right# wir setzen self.rect.x zur rechten Ecke steht genau neben dran  
                    #for sprite in self.game.all_sprites:
                    #    sprite.rect.x -= PLAYER_SPEED 
        if direction == "y":
            hits = pygame.sprite.spritecollide(self,self.game.blocks,False) # prüft obt die rect zweier Sprites miteinander collidieren 
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top -self.rect.height# wir setzen self.rect.x zu Linke Ecke und dann rechenn wir minus width von unserem player
                    #for sprite in self.game.all_sprites:
                    # #   sprite.rect.y += PLAYER_SPEED 
                if self.y_change < 0:  
                    self.rect.y = hits[0].rect.bottom # wir setzen self.rect.x zu Linke Ecke und dann rechenn wir minus width von unserem player
                    #for sprite in self.game.all_sprites:
                    #    sprite.rect.y -= PLAYER_SPEED 
class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y,transparent):
        self.game = game 
        self._layer = BLOCK_LAYER
        if transparent:
            self.groups = self.game.all_sprites,self.game.blocks
        else:
            self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x*BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
        self.height= BOXSIZE
        image_to_load = pygame.image.load(r"C:\Users\carlc\OneDrive\Dokumente\GitHub\Gamewithus\Code\img\bestwall.png")
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))

        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0 
        self.rect.x = self.x
        self.rect.y = self.y 
class Floor(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game 
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x*BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
        self.height= BOXSIZE
        image_to_load = pygame.image.load(r"C:\Users\carlc\OneDrive\Dokumente\GitHub\Gamewithus\Code\img\floor.png")
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))

        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0 
        self.rect.x = self.x
        self.rect.y = self.y 