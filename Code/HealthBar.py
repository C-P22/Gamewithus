import pygame
from config import *


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, game, Player):
        self.x = Player.rect.x
        self.y = Player.rect.y
        self.game = game
        self.width = HEALTH_BAR_WIDTH
        self.height = HEALTH_BAR_HEIGHT
        self._layer = PLAYER_LAYER +10
        self.groups = self.game.all_sprites        
        self.player = Player
        self.hp = CURRENT_HEALTH()
        self.max_hp = START_PLAYER_HEALTH
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
        
    def draw(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
        ratio = self.hp/self.max_hp
        self.image = pygame.Surface([self.width*ratio, self.height])
        self.image.fill((0,255,0))
        
    def health(self):

        self.hp -= 1



        #pygame.draw.rect( "red", (self.x, self.y, self.width, self.height))
        #pygame.draw.rect( "green", (self.x, self.y, self.width * ratio, self.height))

