from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass radius to parent's init
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, (218, 165, 32), self.position, self.radius, 3)

    def update(self, dt):
        self.position += (self.velocity * dt)