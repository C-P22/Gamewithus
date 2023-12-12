import pygame
import sys
import os
from Game import *

os.chdir(os.path.dirname(__file__))

game = Game()
game.load_next_level()
while game.running:
    game.main()
    game.game_over()

pygame.quit()
sys.exit()
