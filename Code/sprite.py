import pygame
from config import *


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # important when we have more objekts so we know which is on top of which
        self.groups = self.game.all_sprites  # add it to all sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * BLOCK_LAYER
        self.y = y * BOXSIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = "down"  # movments of the caracter
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()  # hitbox = image the same
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_block('x')
        self.rect.y += self.y_change
        self.collide_block('y')
        self.x_change = 0
        self.y_change = 0
        self.collide_powerup()

    def movement(self):
        key = pygame.key.get_pressed()  # checks which keys are being pressed
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

    def collide_powerup(self):
        collide = pygame.sprite.spritecollide(self,self.game.powerup,True)

    def collide_block(self, direction):
        if direction == "x":
            # False ist ob wir den Sprite löschen wollen
            hits = pygame.sprite.spritecollide(self, self.game.blocks,
                                               False)  # prüft obt die rect zweier Sprites miteinander collidieren
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[
                                      0].rect.left - self.rect.width  # wir setzen self.rect.x zu Linke Ecke und dann rechenn wir minus width von unserem player

                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right  # wir setzen self.rect.x zur rechten Ecke steht genau neben dran

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks,
                                               False)  # prüft obt die rect zweier Sprites miteinander collidieren
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[
                                      0].rect.top - self.rect.height  # wir setzen self.rect.x zu Linke Ecke und dann rechenn wir minus width von unserem player

                if self.y_change < 0:
                    self.rect.y = hits[
                        0].rect.bottom  # wir setzen self.rect.x zu Linke Ecke und dann rechenn wir minus width von unserem player


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
        self.height = BOXSIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(SAND)

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y


class POWERUP(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
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


