from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (252, 0, 0), self.position, self.radius, width = 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position[0], self.position[1], smaller_radius)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], smaller_radius)

            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)

