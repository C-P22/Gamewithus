import pygame
import os
from config import *

def init():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(MUSIC_VOLUME)

def play_level_soundtrack():
    # pygame.mixer.music.stop()
    # pygame.mixer.music.load(LEVEL_SOUNDTRACK)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(LEVEL_SOUNDTRACK), -1)
    pygame.mixer.Channel(0).set_volume(MUSIC_VOLUME)

def play_footsteps_sound():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(FOOTSTEPS_SOUNDTRACK), -1)

def stop_footsteps_sound():
    pygame.mixer.Channel(1).stop()