import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, screen_height, screen_width):
        super().__init__()
        # Set image to passed in image
        self.image = image
        # Saving initial x, y coordinates to reset later
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5
    
    def checkEdges(self):
        # Resetting position when pipe goes off screen
        if self.rect.right < 0:
            self.rect.topleft = (self.x, self.y)

    # Resets position
    def reset(self):
        self.rect.topleft = (self.x, self.y)

    def update(self):
        # Move pipe to the left
        self.rect.x -= self.speed
        self.checkEdges()