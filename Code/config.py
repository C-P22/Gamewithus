WIN_WIDTH = 800
WIN_HEIGHT = 800
TILESIZE = 30
BOXSIZE = 40
FPS = 60 # framrate


PLAYER_LAYER = 2
BLOCK_LAYER = 1

PLAYER_SPEED = 3


def CURRENT_SPEED():
    return PLAYER_SPEED


def NEW_SPEED():
    global PLAYER_SPEED
    PLAYER_SPEED += 2
    return PLAYER_SPEED


RED = (255,0,0)
BLACK = (0,0,0)
SAND =(194,178,128)
level_1 =["XXXXXXXXXXXXXXXXXXXX",
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
level_2 = [['u', 'X', 'X', 'X', 'X', 'X', 'u', 'u', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'u', 'u', 'u'], ['X', '.', '.', 'P', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'u'], ['X', '.', 'X', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', 'X'], ['X', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', 'X'], ['X', '.', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', '.', 'X', 'X', 'u'], ['X', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', 'X', 'X', 'X', 'X', 'u', 'u'], ['u', 'X', 'X', '.', '.', 'X', '.', 'X', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', 'X', 'u'], ['u', 'u', 'X', '.', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', 'u'], ['u', 'X', '.', '.', 'X', '.', '.', '.', 'X', 'u', 'X', '.', '.', '.', 'X', '.', '.', '.', 'X', 'u'], ['X', '.', '.', 'X', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', '.', 'X', '.', '.', 'X', '.', 'X', 'u'], ['X', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', 'X', 'u'], ['u', 'X', 'X', '.', 'X', 'X', '.', 'X', 'X', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', 'u', 'u'], ['X', '.', 'X', '.', 'X', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', 'X', 'X', 'u', 'u'], ['X', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', 'u'], ['u', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', 'X', 'X', 'X', '.', '.', 'X', '.', 'X', 'u'], ['u', 'u', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'X', '.', '.', 'X'], ['u', 'X', '.', '.', '.', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', 'X', '.', '.', 'X', '.', 'X'], ['X', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', 'X'], ['u', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'u'], ['u', 'u', 'X', 'X', 'u', 'u', 'u', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'u', 'u', 'u']]
level_3 = [['u', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u'], ['X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'], ['u', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', '.', 'X', 'u'], ['X', '.', '.', 'X', '.', '.', 'X', 'X', '.', 'X', 'X', '.', '.', 'X', '.', 'X', '.', '.', '.', 'X'], ['X', '.', 'X', 'X', '.', 'X', 'X', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', 'X', 'X', '.', 'X', '.', '.', '.', 'X'], ['u', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', 'X', 'X', 'X', 'X', 'u'], ['X', '.', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'], ['X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', 'X'], ['X', '.', '.', 'X', '.', 'X', '.', '.', 'X', 'X', '.', 'X', '.', '.', '.', 'X', 'X', 'X', '.', 'X'], ['X', 'P', '.', 'X', '.', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', 'X'], ['u', 'X', 'X', 'u', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.', 'X', 'X', '.', '.', 'X', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'X', '.', 'X', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'X', '.', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', 'X', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.', 'X', '.', '.', '.', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'u', 'X', '.', '.', 'X', 'X', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', '.', '.', '.', 'X', '.', 'X', '.', '.', '.', 'X', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', 'X', '.', 'X', '.', '.', '.', 'X', 'X', 'X', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'], ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'X', 'X', 'X', 'X', 'u', 'X', 'X', 'X', 'X', 'u']]

