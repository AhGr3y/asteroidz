import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Small asteroids get destroyed when shot
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Medium and Large asteroids split into smaller & faster asteroids
        split_angle = random.uniform(20, 50)
        # Vectors of the split asteroids
        vector_a = self.velocity.rotate(split_angle)
        vector_b = self.velocity.rotate(-split_angle)
        # Radius of the split asteroids
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create the split asteroids
        asteroid_a = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, split_radius)
        # Speed the asteroids up
        asteroid_a.velocity = vector_a * 1.2
        asteroid_b.velocity = vector_b * 1.2