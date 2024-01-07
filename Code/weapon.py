import pygame
import random
import math 
from config import *
import time 
from icecream import ic 


class Weapon(pygame.sprite.Sprite):
    def __init__(self,game,Player):
        self.player = Player
        self.game = game 
        self._layer = WEAPON_LAYER
        self.x = Player.rect.x
        self.y = Player.rect.y
        self.width = 40
        self.height = 10
        self.weapon_range = START_WEAPON_RANGE
        self.damage = 4 / FPS
        self.groups = self.game.all_sprites, self.game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.load()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.rect.x = self.player.rect.x - 30
        self.rect.y = self.player.rect.y + 30
        
        self.attack()


    def attack(self):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

            mouse_x -= WIN_WIDTH / 2 + PLAYER_ANIMATION_DOWN[0].get_width() / 2
            mouse_y -= WIN_HEIGHT / 2 + PLAYER_ANIMATION_DOWN[0].get_height() / 2
            
            
            direction_x = mouse_x 
            direction_y = mouse_y 
            distance = math.sqrt(direction_x**2 + direction_y**2)
            

            # Normalize the direction vector
            if distance != 0:
                direction_x /= distance
                direction_y /= distance
            #time.sleep(3)
            self.rect.x = self.player.rect.centerx - self.rect.width / 2 + int(direction_x * self.weapon_range) * 1
            self.rect.y = self.player.rect.centery - self.rect.height / 2 + int(direction_y * self.weapon_range) * 1
            self.load()
            self.collide_block()
        else:
            self.load()

    def load(self):
        image_to_load = pygame.image.load(WEAPON_SPRITE_PATH)
        self.image = pygame.Surface([image_to_load.get_width(), image_to_load.get_height()])
        self.image.set_colorkey(PINK)
        self.image.blit(image_to_load,(0,0))

    def collide_block(self):
        collides = pygame.sprite.spritecollide(self, self.game.destroyable, False)
        for collide in collides:
            collide.health -= self.damage
            ic(collide.health)