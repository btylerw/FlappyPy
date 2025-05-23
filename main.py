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

# Creates game objects
player = Character(100, 100, "img/pythonlogo.png")
pipe = Pipe(500, 500, "img/pipe.png", SCREEN_HEIGHT, SCREEN_WIDTH)
# Creating sprite groups for rendering/collision detection
players = pygame.sprite.Group()
pipes = pygame.sprite.Group()
players.add(player)
pipes.add(pipe)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # Collision detection between the player and any pipe on the screen
    collision = pygame.sprite.spritecollide(player, pipes, False)
    if collision:
        print("Collision detected")
    player.update()
    pipes.update()
    players.draw(screen)
    pipes.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()