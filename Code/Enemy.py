import pygame
from config import *
import random


def get_movement_matrix(movement_matrix, labyrinth_length, labyrinth_width):
    for i in range(1, labyrinth_length-1):
        for j in range(1, labyrinth_width-1):
            if movement_matrix[i+1][j] + movement_matrix[i-1][j] + movement_matrix[i][j+1] + movement_matrix[i][j-1] != 2:
                movement_matrix[i][j] = 2
            elif movement_matrix[i+1][j] + movement_matrix[i][j+1] == 2 or movement_matrix[i+1][j] + movement_matrix[i][j-1] == 2 or movement_matrix[i-1][j] + movement_matrix[i-1][j+1] == 2:
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

    def update(self):
        self.movement()

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

    def enemy_movement(self, movement_matrix, labyrinth_length, labyrinth_width):
        for i in range(labyrinth_length):
            for j in range(labyrinth_width):
                if movement_matrix[i][j] == 3:
                    self.facing = random.choice(['up', 'down', 'right'])
                    if self.facing == 'left':
                        self.x_change -= ENEMY_SPEED
                    elif self.facing == 'up':
                        self.y_change += ENEMY_SPEED
                    else:
                        self.y_change -= ENEMY_SPEED
                if movement_matrix == 1.2:
                    self.facing = random.choice(['up', 'down', 'right'])
                    if self.facing == 'left':
                        self.x_change -= ENEMY_SPEED
                    elif self.facing == 'up':
                        self.y_change += ENEMY_SPEED
                    else:
                        self.y_change -= ENEMY_SPEED
                if movement_matrix == 1.1:
                    self.facing = random.choice(['up', 'down', 'right'])
                    if self.facing == 'left':
                        self.x_change -= ENEMY_SPEED
                    elif self.facing == 'up':
                        self.y_change += ENEMY_SPEED
                    else:
                        self.y_change -= ENEMY_SPEED
                if movement_matrix == 1:
                    self.facing = random.choice(['up', 'down', 'right'])
                    if self.facing == 'left':
                        self.x_change -= ENEMY_SPEED
                    elif self.facing == 'up':
                        self.y_change += ENEMY_SPEED
                    else:
                        self.y_change -= ENEMY_SPEED



