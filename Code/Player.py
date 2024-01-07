import pygame
import math
from weapon import *
from HealthBar import * 
from config import *
from animation_handler import Animation

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # important when we have more objects, so we know which is on top of which
        self.groups = self.game.all_sprites, self.game.player  # add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILE_SIZE * PLAYER_ANIMATION_DOWN[0].get_width() / PLAYER_ANIMATION_DOWN[0].get_height()
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        # self.image.blit(pygame.image.load("img/player/player_look_down.png"),(0,0))

        self.animation_right = Animation(PLAYER_ANIMATION_RIGHT, self.game)
        self.animation_up = Animation(PLAYER_ANIMATION_UP, self.game)
        self.animation_left = Animation(PLAYER_ANIMATION_LEFT, self.game)
        self.animation_down = Animation(PLAYER_ANIMATION_DOWN, self.game)
        
        self.rect = self.image.get_rect()  # hit box is the same size as the image

        #set position
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

        self.light_range = START_PLAYER_LIGHT_RANGE
        self.light_intensities_count = LIGHT_INTENSITIES_COUNT
        self.weapon = Weapon(game, self)

        self.is_overlapping_with_portal = False
        self.facing = 'down'
        self.health_bar = HealthBar(game,self)
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.movement()
        self.weapon.update()
        self.collide()
        self.update_sprite()
        self.health_bar.draw()
    def reload(self):
        self.facing = "down"
        
        self.x_change = 0
        self.y_change = 0
    
    def update_sprite(self):
        if self.facing == 'right':
            sprite = self.animation_right.get_current_sprite()
        elif self.facing == 'up':
            sprite = self.animation_up.get_current_sprite()
        elif self.facing == 'left':
            sprite = self.animation_left.get_current_sprite()
        elif self.facing == 'down':
            sprite = self.animation_down.get_current_sprite()
        
        self.image = pygame.Surface([sprite.get_width(), sprite.get_height()])
        self.image.set_colorkey(PINK)
        self.image.blit(sprite, (0, 0))

    def collide(self):
        if not self.game.in_debug_mode:
            self.collide_enemy()
        self.collide_tile(MOVEMENT_SUBSTEP_COUNT)
        self.collide_powerup()
        self.collide_portal()

    def collide_tile(self, sub_step_count):
        if self.game.in_debug_mode:
            self.rect.x += self.x_change
            self.rect.y += self.y_change

            self.x_change = 0
            self.y_change = 0
            return

        # do small steps multiple times to get the same outcome as doing one normal step but with more precision
        for _ in range(sub_step_count):
            self.rect.x += self.x_change / sub_step_count
            self.collide_block('x')
            self.rect.y += self.y_change / sub_step_count
            self.collide_block('y')

        self.x_change = 0
        self.y_change = 0

    def collide_portal(self):
        self.is_overlapping_with_portal = pygame.sprite.spritecollide(self, self.game.portal, False)

    def movement(self):
        key = pygame.key.get_pressed()  # checks which keys are being pressed
        if not key[pygame.K_g]:  # freeze
            if key[pygame.K_UP]or key[pygame.K_w]:
                self.y_change -= CURRENT_SPEED()
                self.facing = 'up'

            if key[pygame.K_DOWN]or key[pygame.K_s]:
                self.y_change += CURRENT_SPEED()
                self.facing = 'down'

            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.x_change -= CURRENT_SPEED()
                self.facing = 'left'

            if key[pygame.K_RIGHT]or key[pygame.K_d]:
                self.x_change += CURRENT_SPEED()
                self.facing = 'right'

    def collide_powerup(self):  # NEUE FUNKTION
        collide = pygame.sprite.spritecollide(self, self.game.powerup, True)
        if collide:
            NEW_SPEED()

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            #print(NEW_HEALTH())
            self.health_bar.health()
            if NEW_HEALTH() == 0:
                self.kill()
                self.game.playing = False

    def collide_block(self, direction):

        if direction == "x":
            # False ist, ob wir der Sprite löschen wollen
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)  # prüft, ob die rect zweier Sprites miteinander kollidieren
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
                    # for sprite in self.game.all_sprites:
                    #    sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right  # wir setzen self.rect.x zur rechten Ecke steht genau neben dran
                    # for sprite in self.game.all_sprites:
                    #    sprite.rect.x -= PLAYER_SPEED
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)  # prüft obt die rect zweier Sprites miteinander kollidieren
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
                    # for sprite in self.game.all_sprites:
                    # #   sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
                    # for sprite in self.game.all_sprites:
                    #    sprite.rect.y -= PLAYER_SPEED
    
    def get_tile_position(self):
        return (self.rect.x + TILE_SIZE // 2) // TILE_SIZE, (self.rect.y + TILE_SIZE // 2) // TILE_SIZE
