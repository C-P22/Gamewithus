import pygame
import os
from config import *

level_music_file = os.path.join(MUSIC_FOLDER, "Pharaoh's Tomb Soundtrack final.mp3")

def init():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(MUSIC_VOLUME)

def play_level_soundtrack():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(level_music_file)
    pygame.mixer.music.play(-1)