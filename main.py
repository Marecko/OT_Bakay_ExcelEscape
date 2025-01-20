import csv
from importlib.util import source_hash

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


        self.stop = -1
        self.help = 0
        self.font = pygame.font.Font(None, 36)
        self.all_deaths = 0
        self.did_animation = False
        self.animate_cp = False
        self.cp = -1
        self.done_cp = []
        self.over = False
        self.setup_map()
    def setup_map(self):
        self.level_completed = False
        self.all_sprites = AllSprites()
        self.color_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.number_of_stars = 0
        self.checkpoints = []
        self.did_animation = False
        self.stop = -1
        self.done_cp = []

        mapy = ["assets/levely/MAPA_LVL_1.csv","assets/levely/MAPA_LVL_2.csv","assets/levely/MAPA_LVL_3.csv"]
        with open(mapy[self.lvl], mode='r') as file:
            csv_reader = csv.reader(file)
            map = []
            for row in csv_reader:
                map.append(row)

        ppos = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if (map[i][j] == '0'):
                    CollisionSprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_0.png",self.collision_sprites)
                elif (map[i][j] == 'n'):
                    CollisionSprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/zem_0.png", self.collision_sprites)
                elif (map[i][j] == 'b'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/blue.png", self.all_sprites,"blue")
                elif (map[i][j] == '.'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites,"white")
                elif(map[i][j] == 'r'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/red.png", self.all_sprites,"red")
                elif (map[i][j] == 'g'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/green.png", self.all_sprites,"green")
                elif (map[i][j] == 's'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites, "white")
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/star_0.png", self.all_sprites,"yellow")
                    self.number_of_stars +=1
                elif (map[i][j] == 'p'):
                    ppos = (j * TILE_SIZE, i * TILE_SIZE)
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites,"white")
                elif (map[i][j] == 'd'):
                    self.door = Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/dvere/dvere_0.png", self.all_sprites, "closed")
                elif (map[i][j] == '2'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spikes/pichlac_2.png", self.all_sprites, "spikeUPnon")
                elif (map[i][j] == '4'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spikes/pichlac_1.png", self.all_sprites, "spikeLEFTnon")
                elif (map[i][j] == '6'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spikes/pichlac_3.png", self.all_sprites, "spikeRIGHTnon")
                elif (map[i][j] == '8'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/spikes/pichlac_0.png", self.all_sprites, "spikeDOWNnon")
                elif (map[i][j] == "c"):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/sprite_5.png", self.all_sprites, "white")
                    self.checkpoints.append(Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/checkpoint/checkpoint_0.png", self.all_sprites, "checkpoint"))

        self.player_start_pos = ppos
        self.player = Player(ppos,self.all_sprites,self.collision_sprites)

        for i in range(len(map)):
            for j in range(len(map[i])):
                if (map[i][j] == 'f'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/fake_down.png", self.all_sprites,"false")
                if(map[i][j] == 'n'):
                    Sprite((j * TILE_SIZE, i * TILE_SIZE), "assets/farby/fake_top.png", self.all_sprites, "false")

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
        if(self.stop < 2100):
            self.door.image = pygame.image.load("assets/dvere/dvere_2.png")
        elif(self.stop < 2500):
            self.door.image = pygame.image.load("assets/dvere/dvere_1.png")
        elif(self.stop < 3000):
            self.door.image = pygame.image.load("assets/dvere/dvere_0.png")




    def animate_door_movement(self,delta):
        pos_x = self.door.rect.x - ((self.door.rect.x - self.player.rect.x) * (self.help  / 2000))
        pos_y = self.door.rect.y - ((self.door.rect.y - self.player.rect.y) * (self.help  / 2000))
        self.all_sprites.draw((pos_x, pos_y))

    def animate_door_movement_back(self,delta):
        pos_x = self.door.rect.x - ((self.door.rect.x - self.player.rect.x) * (1-self.help / 2000))
        pos_y = self.door.rect.y - ((self.door.rect.y - self.player.rect.y) * (1-self.help / 2000))
        self.all_sprites.draw((pos_x, pos_y))


    def do_the_text_and_stuff(self):
        text_surface = self.font.render("Deaths this Level: " + self.player.deaths.__str__(), True, (128, 128, 128))
        text_rect = text_surface.get_rect(topleft=(10, 10))
        text_surface2 = self.font.render("Deaths all Levels: " + (self.all_deaths + self.player.deaths).__str__(), True,
                                         (128, 128, 128))
        text_rect2 = text_surface2.get_rect(topleft=(10, 46))
        star_surface = self.font.render(
            "Stars: " + self.player.collected_stars.__str__() + " / " + self.number_of_stars.__str__(), True,
            (128, 128, 128))
        star_rect = text_surface.get_rect(topright=(WINDOW_WIDTH - 10, 10))
        image_surface = pygame.image.load("assets/rgb_0.png").convert_alpha()
        image_surface = pygame.transform.scale(image_surface, (150, 150))

        image_rect = image_surface.get_rect(topleft=(10, 200))

        self.display_surface.blit(text_surface, text_rect)
        self.display_surface.blit(text_surface2, text_rect2)
        self.display_surface.blit(star_surface, star_rect)
        self.display_surface.blit(image_surface, image_rect)

    def animate_checkpoint(self,delta,cp):
        self.stop -= delta * 1000
        if (self.stop < 500):
            self.animate_cp = False
            self.checkpoints[cp].image = pygame.image.load("assets/checkpoint/checkpoint_3.png")
            self.stop = -1
        elif (self.stop < 1000):
            self.checkpoints[cp].image = pygame.image.load("assets/checkpoint/checkpoint_2.png")
        elif (self.stop < 1500):
            self.checkpoints[cp].image = pygame.image.load("assets/checkpoint/checkpoint_1.png")


    def run(self):
        while self.running:
            delta = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if(self.over):
                pass
            else:

                self.display_surface.fill('black')
                if(self.player.controls):
                    self.all_sprites.draw(self.player.rect.center)
                    self.all_sprites.update(delta)
                else:
                    self.animate_all_door(delta)
                self.do_the_text_and_stuff()

            if(self.player_start_pos != self.player.star_pos):
                self.player_start_pos = self.player.star_pos
                for i in range(len(self.checkpoints)):
                    if(self.checkpoints[i].rect.topleft == self.player_start_pos and self.checkpoints[i].color != "done"):
                        self.stop = 2000
                        self.cp = i
                        self.animate_cp = True
                        self.checkpoints[i].color = "done"
                        self.animate_checkpoint(delta,self.cp)
                        self.done_cp.append(self.checkpoints[i])
            if(self.animate_cp):
                self.animate_checkpoint(delta, self.cp)



            pygame.display.update()


            if(self.player.collected_stars == self.number_of_stars and not self.did_animation):
                self.door.color = "open"
                self.player.controls = False
                self.stop = 5000
                self.did_animation = True

            if(not self.level_completed):
                self.end_level()


        pygame.quit()
        sys.exit()

    def die_ende(self):

        self.display_surface.fill('white')
        self.background_image = pygame.image.load("assets/rgb_0.png")
        self.background_image = pygame.transform.scale(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.blit(self.background_image, (0, 0))
        sss = ("Thanks for playing ExcelEscape\n"
               "Created by :Marek Bakay\n"
               "\n\n\n"
               "Deaths all Levels: ")
        text_surface2 = self.font.render(sss + (self.all_deaths + self.player.deaths).__str__(), True,
                                         (0, 0, 0))
        text_rect2 = text_surface2.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.display_surface.blit(text_surface2, text_rect2)



    def end_level(self):
        for sprite in self.all_sprites:
            if(sprite.rect.colliderect(self.player.hitbox_rect) and sprite != self.player):
                if(sprite.color == "open"):
                    self.level_completed = True
                    self.lvl+=1
                    self.all_deaths += self.player.deaths


                    if(self.lvl == 3):
                        self.over = True
                        self.die_ende()
                    else:

                        self.setup_map()








if __name__ == '__main__':

    game = Game()
    game.run()

