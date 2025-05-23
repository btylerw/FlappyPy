# Example file showing a circle moving on screen
import pygame
from character import Character
from obstacles import Pipe

# pygame setup
pygame.init()
SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
running = True
dt = 0

# Creates player character
player = Character(100, 100, "img/pythonlogo.png")
pipes = Pipe(500, 500, "img/pipe.png", SCREEN_HEIGHT, SCREEN_WIDTH)
all_sprites = pygame.sprite.Group()
# Adds player to sprites that will be rendered
all_sprites.add(player)
all_sprites.add(pipes)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    all_sprites.update()
    all_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()