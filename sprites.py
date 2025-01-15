from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self,position, file_path,groups):
        super().__init__(groups)
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self,position,file_path,groups):
        super().__init__(groups)
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)