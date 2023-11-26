from sprite import *
from config import *
import sys
<<<<<<< HEAD
from Code_Guiheng.powerup import *
=======

>>>>>>> 9925be4eb69e9453939c6b0a3e2141fac9c36efc


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()  # framerate
        self.running = True

    def new(self):
        # when a new game starts 
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()# hier können wir unsere Sprites reintun
        self.powerup = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        # self.player = Player(self,1,2)
        self.create_level()

    def update(self):
        self.all_sprites.update()

    def create_level(self):
        for i, row in enumerate(level_1):
            for j, colum in enumerate(row):
                if colum == "X":
                    Block(self, j, i)
                if colum == "P":
                    Player(self, j, i)
                if colum == "B":
                    print(j,i)
                    POWERUP(self, j, i)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():  # all events that are registrated are here beeing checkt

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

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
