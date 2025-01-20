from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups,collision_sprites):
        super().__init__(groups)
        self.frames = {"red": [], "green": [], "blue": []}
        self.load_images()
        self.image = pygame.image.load("assets/panacik/panacikred_0.png").convert_alpha()
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
        self.controls = True
        self.deaths = 0
        self.frame_timer = 0
        self.frame_interval = 0.2
        self.state = 0

    def load_images(self):
        for state in self.frames.keys():
            for i in range(4):
                image_path = f"assets/panacik/panacik{state}_{i}.png"
                self.frames[state].append(pygame.image.load(image_path).convert_alpha())


    def animate(self, delta):
        self.frame_timer += delta
        if self.frame_timer >= self.frame_interval:
            self.frame_timer = 0
            self.state = (self.state + 1) % len(self.frames[self.color])
            self.image = self.frames[self.color][self.state]


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
                if (sprite.color in ["spikeUPnon","spikeDOWNnon","spikeLEFTnon","spikeRIGHTnon"]):
                    self.kill()
                elif(sprite.color == self.color):
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
                if (sprite.color in ["spikeUPnon", "spikeDOWNnon", "spikeLEFTnon", "spikeRIGHTnon"]):
                    self.kill()
                if(sprite.color == "checkpoint"):
                    self.star_pos = sprite.rect.topleft

    def kill(self):
        self.deaths += 1
        self.speed = 500
        self.gravity = 250
        self.standing = False
        self.momentum = 0
        self.color = "red"
        self.hitbox_rect.topleft = self.star_pos





    def input(self):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_UP] and self.standing):
            self.gravity = -1100
            self.standing = False
        if(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] and self.standing):
            self.standing = False
        self.direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction
        if(keys[pygame.K_1]):
            self.color = "red"
            self.image = pygame.image.load("assets/panacik/panacikred_0.png").convert_alpha()
            self.standing = False
        if(keys[pygame.K_2]):
            self.color = "green"
            self.image = pygame.image.load("assets/panacik/panacikgreen_0.png").convert_alpha()
            self.standing = False
        if(keys[pygame.K_3]):
            self.color = "blue"
            self.image = pygame.image.load("assets/panacik/panacikblue_0.png").convert_alpha()
            self.standing = False



    def update(self, delta):

        if(self.controls):
            self.input()
        self.drop(delta)
        self.move(delta)


        if(self.momentum > 0):
            self.momentum -= 1

        self.animate(delta)