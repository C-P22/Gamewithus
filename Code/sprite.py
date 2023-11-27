import pygame
import math
from config import *
import random


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
<<<<<<< Updated upstream
        self._layer = PLAYER_LAYER  # important when we have more objekts so we know which is on top of which
        self.groups = self.game.all_sprites  # add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)
=======
        self._layer = PLAYER_LAYER # important when we have more objekts so we know which is on top of which
        self.groups = self.game.all_sprites,self.game.player# add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self,self.groups)
>>>>>>> Stashed changes

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = "down"  # movements of the character
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()  # hitbox = image the same
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
<<<<<<< Updated upstream
        self.x_change = 0
        self.y_change = 0

=======
        self.x_change = 0 
        self.y_change = 0

        if self.collide_portal():
            return True
        return False 
        
    def collide_portal(self):
        hits = pygame.sprite.spritecollide(self,self.game.portal,False)
        if hits:
            return True 
        return False
>>>>>>> Stashed changes
    def movement(self):
        key = pygame.key.get_pressed()  # checks which keys are being pressed
        if key[pygame.K_g]:  # freeze
            pass
        else:

            if key[pygame.K_LEFT]:
                # for sprite in self.game.all_sprites:
                #    sprite.rect.x += PLAYER_SPEED

                self.x_change -= CURRENT_SPEED()
                self.facing = 'left'
            if key[pygame.K_RIGHT]:
                # for sprite in self.game.all_sprites:
                #    sprite.rect.x  -= PLAYER_SPEED
                self.x_change += CURRENT_SPEED()
                self.facing = 'right'
            if key[pygame.K_UP]:
                # for sprite in self.game.all_sprites:
                #   sprite.rect.y += PLAYER_SPEED
                self.y_change -= CURRENT_SPEED()
                self.facing = 'up'
            if key[pygame.K_DOWN]:
                # for sprite in self.game.all_sprites:
                #   sprite.rect.y -= PLAYER_SPEED
                self.y_change += CURRENT_SPEED()
                self.facing = 'down'

    def collide_powerup(self):
        collide = pygame.sprite.spritecollide(self, self.game.powerup, True)
        if collide:
            print("collide")
            NEW_SPEED()
            print(PLAYER_SPEED)

    def collide_block(self, direction):

        if direction == "x":
            # False ist, ob wir den Sprite löschen wollen
            hits = pygame.sprite.spritecollide(self, self.game.blocks,
                                               False)  # prüft obt die rect zweier Sprites miteinander kollidieren
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[
                                      0].rect.left - self.rect.width  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
                    # for sprite in self.game.all_sprites:
                    #    sprite.rect.x += PLAYER_SPEED 
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right  # wir setzen self.rect.x zur rechten Ecke steht genau neben dran
                    # for sprite in self.game.all_sprites:
                    #    sprite.rect.x -= PLAYER_SPEED 
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks,
                                               False)  # prüft obt die rect zweier Sprites miteinander kollidieren
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[
                                      0].rect.top - self.rect.height  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
                    # for sprite in self.game.all_sprites:
                    # #   sprite.rect.y += PLAYER_SPEED 
                if self.y_change < 0:
                    self.rect.y = hits[
                        0].rect.bottom  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
                    # for sprite in self.game.all_sprites:
                    #    sprite.rect.y -= PLAYER_SPEED 


class Block(pygame.sprite.Sprite):
<<<<<<< Updated upstream
    def __init__(self, game, x, y, transparent):
        self.game = game
        self._layer = BLOCK_LAYER
        if transparent:
            self.groups = self.game.all_sprites, self.game.blocks
        else:
            self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
        self.height = BOXSIZE
        image_to_load = pygame.image.load(r"img/bestwall.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0, 0))

        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0
        self.rect.x = self.x
        self.rect.y = self.y


class Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
=======
    def __init__(self,game,x,y):
        self.game = game 
        self._layer = BLOCK_LAYER
        
>>>>>>> Stashed changes

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
<<<<<<< Updated upstream
        self.height = BOXSIZE
        image_to_load = pygame.image.load(r"img/floor.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0, 0))
=======
        self.height= BOXSIZE
    def get_form_img(self,Path):
        image_to_load = pygame.image.load(Path)
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))
>>>>>>> Stashed changes

        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0
        self.rect.x = self.x
<<<<<<< Updated upstream
        self.rect.y = self.y


class Powerup(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        print(x, y)
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.powerup
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
        self.height = BOXSIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BOOST)

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
=======
        self.rect.y = self.y 
    def get_form_colour(self,Color):
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(Color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Wall(Block):
    def __init__(self,game,x,y,transparent):

        Block.__init__(self,game,x,y)
        if transparent:
            self.groups = self.game.all_sprites,self.game.blocks
        else:
            self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        Block.get_form_colour(self,SAND)
class Floor(Block):
    def __init__(self,game,x,y):
        Block.__init__(self,game,x,y)
        
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        Block.get_form_img(self,"img/floorbig.png")
class Portal(Block):
    def __init__(self,game,x,y):
        Block.__init__(self,game,x,y)
        self.groups = self.game.all_sprites,self.game.portal
        pygame.sprite.Sprite.__init__(self,self.groups)
        Block.get_form_img(self,"img/portal.png")
>>>>>>> Stashed changes
