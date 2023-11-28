import pygame
from sprite import *
from config import *
import sys
import turtle
from labrinth_generator import Maze
from icecream import ic 

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock() #framerate
        self.running = True 
        self.x = 0
        self.labrinth_lenght = 8
        self.labrinth_wigth = 8
        #self.overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        #self.overlay.fill((0, 0, 0, 128))    

    def new(self):
        # when a new game starts 
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates() # hier können wir unsere Sprites reintun
        self.blocks= pygame.sprite.LayeredUpdates()
        self.waende = pygame.sprite.LayeredUpdates()
        self.portal= pygame.sprite.LayeredUpdates()
        self.enemies= pygame.sprite.LayeredUpdates()
        self.attacks= pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.powerup =  pygame.sprite.LayeredUpdates()
        self.weapons =  pygame.sprite.LayeredUpdates()
        self.destroyable =  pygame.sprite.LayeredUpdates()
        ##self.player = Player(self,1,2)
        self.create_level(self.labrinth_lenght,self.labrinth_wigth) 
    def update(self):
        if self.player.update():
            self.labrinth_lenght += 3
            self.labrinth_wigth += 3
            self.new()
        self.blocks.update()
        #self.weapons.update()
    def create_level(self,lenght,wigth):
        level = Maze(lenght,wigth,lenght//2,wigth//2)
        for i,row in enumerate(level.maze):
            for j,colum in enumerate(row):
                Floor(self,j,i)
                if colum =="X":
                    Wall(self,j,i,True)
                if colum == "P":
                    self.player = Player(self,j,i)
                    Floor(self,j,i) 
                if colum == ".":
                    
                    x = random.randint(0,50)
                
                    if x < 10:
                        

                        Wall(self,j,i,False)
                    elif x == 10:

                        Powerup(self,j,i)

                if colum == "E":
                    Floor(self,j,i)
                    Portal(self,j,i) 
    def draw(self):
        self.screen.fill(BLACK)
        ''''''''''
        self.all_sprites.draw(self.screen)
        '''  
        camera_offset = [0,0]
        # Update camera offset to center on the player
        camera_offset[0] = (WIN_WIDTH // 2) - self.player.rect.x
        camera_offset[1] = (WIN_HEIGHT // 2) - self.player.rect.y
        #ic(camera_offset[0],camera_offset[1])
        # Draw sprites at adjusted positions based on camera offset
        for sprite in self.all_sprites:
            sprite.rect.x += camera_offset[0]
            sprite.rect.y += camera_offset[1]
        
        self.all_sprites.draw(self.screen)

        # Reset sprite positions after drawing
        #for sprite in self.all_sprites:
        #    sprite.rect.x -= camera_offset[0]
        #    sprite.rect.y -= camera_offset[1]   
        #ligth = Light(True,300)
       # x = random.randint(0,9)
        #self.x = x 
        #image = pygame.image.load(f"img/light/{self.x}.png")
       # image_rect =image.get_rect()
        #self.screen.blit(image, image_rect)
        self.clock.tick(FPS)
        pygame.display.update()
        self.clock.tick(FPS)
        # self.screen.blit(self.overlay, (0, 0))
        pygame.display.update()
    def events(self):
        for event in pygame.event.get():  # all events that are registered are here being checkt
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        key = pygame.key.get_pressed()  # checks which keys are being pressed
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
