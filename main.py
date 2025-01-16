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
        self.lvl = 0
        self.setup_map()




    def setup_map(self):
        self.all_sprites = AllSprites()
        self.color_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.number_of_stars = 0
        mapy = ["ExportedDataSPIKE.csv",'ExportedData2.csv']
        with open(mapy[self.lvl], mode='r') as file:
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
                elif (map[i][j] == 'b'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_3.png", self.all_sprites,"blue")
                elif (map[i][j] == '.'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites,"white")
                elif(map[i][j] == 'r'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_1.png", self.all_sprites,"red")
                elif (map[i][j] == 'g'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_2.png", self.all_sprites,"green")
                elif (map[i][j] == 's'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_4.png", self.all_sprites,"yellow")
                    self.number_of_stars +=1
                elif (map[i][j] == 'p'):
                    ppos = (j * TILE_SIZE, i * TILE_SIZE)
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites,"white")
                elif (map[i][j] == 'd'):
                    self.door = Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_1.png", self.all_sprites, "closed")
                elif (map[i][j] == '2'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spike_0.png", self.all_sprites, "spikeUPnon")
                elif (map[i][j] == '4'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spike_2.png", self.all_sprites, "spikeLEFTnon")
                elif (map[i][j] == '6'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spike_3.png", self.all_sprites, "spikeRIGHTnon")
                elif (map[i][j] == '8'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spike_1.png", self.all_sprites, "spikeDOWNnon")

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
            if(self.player.collected_stars == self.number_of_stars):
                self.door.image = pygame.image.load("assets/farby/sprite_2.png").convert_alpha()
                self.door.color = "open"
            self.end_level()

        pygame.quit()
        sys.exit()





    def end_level(self):
        for sprite in self.all_sprites:
            if(sprite.rect.colliderect(self.player.hitbox_rect) and sprite != self.player):
                if(sprite.color == "open"):
                    self.lvl+=1
                    self.setup_map()
                    self.player.kill()






if __name__ == '__main__':
    print("fuck")
    game = Game()
    game.run()

