from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # Pass radius to parent's init

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, SHOT_RADIUS, 3)

    def update(self, dt):
        self.position += (self.velocity * dt)