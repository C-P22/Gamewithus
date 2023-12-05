import pygame
import sys
from Game import *

game = Game()
game.load_next_level()
while game.running:
    game.main()
    game.game_over()

pygame.quit()
sys.exit()
