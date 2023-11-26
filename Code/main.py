import pygame
from sprite import *
from config import *
import sys
import turtle
from labrinth_generator import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock() #framerate
        self.running = True 
        #self.overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        #self.overlay.fill((0, 0, 0, 128))    

    def new(self):
        # when a new game starts 
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates() # hier können wir unsere Sprites reintun
        self.blocks= pygame.sprite.LayeredUpdates()
        self.enemies= pygame.sprite.LayeredUpdates()
        self.attacks= pygame.sprite.LayeredUpdates()
        ##self.player = Player(self,1,2)
        self.create_level() 
    def update(self):
        self.all_sprites.update()
    def create_level(self):
        level = Maze(20,20,10,1)
        for i,row in enumerate(level.maze):
            for j,colum in enumerate(row):
                if colum =="X":
                    Block(self,j,i,True)
                if colum == "P":
                    self.player = Player(self,j,i)
                    Floor(self,j,i)
                if colum == ".":
                    x = random.randint(0,10)
                    if x == 0:

                        Block(self,j,i,False)
                    else:
                        Floor(self,j,i)
    
    def draw(self):

        self.screen.fill(BLACK)
        ''''''''''
        self.all_sprites.draw(self.screen)
        
        camera_offset = [0,0]
        # Update camera offset to center on the player
        camera_offset[0] = (WIN_WIDTH // 2) - self.player.rect.x
        camera_offset[1] = (WIN_HEIGHT // 2) - self.player.rect.y

        # Draw sprites at adjusted positions based on camera offset
        for sprite in self.all_sprites:
            sprite.rect.x += camera_offset[0]
            sprite.rect.y += camera_offset[1]
        '''
        self.all_sprites.draw(self.screen)

        # Reset sprite positions after drawing
        #for sprite in self.all_sprites:
         #   sprite.rect.x -= camera_offset[0]
          #  sprite.rect.y -= camera_offset[1]

        self.clock.tick(FPS)
        pygame.display.update()
        self.clock.tick(FPS)
        #self.screen.blit(self.overlay, (0, 0))
        pygame.display.update()
    def events(self):
        for event in pygame.event.get():# all events that are registrated are here beeing checkt

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        key = pygame.key.get_pressed()#checks which keys are being pressed
        if key[pygame.K_SPACE]:
            self.new()
    def main(self):
        while self.playing == True:
            self.events()
            self.update()
            self.draw()
        self.running = False
    def game_over(self):
        pass

g = Game()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()

