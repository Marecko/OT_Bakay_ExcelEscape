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
        self.stop = -1
        self.help = 0
        self.font = pygame.font.Font(None, 36)
        self.all_deaths = 0
        self.did_animation = False



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

    def animate_all_door(self,delta):
        if (self.stop > 3000):
            if (self.help <= 0):
                self.help = 2000
            self.help -= delta * 1000
            self.animate_door_movement(delta)
        elif (self.stop > 2000):
            self.animate_door()
        else:
            if (self.help <= 0):
                self.help = 2000
            self.help -= delta * 1000
            self.animate_door_movement_back(delta)
        self.stop -= delta * 1000

        if (self.stop < 0):
            self.player.controls = True
    def animate_door(self):
        self.all_sprites.draw(self.door.rect.center)
        if(self.stop < 2000):
            self.door.image = pygame.image.load("assets/farby/sprite_2.png")
        elif(self.stop < 2500):
            self.door.image = pygame.image.load("assets/farby/sprite_3.png")
        elif(self.stop < 3000):
            self.door.image = pygame.image.load("assets/farby/sprite_4.png")




    def animate_door_movement(self,delta):
        pos_x = self.door.rect.x - ((self.door.rect.x - self.player.rect.x) * (self.help  / 2000))
        pos_y = self.door.rect.y - ((self.door.rect.y - self.player.rect.y) * (self.help  / 2000))
        self.all_sprites.draw((pos_x, pos_y))

    def animate_door_movement_back(self,delta):
        pos_x = self.door.rect.x - ((self.door.rect.x - self.player.rect.x) * (1-self.help / 2000))
        pos_y = self.door.rect.y - ((self.door.rect.y - self.player.rect.y) * (1-self.help / 2000))
        self.all_sprites.draw((pos_x, pos_y))


    def do_the_text_and_stuff(self):
        text_surface = self.font.render("Deaths this Level: " + self.player.deaths.__str__(), True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(10, 10))  # Position in top-left corner
        text_surface2 = self.font.render("Deaths all Levels: " + (self.all_deaths + self.player.deaths).__str__(), True,
                                         (255, 255, 255))
        text_rect2 = text_surface.get_rect(topleft=(10, 46))  # Position in top-left corner
        star_surface = self.font.render(
            "Stars: " + self.player.collected_stars.__str__() + " / " + self.number_of_stars.__str__(), True,
            (255, 255, 255))
        star_rect = text_surface.get_rect(topright=(WINDOW_WIDTH - 10, 10))
        image_surface = pygame.image.load("assets/HINT.png").convert_alpha()
        image_rect = image_surface.get_rect(topleft=(46, 10))
        # Draw text
        self.display_surface.blit(text_surface, text_rect)
        self.display_surface.blit(text_surface2, text_rect2)
        self.display_surface.blit(star_surface, star_rect)
        self.display_surface.blit(image_surface, image_rect)

    def run(self):
        while self.running:
            delta = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill('black')
            if(self.player.controls):
                self.all_sprites.draw(self.player.rect.center)
                self.all_sprites.update(delta)
            else:
                self.animate_all_door(delta)
            self.do_the_text_and_stuff()

            pygame.display.update()
            # self.clock.tick(60)
            if(self.player.collected_stars == self.number_of_stars and not self.did_animation):
                self.door.color = "open"
                self.player.controls = False
                self.stop = 5000
                self.did_animation = True


            self.end_level()

        pygame.quit()
        sys.exit()





    def end_level(self):
        for sprite in self.all_sprites:
            if(sprite.rect.colliderect(self.player.hitbox_rect) and sprite != self.player):
                if(sprite.color == "open"):
                    self.lvl+=1
                    self.all_deaths += self.player.deaths
                    self.did_animation = False
                    self.setup_map()








if __name__ == '__main__':
    print("fuck")
    game = Game()
    game.run()

