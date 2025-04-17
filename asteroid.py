from circleshape import *
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass radius to parent's init
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (218, 165, 32), self.position, self.radius, 3)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroidfield):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle) * 1.2
            vector2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # Call the spawn method on the passed asteroidfield instance
            asteroidfield.spawn(new_radius, self.position, vector1)
            asteroidfield.spawn(new_radius, self.position, vector2)


