#
# To activate the virtual environment, first run: source venv/bin/activate 

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    # Set containers BEFORE creating instances
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable,)  # Note the comma to make it a tuple
    Shot.containers = (shots, updatable, drawable)

    # Instantiate objects AFTER setting containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Add player manually (since it doesn't use containers)
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

        for roid in asteroid_group:
            for shot in shots:
                if shot.collides_with(roid):
                    roid.split(asteroidfield)
                    shot.kill()
            if roid.collides_with(player):
                print(" - - - G a m e   o v e r ! - - - ")
                exit()


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