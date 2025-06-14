import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    pygame.display.set_caption("Boot Asteroids Game")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if player.overlap(asteroid):
                print("Game over!")
                sys.exit("")
            for shot in shots:
                if asteroid.overlap(shot):
                    asteroid.split()
                    shot.kill()
                    break

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
