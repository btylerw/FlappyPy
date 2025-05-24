# Example file showing a circle moving on screen
import pygame
from character import Character
from obstacles import Pipe

# pygame setup
pygame.init()
pygame.display.set_caption("FlappyPy")
SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 72)

def renderTextWithBorder(text, font, text_color, border_color, border_width=2):
    base = font.render(text, True, text_color)
    size = base.get_width() + 2 * border_width, base.get_height() + 2 * border_width
    border_surface = pygame.Surface(size, pygame.SRCALPHA)

    for dx in [-border_width, 0, border_width]:
        for dy in [-border_width, 0, border_width]:
            if dx != 0 or dy != 0:
                border_surface.blit(font.render(text, True, border_color), (dx + border_width, dy + border_width))
    
    border_surface.blit(base, (border_width, border_width))
    return border_surface

startMessage = renderTextWithBorder("Press Enter to Start. Press Space to Jump", font, WHITE, BLACK, border_width=2)
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
running = True
# Game is paused on launch
start = False
dt = 0
# Keeps score
score = 0
# Keeps track of high score
high_score = 0
# Flag to allow score to only update a single time
has_passed = False

# Creates game objects
player_image = pygame.image.load("img/pythonlogo.png")
# Resizing player image
player_image = pygame.transform.scale(player_image, (64, 64))
player = Character(100, 100, player_image, SCREEN_HEIGHT)
# Loading the pipe image to use in obstacles class
pipe_image = pygame.image.load("img/pipe.png")
# Creating a pipe image that is flipped upside down
flipped_pipe_image = pygame.transform.flip(pipe_image, False, True)
# Creating two pipes that will have a small space between them that the player must navigate through
pipe = Pipe(1000, 500, pipe_image, SCREEN_HEIGHT, SCREEN_WIDTH)
flipped_pipe = Pipe(1000, 100, flipped_pipe_image, SCREEN_HEIGHT, SCREEN_WIDTH)
# Creating sprite groups for rendering/collision detection
players = pygame.sprite.Group()
pipes = pygame.sprite.Group()
players.add(player)
pipes.add(pipe)
pipes.add(flipped_pipe)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing everything on the screen before any physics happen
    # Keeps user's score
    message = f"Score: {str(score)}"
    highScore = f"High Score: {str(high_score)}"
    # Renders current score to screen
    scoreMessage = renderTextWithBorder(message, font, WHITE, BLACK, border_width=2)
    highScoreMessage = renderTextWithBorder(highScore, font, WHITE, BLACK, border_width=2)
    screen.fill("purple")
    players.draw(screen)
    pipes.draw(screen)
    screen.blit(scoreMessage, (SCREEN_WIDTH/2, 50))
    screen.blit(highScoreMessage, (SCREEN_WIDTH, 50))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        # Game starts once player presses Enter
        start = True
    if start:
        # Collision detection between the player and any pipe on the screen
        collision = pygame.sprite.spritecollide(player, pipes, False)
        if collision or player.crashed:
            # If we detect a collision, the game is over
            # Reset positions for everything and pause the game
            player.reset()
            for pipe in pipes:
                pipe.reset()
            start = False
            score = 0
        # Physics happen
        for pipe in pipes:
            # Checking if player has moved past pipes, if so update score
            if not has_passed and player.rect.left > pipe.rect.right:
                score += 1
                # Set flag to not continuously update score
                has_passed = True
            # Reset flag to allow score to update again
            if has_passed and player.rect.left < pipe.rect.right:
                has_passed = False
        player.update()
        pipes.update()
        high_score = max(high_score, score)
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

pygame.quit()