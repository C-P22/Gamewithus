import pygame
import math
from config import *
import random
from icecream import ic 


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER # important when we have more objekts so we know which is on top of which
        self.groups = self.game.all_sprites,self.game.player# add it to all sprite group# add it to all sprite group
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = "down"  # movements of the character
        image_to_load = pygame.image.load("img/player/player_look_down.png")
        self.image = pygame.Surface([self.width,self.height])
        self.image = self.image.convert_alpha()
        #self.image.set_colorkey(BLACK)
        self.image.blit(image_to_load,(0,0))


        self.rect = self.image.get_rect()  # hitbox = image the same
        self.rect.x = self.x
        self.rect.y = self.y
        self.weapon = Wepon(game,self)

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

        self.x_change = 0 
        self.y_change = 0
        self.collide_powerup()
        self.weapon.update()
        if self.collide_portal():
            return True
        return False 
        
    def collide_portal(self):
        hits = pygame.sprite.spritecollide(self,self.game.portal,False)
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

    def collide_powerup(self):
        collide = pygame.sprite.spritecollide(self, self.game.powerup, True)
        if collide:
            NEW_SPEED()

    def collide_block(self, direction):

        if direction == "x":
            # False ist, ob wir der Sprite löschen wollen
            hits = pygame.sprite.spritecollide(self, self.game.waende,
                                               False)  # prüft ob die rect zweier Sprites miteinander kollidieren
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
            hits = pygame.sprite.spritecollide(self, self.game.waende,
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
    def __init__(self,game,x,y):
        self.game = game 
        self._layer = BLOCK_LAYER
        self.x = x * BOXSIZE
        self.y = y * BOXSIZE
        self.width = BOXSIZE
        self.health = 3
        self.height = BOXSIZE

    def get_form_img(self,Path,Alpha):
        image_to_load = pygame.image.load(Path)
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))
        if Alpha:
            self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect_change_x = 0
        self.rect_change_y = 0
        self.rect.x = self.x
        self.rect.y = self.y
    def get_form_colour(self,Color):
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(Color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        # Check if the object has no health left
        if self.health <= 0:
            self.kill()

class Powerup(Block):
    def __init__(self, game, x, y):
        Block.__init__(self,game,x,y)
       
        self.groups = self.game.all_sprites, self.game.powerup,self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        Block.get_form_colour(self,BOOST)
        

    

class Wall(Block):
    def __init__(self,game,x,y,transparent):

        Block.__init__(self,game,x,y)
        if transparent:
            self.groups = self.game.all_sprites,self.game.blocks, self.game.waende
        else:
            self.groups = self.game.all_sprites,self.game.blocks,self.game.destroyable,self.game.waende
        pygame.sprite.Sprite.__init__(self,self.groups)
        Block.get_form_colour(self,SAND)
class Floor(Block):
    def __init__(self,game,x,y):
        Block.__init__(self,game,x,y)
        
        self.groups = self.game.all_sprites,self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)
        Block.get_form_img(self,"img/floorbig.png",False)
class Portal(Block):
    def __init__(self,game,x,y):
        Block.__init__(self,game,x,y)
        self.groups = self.game.all_sprites,self.game.portal,self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)
        Block.get_form_img(self,"img/portal.png",True)

class Wepon(pygame.sprite.Sprite):
    def __init__(self,game,Player):
        self.player = Player
        self.game = game 
        self._layer = WEAPON_LAYER
        self.x = Player.x
        self.y = Player.y
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
        self.rect.x = 450
        self.rect.y = 450
        self.activated = False
        
        self.attack()


    def attack(self):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction_x = mouse_x - self.rect.x
            direction_y = mouse_y - self.rect.y
            distance = math.sqrt(direction_x**2 + direction_y**2)

            # Normalize the direction vector
            if distance != 0:
                direction_x /= distance
                direction_y /= distance
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
            self.image = pygame.Surface([self.width,self.height])
            self.image.fill((255,255,0))
            self.ready_to_deal_damage = True
    def collide_block(self):
        if  self.ready_to_deal_damage:
            ic(self.ready_to_deal_damage)
            collides = pygame.sprite.spritecollide(self, self.game.destroyable, False)
            for collide in collides:
                collide.health -= self.damage
                ic(collide.health)
            self.ready_to_deal_damage = False