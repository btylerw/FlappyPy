import pygame

# Character class, loads image used, gets it's hitbox, and updates it's velocity
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image, screen_height, speed=10):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.screen_height = screen_height
        self.speed = speed
        self.crashed = False
    
    def handleKeys(self):
        keys = pygame.key.get_pressed()
        # When spacebar is pressed, character will move up
        if keys[pygame.K_SPACE]:
            self.speed = 10
    
    # Resets position and speed
    def reset(self):
        self.speed = 10
        self.rect.topleft = (self.x, self.y)
        self.crashed = False

    def update(self):
        # Check for key press
        self.handleKeys()
        # Character will constantly move up or down
        self.rect.y -= self.speed
        # Velocity constantly decreases whenever spacebar is not pressed, causing character to fall
        self.speed -= 1
        # Setting a max falling speed
        if (self.speed < -10):
            self.speed = -10
        # Resets game when user crashes into ground
        if self.rect.bottom > self.screen_height - 500:
            self.crashed = True