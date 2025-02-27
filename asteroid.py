from __future__ import annotations
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white",
                           center=self.position, radius=self.radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_asteroid = Asteroid(
            *self.position, self.radius - ASTEROID_MIN_RADIUS)
        first_asteroid.velocity = self.velocity.rotate(random_angle) * 1.2
        second_asteroid = Asteroid(
            *self.position, self.radius - ASTEROID_MIN_RADIUS)
        second_asteroid.velocity = self.velocity.rotate(-random_angle) * 1.2

    def update(self, dt: int):
        self.position += self.velocity * dt
