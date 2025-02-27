from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED
from circleshape import CircleShape
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius
        )

    def update(self, dt: int):
        self.position += self.velocity * dt
