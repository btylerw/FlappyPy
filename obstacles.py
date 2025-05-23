import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, screen_height, screen_width):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5
    
    def checkEdges(self):
        if self.rect.right < 0:
            self.rect.topleft = (self.x, self.y)

    def update(self):
        self.rect.x -= self.speed
        self.checkEdges()