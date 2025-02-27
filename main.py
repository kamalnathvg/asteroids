from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: int = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot, drawable, updatable)
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT/2)
    asteroid_field: AsteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for asteroid in asteroids:

            for s in shot:
                if asteroid.is_collided(s):
                    asteroid.split()
                    s.kill()

            if asteroid.is_collided(player):
                print("Game Over!")
                print(f"collided with asteroid at {
                      asteroid.position}, with radius {asteroid.radius}")
                print(f"player position {player.position}")
                return

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60.0) / 1000


if __name__ == "__main__":
    main()
