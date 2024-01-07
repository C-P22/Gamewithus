import pygame
import math
from weapon import *
from config import *
from animation_handler import Animation
from sound_handler import *

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # important when we have more objects, so we know which is on top of which
        self.groups = self.game.all_sprites, self.game.player  # add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILE_SIZE * PLAYER_ANIMATION_DOWN[0].get_width() / PLAYER_ANIMATION_DOWN[0].get_height()
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])

        self.animation_right = Animation(PLAYER_ANIMATION_RIGHT, self.game)
        self.animation_up = Animation(PLAYER_ANIMATION_UP, self.game)
        self.animation_left = Animation(PLAYER_ANIMATION_LEFT, self.game)
        self.animation_down = Animation(PLAYER_ANIMATION_DOWN, self.game)
        
        self.rect = self.image.get_rect()  # hit box is the same size as the image

        #set position
        self.x = x * TILE_SIZE # use of floating point stuff
        self.y = y * TILE_SIZE
        self.rect.x = x * TILE_SIZE # actual position used in the end
        self.rect.y = y * TILE_SIZE

        self.weapon = Weapon(game, self)

        self.is_overlapping_with_portal = False
        self.facing = 'down'

        self.x_change = 0
        self.y_change = 0

        self.prev_moving = False
        self.moving = False

        self.speed = START_PLAYER_SPEED
        self.health = START_PLAYER_HEALTH
        self.light_range = START_PLAYER_LIGHT_RANGE

    def update(self):
        self.movement()
        self.weapon.update()
        self.collide()
        self.update_sprite()
        self.update_sound()
    
    def update_sound(self):
        if (self.moving and not self.prev_moving):
            play_footsteps_sound()
        elif (not self.moving and self.prev_moving):
            stop_footsteps_sound()

    def update_sprite(self):
        game_tick = self.game.tick
        if not self.moving:
            self.game.tick = 0

        if self.facing == 'right':
            sprite = self.animation_right.get_current_sprite()
        elif self.facing == 'up':
            sprite = self.animation_up.get_current_sprite()
        elif self.facing == 'left':
            sprite = self.animation_left.get_current_sprite()
        elif self.facing == 'down':
            sprite = self.animation_down.get_current_sprite()
        
        self.game.tick = game_tick
        
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
            self.x += self.x_change / sub_step_count
            self.rect.x = int(self.x)
            self.collide_block('x')
            self.y += self.y_change / sub_step_count
            self.rect.y = int(self.y)
            self.collide_block('y')

        self.x_change = 0
        self.y_change = 0

    def collide_portal(self):
        self.is_overlapping_with_portal = pygame.sprite.spritecollide(self, self.game.portal, False)

    def movement(self):
        key = pygame.key.get_pressed()  # checks which keys are being pressed
        if not key[pygame.K_g]:  # freeze
            if key[pygame.K_UP]or key[pygame.K_w]:
                self.y_change -= self.speed
                self.facing = 'up'

            if key[pygame.K_DOWN]or key[pygame.K_s]:
                self.y_change += self.speed
                self.facing = 'down'

            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.x_change -= self.speed
                self.facing = 'left'

            if key[pygame.K_RIGHT]or key[pygame.K_d]:
                self.x_change += self.speed
                self.facing = 'right'
        
        self.prev_moving = self.moving
        self.moving = self.x_change != 0 or self.y_change != 0

    def collide_powerup(self):
        if pygame.sprite.spritecollide(self, self.game.powerup, True):
            self.speed += PLAYER_SPEED_INCREASE

    def collide_enemy(self):
        if pygame.sprite.spritecollide(self, self.game.enemies, False):
            self.health -= 1
            if self.health <= 0:
                self.kill()
                self.game.playing = False

    def collide_block(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)  # prüft, ob die rect zweier Sprites miteinander kollidieren
        if not hits:
            return
        
        if direction == "x":
            # False ist, ob wir der Sprite löschen wollen
            if self.x_change > 0:
                self.x = hits[0].rect.left - self.rect.width  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
            elif self.x_change < 0:
                self.x = hits[0].rect.right  # wir setzen self.rect.x zur rechten Ecke steht genau neben dran
        elif direction == "y":
            if self.y_change > 0:
                self.y = hits[0].rect.top - self.rect.height  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player
            elif self.y_change < 0:
                self.y = hits[0].rect.bottom  # wir setzen self.rect.x zu Linke Ecke und dann rechnen wir minus width von unserem player

        self.rect.x = self.x
        self.rect.y = self.y
    
    def collide_block_new(self):
        relative_x = self.rect.x % TILE_SIZE
        relative_y = self.rect.y % TILE_SIZE
        
        if self.is_between_four_tiles():
            pass
        else:
            pass

    def get_tile_position(self):
        return (self.rect.x + TILE_SIZE // 2) // TILE_SIZE, (self.rect.y + TILE_SIZE // 2) // TILE_SIZE
    
    def is_between_two_tiles_horizontal(self):
        return not (((self.rect.x + ENTITY_SIZE // 2) % TILE_SIZE) >= (ENTITY_SIZE / 2) and ((self.rect.x + ENTITY_SIZE // 2) % TILE_SIZE) <= (TILE_SIZE - ENTITY_SIZE / 2))

    def is_between_two_tiles_vertical(self):
        return not (((self.rect.y + ENTITY_SIZE // 2) % TILE_SIZE) >= (ENTITY_SIZE / 2) and ((self.rect.y + ENTITY_SIZE // 2) % TILE_SIZE) <= (TILE_SIZE - ENTITY_SIZE / 2))

    def is_between_four_tiles(self):
        return self.is_between_two_tiles_horizontal() and self.is_between_two_tiles_vertical()
