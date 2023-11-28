import pygame
import math
from config import *
import random


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # important when we have more objekts, so we know which is on top of which
        self.groups = self.game.all_sprites, self.game.player  # add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = "down"  # movements of the character
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()  # hit box = image the same
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.collide_enemy()    # NEU
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

        self.x_change = 0
        self.y_change = 0
        self.collide_powerup()
        if self.collide_portal():
            return True
        return False

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

    def collide_powerup(self):  # NEUE FUNKTION
        collide = pygame.sprite.spritecollide(self, self.game.powerup, True)
        if collide:
            NEW_SPEED()

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
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


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE

        self.height = BOXSIZE

    def get_form_img(self, Path):
        image_to_load = pygame.image.load(Path)
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0, 0))

        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def get_form_colour(self, Color):
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Powerup(Block):
    def __init__(self, game, x, y):
        Block.__init__(self, game, x, y)

        self.groups = self.game.all_sprites, self.game.powerup
        pygame.sprite.Sprite.__init__(self, self.groups)
        Block.get_form_colour(self, BOOST)


class Wall(Block):
    def __init__(self, game, x, y, transparent):

        Block.__init__(self, game, x, y)
        if transparent:
            self.groups = self.game.all_sprites, self.game.blocks
        else:
            self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        Block.get_form_colour(self, SAND)


class Floor(Block):
    def __init__(self, game, x, y):
        Block.__init__(self, game, x, y)

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        Block.get_form_img(self, "img/floorbig.png")


class Portal(Block):
    def __init__(self, game, x, y):
        Block.__init__(self, game, x, y)
        self.groups = self.game.all_sprites, self.game.portal
        pygame.sprite.Sprite.__init__(self, self.groups)
        Block.get_form_img(self, "img/portal.png")


class Enemy(pygame.sprite.Sprite):  # NEUE CLASS ERSTELLT
    def __init__(self, game, x, y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(30, 50)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(ENEMY)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

