import pygame


class SoundHandler():
    root_folder = "sounds"
    music_folder = root_folder + "\\" + "music"
    global level_music_file
    level_music_file = music_folder + "\\" + "Pharaoh's Tomb Soundtrack final.mp3"

    def __init__(self):
        pass

    def play_level_soundtrack():
        pygame.mixer.music.stop()
        #pygame.mixer.music.load(level_music_file)
        #pygame.mixer.music.play(-1)
