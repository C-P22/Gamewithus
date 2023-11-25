from sprite import *
from config import *


class POWERUP(pygame.sprite.Sprite):
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
        self.image.fill(BOOST)

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def boost(self, PLAYER_SPEED):
        collide = pygame.sprite.spritecollide(self,self.game.blocks,False)
        print("collide")
        if collide:
            PLAYER_SPEED += 20
            print("boost")
        else:
            print("no collision")
