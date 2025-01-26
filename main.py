#
# To activate the virtual environment, first run: source venv/bin/activate 

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Instantiate Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add player to groups manually
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Hook updates
        for sprite in updatable:
            sprite.update(dt)

        # Draw the sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Move to the next frame
        pygame.display.flip()

        # Update dt with delta time after limiting to 60 FPS
        dt = clock.tick(60) / 1000

        # Output the current FPS in the console
        # fps = clock.get_fps()
        # print(f"FPS: {fps}")

if __name__ == "__main__":
    main()