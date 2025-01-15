import csv

from settings import *
import sys
from sprites import *

from groups import AllSprites
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = AllSprites()
        self.color_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup_map()
    def setup_map(self):
        with open('ExportedData.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            map = []
            for row in csv_reader:
                map.append(row)
        print(map)
        ppos = []
        for i in range(len(map)):
            for j in range(len(map[i])):


                if (map[i][j] == '0'):
                    CollisionSprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_0.png",self.collision_sprites)
                if (map[i][j] == 'b'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_3.png", self.all_sprites,"blue")
                if (map[i][j] == '.'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites,"white")
                if(map[i][j] == 'r'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_1.png", self.all_sprites,"red")
                if (map[i][j] == 'g'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_2.png", self.all_sprites,"green")
                if (map[i][j] == 's'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_4.png", self.all_sprites,"yellow")
                if (map[i][j] == 'p'):
                    ppos = (j * TILE_SIZE, i * TILE_SIZE)
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites,"white")

        self.player = Player(ppos,self.all_sprites,self.collision_sprites)
        for i in range(len(map)):
            for j in range(len(map[i])):
                if (map[i][j] == 'f'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_0.png", self.all_sprites,"false")



    def run(self):
        while self.running:
            delta = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(delta)
            pygame.display.update()
            # self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    print("fuck")
    game = Game()
    game.run()

