import pygame
from config import *
import random


def get_movement_matrix(movement_matrix, labyrinth_length, labyrinth_width):
    for i in range(1, labyrinth_length - 1):
        for j in range(1, labyrinth_width - 1):
            if movement_matrix[i + 1][j] + movement_matrix[i - 1][j] + movement_matrix[i][j + 1] + movement_matrix[i][j - 1] != 2:
                movement_matrix[i][j] = 2
            elif movement_matrix[i + 1][j] + movement_matrix[i][j + 1] == 2 or movement_matrix[i + 1][j] + \
                    movement_matrix[i][j - 1] == 2 or movement_matrix[i - 1][j] + movement_matrix[i - 1][j + 1] == 2:
                movement_matrix[i][j] = 2
    return movement_matrix


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = ENTITY_SIZE
        self.height = ENTITY_SIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(30, 50)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(ENEMY_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.matrix_x = 0
        self.matrix_y = 0
        self.matrix_tile = 0

    def update(self):
        self.enemy_movement(get_movement_matrix(self.game.enemie_movement, self.game.labrinth_length, self.game.labrinth_width))

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def enemy_movement(self, movement_matrix):
        self.facing = random.choice(['up', 'down', 'left', 'right'])
        if self.facing == 'up' and movement_matrix[self.matrix_x][self.matrix_y] == 1:  # schaut, ob es an der Position eine Wand ist
            if movement_matrix[self.matrix_y + 1][self.matrix_x] != 0:  # schaut, ob der nächste Tile eine Wand ist
                self.y_change += ENEMY_SPEED
                self.matrix_tile += ENEMY_SPEED
                if self.matrix_tile >= TILE_SIZE:  # bewegt so lange bis es ein Tile durchläuft
                    self.matrix_tile = self.matrix_tile - TILE_SIZE
                    self.matrix_y += 1
        elif self.facing == 'down' and movement_matrix[self.matrix_y][self.matrix_x] == 1:
            if movement_matrix[self.matrix_y - 1][self.matrix_x] != 0:
                self.y_change -= ENEMY_SPEED
                self.matrix_tile += ENEMY_SPEED
                if self.matrix_tile >= TILE_SIZE:
                    self.matrix_tile = self.matrix_tile - TILE_SIZE
                    self.matrix_y -= 1
        elif self.facing == 'left' and movement_matrix[self.matrix_y][self.matrix_x] == 1:
            if movement_matrix[self.matrix_y][self.matrix_x - 1] != 0:
                self.x_change -= ENEMY_SPEED
                self.matrix_tile += ENEMY_SPEED
                if self.matrix_tile >= TILE_SIZE:
                    self.matrix_tile = self.matrix_tile - TILE_SIZE
                    self.matrix_x -= 1
        else:
            if movement_matrix[self.matrix_y][self.matrix_x + 1] != 0:
                self.y_change += ENEMY_SPEED
                self.matrix_tile += ENEMY_SPEED
                if self.matrix_tile >= TILE_SIZE:
                    self.matrix_tile = self.matrix_tile - TILE_SIZE
                    self.matrix_x += 1

            if movement_matrix[self.matrix_y][self.matrix_x] == 2:
                self.facing = random.choice(['up', 'down', 'left', 'right'])
                if self.facing == 'up' and movement_matrix[self.matrix_y][self.matrix_x] == 2:
                    if movement_matrix[self.matrix_y + 1][self.matrix_x] != 0:
                        self.y_change += ENEMY_SPEED
                        self.matrix_tile += ENEMY_SPEED
                        if self.matrix_tile >= TILE_SIZE:
                            self.matrix_tile = self.matrix_tile - TILE_SIZE
                            self.matrix_y += 1
                elif self.facing == 'down' and movement_matrix[self.matrix_y][self.matrix_x] == 2:
                    if movement_matrix[self.matrix_y - 1][self.matrix_x] != 0:
                        self.y_change -= ENEMY_SPEED
                        self.matrix_tile += ENEMY_SPEED
                        if self.matrix_tile >= TILE_SIZE:
                            self.matrix_tile = self.matrix_tile - TILE_SIZE
                            self.matrix_y -= 1
                elif self.facing == 'left' and movement_matrix[self.matrix_y][self.matrix_x] == 2:
                    if movement_matrix[self.matrix_y][self.matrix_x - 1] != 0:
                        self.x_change -= ENEMY_SPEED
                        self.matrix_tile += ENEMY_SPEED
                        if self.matrix_tile >= TILE_SIZE:
                            self.matrix_tile = self.matrix_tile - TILE_SIZE
                            self.matrix_x -= 1
                elif self.facing == 'right' and movement_matrix[self.matrix_y][self.matrix_x] == 2:
                    if movement_matrix[self.matrix_y][self.matrix_x + 1] != 0:
                        self.x_change += ENEMY_SPEED
                        self.matrix_tile += ENEMY_SPEED
                        if self.matrix_tile >= TILE_SIZE:
                            self.matrix_tile = self.matrix_tile - TILE_SIZE
                            self.matrix_x += 1
