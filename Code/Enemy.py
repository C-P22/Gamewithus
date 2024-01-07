import pygame
from config import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies,self.game.destroyable
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.health = 1

        self.width = ENTITY_SIZE
        self.height = ENTITY_SIZE
        
        self.x_change = 0
        self.y_change = 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(ENEMY_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE + (TILE_SIZE - ENTITY_SIZE) // 2
        self.rect.y = y * TILE_SIZE + (TILE_SIZE - ENTITY_SIZE) // 2

        # the direction this enemy moved towards in the previous frame with the numbers 0, 1, 2, 3 representing right, up, left, down
        self.prev_mov_dir = random.randint(0, 3)
        self.prev_tile_pos = (-1, -1)

    def update(self):
        self.move()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0
        if self.health <= 0:
            self.kill()

    def move(self):
        # don't change direction if you're in the same tile as in the previous frame
        if self.prev_tile_pos != self.get_tile_position() and self.is_fully_inside_tile() or self.prev_mov_dir == -1:
            choice = self.choose_direction()
            self.prev_tile_pos = self.get_tile_position()
        else:
            choice = self.prev_mov_dir

        if choice == 0:
            self.x_change = ENEMY_SPEED
        elif choice == 1:
            self.y_change = ENEMY_SPEED
        elif choice == 2:
            self.x_change = -ENEMY_SPEED
        elif choice == 3:
            self.y_change = -ENEMY_SPEED
        
        self.prev_mov_dir = choice
    
    def choose_direction(self):
        x_pos, y_pos = self.get_tile_position()

        # can the enemy go right, up, left, down?
        can_go_in_direction = [True, True, True, True]
        # can't go into a wall
        if can_go_in_direction[0]:
            can_go_in_direction[0] = not self.game.is_wall_matrix[x_pos + 1][y_pos]
        if can_go_in_direction[1]:
            can_go_in_direction[1] = not self.game.is_wall_matrix[x_pos][y_pos + 1]
        if can_go_in_direction[2]:
            can_go_in_direction[2] = not self.game.is_wall_matrix[x_pos - 1][y_pos]
        if can_go_in_direction[3]:
            can_go_in_direction[3] = not self.game.is_wall_matrix[x_pos][y_pos - 1]

        # where can the enemy go?
        possible_options = []
        for i in range(4):
            if can_go_in_direction[i]:
                possible_options.append(i)
        
        if len(possible_options) == 0:
            return -1
        
        # if you can turn 180 and go the other direction but still have other options, don't
        if len(possible_options) > 1 and possible_options.__contains__((self.prev_mov_dir + 2) % 4) and self.prev_mov_dir != -1:
            possible_options.remove((self.prev_mov_dir + 2) % 4)

        return random.choice(possible_options)
    
    def get_tile_position(self):
        return (self.rect.x + TILE_SIZE // 2) // TILE_SIZE, (self.rect.y + TILE_SIZE // 2) // TILE_SIZE
    
    def is_fully_inside_tile(self):
        is_fully_inside_coloumn = ((self.rect.x + ENTITY_SIZE // 2) % TILE_SIZE) >= (ENTITY_SIZE / 2) and ((self.rect.x + ENTITY_SIZE // 2) % TILE_SIZE) <= (TILE_SIZE - ENTITY_SIZE / 2)
        is_fully_inside_row = ((self.rect.y + ENTITY_SIZE // 2) % TILE_SIZE) >= (ENTITY_SIZE / 2) and ((self.rect.y + ENTITY_SIZE // 2) % TILE_SIZE) <= (TILE_SIZE - ENTITY_SIZE / 2)
        return is_fully_inside_coloumn and is_fully_inside_row