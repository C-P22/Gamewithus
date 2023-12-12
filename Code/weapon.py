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
        self.activated = False
        self.height = 10
        self.weapon_range = 80
        self.ready_to_deal_damage = True
        self.damage = 1 
        self.groups = self.game.all_sprites, self.game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.load(False)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.rect.x = self.player.rect.x+50 
        self.rect.y = self.player.rect.y+50
        self.activated = False
        
        self.attack()


    def attack(self):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

            mouse_x -= 400
            mouse_y -= 400
            
            
            direction_x = mouse_x 
            direction_y = mouse_y 
            distance = math.sqrt(direction_x**2 + direction_y**2)
            

            # Normalize the direction vector
            if distance != 0:
                direction_x /= distance
                direction_y /= distance
            #time.sleep(3)
            self.rect.x += int(direction_x * self.weapon_range)
            self.rect.y += int(direction_y * self.weapon_range)
            self.activated = True
            self.load(True)
            self.collide_block()
        else:
            self.load(False)
    def load(self,Direction):
        if Direction:
            self.image = pygame.Surface([self.height,self.width])
            self.image.fill((255,255,0))
            
        else:
            image_to_load = pygame.image.load("img/weapon/weopon.png")
            self.image = pygame.Surface([self.width,self.height])
            self.image = self.image.convert_alpha()
            #self.image.set_colorkey(BLACK)
            self.image.blit(image_to_load,(0,0))
            self.ready_to_deal_damage = True
    def collide_block(self):
        if  self.ready_to_deal_damage:
            #ic(self.ready_to_deal_damage)
            collides = pygame.sprite.spritecollide(self, self.game.destroyable, False)
            for collide in collides:
                collide.health -= self.damage
                ic(collide.health)
            self.ready_to_deal_damage = False