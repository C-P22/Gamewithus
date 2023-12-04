import pygame
import math
from config import *
import random


class Character:
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