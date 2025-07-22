

from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (252, 252, 252), self.position, radius=SHOT_RADIUS, width = 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

