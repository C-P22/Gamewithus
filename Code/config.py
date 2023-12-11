import os

WIN_WIDTH = 800
WIN_HEIGHT = 800
ENTITY_SIZE = 80
TILE_SIZE = 100
FPS = 60
MOVEMENT_SUBSTEP_COUNT = 5

UI_LAYER = 6
WEAPON_LAYER = 5
PLAYER_LAYER = 4
DARKNESS_LAYER = 3
ENEMY_LAYER = 2
BLOCK_LAYER = 1

PLAYER_HEALTH = 60
PLAYER_SPEED = 5
PLAYER_LIGHT_RANGE = 5

ENEMY_SPEED = 5

HEALTH_BAR_X = 200
HEALTH_BAR_Y = 200
HEALTH_BAR_WIDTH = 25
HEALTH_BAR_HEIGHT = 20

LIGHT_ADAPTION_TIME = 0.5

SOUND_FOLDER = "sounds"
MUSIC_FOLDER = os.path.join(SOUND_FOLDER, "music")
LEVEL_SOUNDTRACK = os.path.join(MUSIC_FOLDER, "Pharaoh's Tomb Soundtrack final.mp3")

IMAGE_FOLDER = "img"
PORTAL_SPRITE_PATH = os.path.join(IMAGE_FOLDER, "portal.png")
FLOOR_SPRITE_PATH = os.path.join(IMAGE_FOLDER, "floorbig.png")

MUSIC_VOLUME = 1

def NEW_HEALTH():
    global PLAYER_HEALTH
    PLAYER_HEALTH -= 1
    print(PLAYER_HEALTH)
    return PLAYER_HEALTH


def CURRENT_HEALTH():
    return CURRENT_HEALTH()


def CURRENT_SPEED():
    return PLAYER_SPEED


def NEW_SPEED():
    global PLAYER_SPEED
    PLAYER_SPEED += 2
    return PLAYER_SPEED


RED = (255, 0, 0)
BLACK = (0, 0, 0)
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
