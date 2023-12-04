import pygame
from sprite import *
from config import *
import sys
import turtle
from labrinth_generator import Maze
import sound_handler


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        sound_handler.SoundHandler.play_level_soundtrack()
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

    def load_next_level(self):
        self.labrinth_length += 3
        self.labrinth_width += 3
        self.initialize_game_objects()
        self.create_level()
        pass

    def initialize_game_objects(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # hier können wir unsere Sprites reintun
        self.blocks = pygame.sprite.LayeredUpdates()
        self.portal = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.powerup = pygame.sprite.LayeredUpdates()

    def create_level(self):
        self.wall_matrix = [[0]*self.labrinth_length]*self.labrinth_width
        level = Maze(self.labrinth_length, self.labrinth_width, self.labrinth_length // 2, self.labrinth_width // 2)
        for i, row in enumerate(level.maze):
            for j, colum in enumerate(row):
                self.wall_matrix[i][j] = 0
                if colum == "X":
                    self.wall_matrix[i][j] = 1
                    Wall(self, j, i, True)
                if colum == "P":
                    self.player = Player(self, j, i)
                    Floor(self, j, i)
                if colum == ".":
                    x = random.randint(0, 50)
                    if x < 10:
                        self.wall_matrix[i][j] = 1
                        Wall(self, j, i, False)
                    elif x == 10:
                        Floor(self, j, i)
                        Powerup(self, j, i)
                    elif x == 20:
                        Floor(self, j, i)
                        Enemy(self, j, i)
                    else:
                        Floor(self, j, i)
                if colum == "E":
                    Floor(self, j, i)
                    Portal(self, j, i)

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


game = Game()
game.load_next_level()
while game.running:
    game.main()
    game.game_over()

pygame.quit()
sys.exit()
