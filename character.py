import pygame

# Character class, loads image used, gets it's hitbox, and updates it's velocity
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, speed=5):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
    
    def handleKeys(self):
        keys = pygame.key.get_pressed()
        # When spacebar is pressed, character will move up
        if keys[pygame.K_SPACE]:
            self.speed = 5
    
    def update(self):
        # Check for key press
        self.handleKeys()
        # Character will constantly move up or down
        self.rect.y -= self.speed
        # Velocity constantly decreases whenever spacebar is not pressed, causing character to fall
        self.speed -= 0.5
        # Setting a max falling speed
        if (self.speed < -5):
            self.speed = -5