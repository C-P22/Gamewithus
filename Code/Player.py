import pygame
import math

from config import *
from Character import *


class Player(pygame.sprite.Sprite, Character):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # important when we have more objekts, so we know which is on top of which
        self.groups = self.game.all_sprites, self.game.player  # add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = ENTITY_SIZE
        self.height = ENTITY_SIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = "down"  # movements of the character
        self.rect = self.image.get_rect()  # hit box = image the same
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.is_overlapping_with_portal = False

        self.light_range = PLAYER_LIGHT_RANGE

    def update(self):
        self.movement()
        self.collide_enemy()
        key = pygame.key.get_pressed()
        self.collide_tile(key[pygame.K_c], 7)
        self.collide_powerup()
        if self.collide_portal():
            self.is_overlapping_with_portal = True
        else:
            self.is_overlapping_with_portal = False

    def collide_tile(self, ignore_walls, sub_step_count):
        if ignore_walls:
            self.rect.x += self.x_change
            self.rect.y += self.y_change

            self.x_change = 0
            self.y_change = 0
            return

        for i in range(sub_step_count):
            self.rect.x += self.x_change / sub_step_count
            self.collide_block('x')

            self.rect.y += self.y_change / sub_step_count
            self.collide_block('y')

        self.x_change = 0
        self.y_change = 0

    def collide_portal(self):
        hits = pygame.sprite.spritecollide(self, self.game.portal, False)
        if hits:
            return True
        return False

    def movement(self):
        key = pygame.key.get_pressed()  # checks which keys are being pressed
        if key[pygame.K_g]:  # freeze
            pass
        else:

                # for sprite in self.game.all_sprites:
                #    sprite.rect.x += PLAYER_SPEED

                self.x_change -= CURRENT_SPEED()
                self.facing = 'left'
                # for sprite in self.game.all_sprites:
                #    sprite.rect.x  -= PLAYER_SPEED
                self.x_change += CURRENT_SPEED()
                self.facing = 'right'
                # for sprite in self.game.all_sprites:
                #   sprite.rect.y += PLAYER_SPEED
                self.y_change -= CURRENT_SPEED()
                self.facing = 'up'
            if key[pygame.K_DOWN]:
                # for sprite in self.game.all_sprites:
                #   sprite.rect.y -= PLAYER_SPEED
                self.y_change += CURRENT_SPEED()
                self.facing = 'down'

    def collide_powerup(self):  # NEUE FUNKTION
        collide = pygame.sprite.spritecollide(self, self.game.powerup, True)
        if collide:
            NEW_SPEED()

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            NEW_HEALTH()
            if NEW_HEALTH() == 0:
                self.kill()
                self.game.playing = False

    def collide_block(self, direction):

        if direction == "x":
            # False ist, ob wir der Sprite löschen wollen
            hits = pygame.sprite.spritecollide(self, self.game.blocks,
                                               False)  # prüft, ob die rect zweier Sprites miteinander kollidieren
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
    
    def get_tile_position(self):
        return (self.rect.x + 50) // 100, (self.rect.y + 50) // 100
