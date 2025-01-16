from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups,collision_sprites):
        super().__init__(groups)
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}
        ##self.load_images()
        ##self.state, self.frame_index = 'down', 0
        self.image = pygame.image.load("assets/farby/sprite_1.png").convert_alpha()
        self.rect = self.image.get_frect(center = position)
        self.hitbox_rect = self.rect
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites
        self.gravity = 250
        self.standing = False
        self.momentum = 0
        self.color = "red"
        self.star_pos = position
        self.groups = groups
        self.collected_stars = 0


    def load_images(self):
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('assets','player',state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surface = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surface)

    def animate(self, delta):
        if self.direction.x != 0:
            self.state = 'right' if self.direction.x > 0 else 'left'
        if self.direction.y != 0:
            self.state = 'down' if self.direction.y > 0 else 'up'
        self.frame_index = (self.frame_index + 5 * delta) if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index)%len(self.frames[self.state])]

    def move(self, delta):
        self.hitbox_rect.x += self.direction.x * self.speed * delta
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * delta
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center



    def collision(self, direction):
        for sprite in self.collision_sprites:

            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0:
                        self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox_rect.left = sprite.rect.right
        for sprite in self.groups:
            if sprite.rect.colliderect(self.hitbox_rect) and sprite != self:
                #print(sprite.color,self.color)
                if(sprite.color == self.color):
                    continue
                elif((self.color == 'red' and sprite.color == "green")
                    or (self.color == 'green' and sprite.color == "blue")
                    or (self.color == 'blue' and sprite.color == "red")):

                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox_rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.hitbox_rect.left = sprite.rect.right
                    else:
                        if (self.gravity < 0):
                            self.hitbox_rect.top = sprite.rect.bottom
                        else:
                            self.hitbox_rect.bottom = sprite.rect.top
                            self.standing = True
                elif((self.color == 'red' and sprite.color == "blue")
                    or(self.color == 'blue' and sprite.color == "green")
                    or(self.color == 'green' and sprite.color == "red")):
                    self.kill()
                elif(sprite.color == "yellow"):
                    sprite.color = "white"
                    sprite.image = pygame.image.load("assets/farby/sprite_5.png").convert_alpha()
                    self.collected_stars += 1
                elif (sprite.color == "spikeUPnon"):
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox_rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.hitbox_rect.left = sprite.rect.right






    def drop(self,delta):

        if(self.gravity < 250):
            self.gravity += 10
        if(not self.standing):
            self.hitbox_rect.y += self.gravity * delta
        for sprite in self.collision_sprites:
            if(sprite.rect.colliderect(self.hitbox_rect)):
                if(self.gravity < 0):
                    self.hitbox_rect.top = sprite.rect.bottom
                else:
                    self.hitbox_rect.bottom = sprite.rect.top
                    self.standing = True
        for sprite in self.groups:
            if sprite.rect.colliderect(self.hitbox_rect) and sprite != self:
                ##print(sprite.color,self.color)
                if(sprite.color == self.color):
                    continue
                elif((self.color == 'red' and sprite.color == "green")
                    or (self.color == 'green' and sprite.color == "blue")
                    or (self.color == 'blue' and sprite.color == "red")):
                    if (self.gravity < 0):
                        self.hitbox_rect.top = sprite.rect.bottom
                    else:
                        self.hitbox_rect.bottom = sprite.rect.top
                        self.standing = True
                elif(sprite.color == "spikeUPnon"):
                    if (self.gravity > 0):
                        self.hitbox_rect.bottom = sprite.rect.top
                        self.kill()
    def kill(self):
        self.speed = 500
        self.gravity = 250
        self.standing = False
        self.momentum = 0
        self.color = "red"
        self.hitbox_rect.topleft = self.star_pos





    def input(self):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_UP] and self.standing):
            self.gravity = -800
            self.standing = False
        if(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] and self.standing):
            self.standing = False
        self.direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction
        if(keys[pygame.K_1]):
            self.color = "red"
            self.image = pygame.image.load("assets/farby/sprite_1.png").convert_alpha()
            self.standing = False
        if(keys[pygame.K_2]):
            self.color = "green"
            self.image = pygame.image.load("assets/farby/sprite_2.png").convert_alpha()
            self.standing = False
        if(keys[pygame.K_3]):
            self.color = "blue"
            self.image = pygame.image.load("assets/farby/sprite_3.png").convert_alpha()
            self.standing = False


    def update(self, delta):


        self.input()
        self.drop(delta)
        self.move(delta)
        print(self.momentum)
        if(self.momentum > 0):
            self.momentum -= 1

        ##self.animate(delta)