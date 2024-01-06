from config import *

class Animation:
    def __init__(self, sprites, game):
        self.sprites = sprites
        self.game = game
        pass

    def get_current_sprite(self):
        relative_tick = self.game.tick % (ANIMATION_TPF * len(self.sprites))
        return self.sprites[relative_tick // ANIMATION_TPF]