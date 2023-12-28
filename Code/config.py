import os
import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800
ENTITY_SIZE = 80
TILE_SIZE = 100
FPS = 60
ANIMATION_FPS = 10
ANIMATION_TPF = FPS // ANIMATION_FPS # TPF = ticks per frame
MOVEMENT_SUBSTEP_COUNT = 1

UI_LAYER = 10
WEAPON_LAYER = 9
PLAYER_LAYER = 8
DARKNESS_LAYER = 7
HIDDEN_WALL_LAYER = 6
HIDDEN_FLOOR_LAYER = 5
ENEMY_LAYER = 4
WALL_LAYER = 3
PORTAL_LAYER = 2
POWERUP_LAYER = 1
FLOOR_LAYER = 0

START_PLAYER_HEALTH = 1000
START_PLAYER_SPEED = 5
START_PLAYER_LIGHT_RANGE = 5
LIGHT_INTENSITIES_COUNT = 5

START_LABYRINTH_WIDTH = 4
START_LABYRINTH_LENGTH = 4
LABYRINTH_WIDTH_INCREASE = 1
LABYRINTH_LENGTH_INCREASE = 1

ENEMY_SPEED = 1

HEALTH_BAR_POS = (200, 200)
HEALTH_BAR_WIDTH = 25
HEALTH_BAR_HEIGHT = 20

LIGHT_ADAPTION_TIME = 0.5

SOUND_FOLDER = "sounds"
MUSIC_FOLDER = os.path.join(SOUND_FOLDER, "music")
LEVEL_SOUNDTRACK = os.path.join(MUSIC_FOLDER, "Pharaoh's Tomb Soundtrack final.mp3")

IMAGE_FOLDER = "img"
PORTAL_SPRITE_PATH = os.path.join(IMAGE_FOLDER, "portal.png")
FLOOR_SPRITE_PATH = os.path.join(IMAGE_FOLDER, "floorbig.png")
WALL_SPRITE_PATH = os.path.join(IMAGE_FOLDER, "sandbrick-pixilart.png")

PLAYER_IMAGE_FLORDER = os.path.join(IMAGE_FOLDER, "player")

PLAYER_ANIMATION_RIGHT = (pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-right (0).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-right (1).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-right (2).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-right (3).png")))
PLAYER_ANIMATION_UP = (pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-back (0).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-back (1).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-back (2).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-back (3).png")))
PLAYER_ANIMATION_LEFT = (pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-left (0).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-left (1).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-left (2).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-left (3).png")))
PLAYER_ANIMATION_DOWN = (pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-front (0).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-front (1).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-front (2).png")),
                          pygame.image.load(os.path.join(PLAYER_IMAGE_FLORDER, "treasure-hunter-pixilart-front (3).png")))

MUSIC_VOLUME = 1


def NEW_HEALTH():
    global START_PLAYER_HEALTH
    START_PLAYER_HEALTH -= 1
    print(START_PLAYER_HEALTH)
    return START_PLAYER_HEALTH


def CURRENT_HEALTH():
    return CURRENT_HEALTH()


def CURRENT_SPEED():
    return START_PLAYER_SPEED


def NEW_SPEED():
    global START_PLAYER_SPEED
    START_PLAYER_SPEED += 2/5 * ( 10 - START_PLAYER_SPEED)

    return START_PLAYER_SPEED


RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 0, 255)
ENEMY_COLOR = (88, 55, 111)
SAND_COLOR = (194, 178, 128)
BOOST_COLOR = (222, 111, 112)

level_1 = ["XXXXXXXXXXXXXXXXXXXX",
           "X.....X...X...X..X.X",
           "X....X..X...X......X",
           "X...........X.X....X",
           "X.X......X...XX....X",
           "X.....X.XX.........X",
           "XX.X........XX.....X",
           "X......X.....X.X...X",
           "X.....X..XX.X.X.X..X",
           "X..X..X...XX.XX.X..X",
           ".P........X....X...X",
           "X....X.X....X....XXX",
           "X......X..X.....X..X",
           "X...X.XXX..X.X.....X",
           "X...............X..X",
           "X..X..XX.X...X.....X",
           "X......X..X.X.X....X",
           "X...X...X..X..X.X..X",
           "X....XXX.X.X.X.....X",
           "XXXXXXXXXXXXXXXXXXXX"
           ]
level_2 = [['u', 'X', 'X', 'X', 'X', 'X', 'u', 'u', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'u', 'u', 'u'],
           ['X', '.', '.', 'P', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'u'],
           ['X', '.', 'X', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', 'X'],
           ['X', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', 'X'],
           ['X', '.', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', '.', 'X', 'X', 'u'],
           ['X', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'u', 'u'],
           ['u', 'X', 'X', '.', '.', 'X', '.', 'X', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', 'X', 'u'],
           ['u', 'u', 'X', '.', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', 'u'],
           ['u', 'X', '.', '.', 'X', '.', '.', '.', 'X', 'u', 'X', '.', '.', '.', 'X', '.', '.', '.', 'X', 'u'],
           ['X', '.', '.', 'X', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', '.', 'X', '.', '.', 'X', '.', 'X', 'u'],
           ['X', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', 'X', 'u'],
           ['u', 'X', 'X', '.', 'X', 'X', '.', 'X', 'X', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', 'u', 'u'],
           ['X', '.', 'X', '.', 'X', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', 'X', 'X', 'u', 'u'],
           ['X', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', 'u'],
           ['u', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', 'X', 'X', 'X', '.', '.', 'X', '.', 'X', 'u'],
           ['u', 'u', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'X', '.', '.', 'X'],
           ['u', 'X', '.', '.', '.', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', 'X', '.', '.', 'X', '.', 'X'],
           ['X', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
           ['u', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'u'],
           ['u', 'u', 'X', 'X', 'u', 'u', 'u', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'u', 'u', 'u']]
level_3 = [['u', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u'],
           ['X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'],
           ['u', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', '.', 'X', 'u'],
           ['X', '.', '.', 'X', '.', '.', 'X', 'X', '.', 'X', 'X', '.', '.', 'X', '.', 'X', '.', '.', '.', 'X'],
           ['X', '.', 'X', 'X', '.', 'X', 'X', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X', '.', 'X', '.', 'X'],
           ['X', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', 'X', 'X', '.', 'X', '.', '.', '.', 'X'],
           ['u', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', 'X', 'X', 'X', 'X', 'u'],
           ['X', '.', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'],
           ['X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', 'X'],
           ['X', '.', '.', 'X', '.', 'X', '.', '.', 'X', 'X', '.', 'X', '.', '.', '.', 'X', 'X', 'X', '.', 'X'],
           ['X', 'P', '.', 'X', '.', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', 'X'],
           ['u', 'X', 'X', 'u', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.', 'X', 'X', '.', '.', 'X', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'X', '.', 'X', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'X', '.', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', 'X', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.', 'X', '.', '.', '.', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'u', 'X', '.', '.', 'X', 'X', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', '.', '.', '.', 'X', '.', 'X', '.', '.', '.', 'X', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', 'X', '.', 'X', '.', '.', '.', 'X', 'X', 'X', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'],
           ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u']]
