import pygame
import random

from config import *
import sound_handler
import light_system

from labrinth_generator import Maze
from Enemy import Enemy
from Player import Player
from Blocks.darkness import *
from Blocks.floor import *
from Blocks.portal import *
from Blocks.powerup import *
from Blocks.wall import *


class Game:
    def __init__(self):
        pygame.init()
        sound_handler.init()
        sound_handler.play_level_soundtrack()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()  # frame rate
        self.running = True
        self.x = 0
        self.labrinth_length = 10
        self.labrinth_width = 10

    def update(self):
        self.player.update()
        if self.player.is_overlapping_with_portal:
            self.load_next_level()
        self.enemies.update()
        self.update_light()

    def update_light(self):
        # # only calculate light when it changes
        # if (self.prev_player_tile_position == self.player.get_tile_position()):
        #     self.prev_player_tile_position = self.player.get_tile_position()
        #     return
        # calculate light
        light_value_matrix = light_system.get_light_matrix_new(self.wall_matrix, self.player.get_tile_position(),
                                                               self.player.light_range)
        # set light values
        for i in range(len(light_value_matrix)):
            for j in range(len(light_value_matrix[i])):
                new_alpha = 255 * (1 - light_value_matrix[i][j] / self.player.light_range)
                old_alpha = self.darkness_matrix[i][j].get_alpha()
                self.darkness_matrix[i][j].set_alpha(old_alpha + (new_alpha - old_alpha) / (LIGHT_ADAPTION_TIME * FPS))
        # store the tile position of player so I know if the light changed in the next iteration
        self.prev_player_tile_position = self.player.get_tile_position()

    def load_next_level(self):
        self.prev_player_tile_position = -1, -1
        self.labrinth_length += 3
        self.labrinth_width += 3
        self.labrinth_length = 20
        self.labrinth_width = 20
        self.initialize_game_objects()
        self.create_level()

    def initialize_game_objects(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # hier können wir unsere Sprites reintun
        self.blocks = pygame.sprite.LayeredUpdates()
        self.darkness = pygame.sprite.LayeredUpdates()
        self.portal = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.powerup = pygame.sprite.LayeredUpdates()

    def create_level(self):
        self.wall_matrix = [[0 for _ in range(self.labrinth_length)] for _ in range(self.labrinth_width)]
        self.darkness_matrix = [[0 for _ in range(self.labrinth_length)] for _ in range(self.labrinth_width)]
        self.enemie_movement = [[0 for _ in range(self.labrinth_length)] for _ in range(self.labrinth_width)]
        level = Maze(self.labrinth_length, self.labrinth_width, self.labrinth_length // 2, self.labrinth_width // 2)
        level = level_1
        for i, row in enumerate(level):
            for j, colum in enumerate(row):
                if colum == "X":
                    self.wall_matrix[j][i] = 1
                    self.enemie_movement[j][i] = 1
                    Wall(self, j, i, True)
                if colum == "P":
                    self.player = Player(self, j, i)
                    self.enemie_movement[j][i] = 1
                    Floor(self, j, i)
                if colum == ".":
                    x = random.randint(0, 50)
                    if x < 10:
                        self.wall_matrix[j][i] = 1
                        self.enemie_movement[j][i] = 1
                        Wall(self, j, i, False)
                    elif x == 10:
                        Floor(self, j, i)
                        self.enemie_movement[j][i] = 1
                        Powerup(self, j, i)
                    elif x == 20:
                        Floor(self, j, i)
                        self.enemie_movement[j][i] = 1
                        Enemy(self, j, i)
                    else:
                        Floor(self, j, i)
                if colum == 'L':
                    Floor(self, j, i)
                    self.enemie_movement[j][i] = 1
                    Enemy(self, j, i)
                if colum == "E":
                    Floor(self, j, i)
                    Portal(self, j, i)
                self.darkness_matrix[j][i] = Darkness(self, j, i)

    def draw_screen(self):

        self.screen.fill(BLACK)
        ''''''''''
        self.all_sprites.draw(self.screen)
        '''

        camera_offset = [0, 0]
        # Update camera offset to center on the player
        camera_offset[0] = (WIN_WIDTH // 2) - self.player.rect.x
        camera_offset[1] = (WIN_HEIGHT // 2) - self.player.rect.y

        # Draw sprites at adjusted positions based on camera offset
        for sprite in self.all_sprites:
            sprite.rect.x += camera_offset[0]
            sprite.rect.y += camera_offset[1]

        self.all_sprites.draw(self.screen)

        # Reset sprite positions after drawing
        for sprite in self.all_sprites:
            sprite.rect.x -= camera_offset[0]
            sprite.rect.y -= camera_offset[1]

    def execute_events(self):
        for event in pygame.event.get():  # all events that are registered are here being checkt

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        key = pygame.key.get_pressed()  # checks which keys are being pressed
        if key[pygame.K_SPACE]:
            self.load_next_level()

    def main(self):
        while self.playing == True:
            self.execute_events()
            self.update()
            self.draw_screen()
            self.clock.tick(FPS)
            pygame.display.update()
        self.running = False

    def game_over(self):
        pass
