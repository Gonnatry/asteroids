import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2
 
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill((0,0,0))
            for up in updatable:
                up.update(dt)
            for ast in asteroids:
                 checking = ast.collision(player)
                 if checking == True:
                      raise SystemExit("Game over!")
            for draw in drawable:
                 draw.draw(screen)    

            pygame.display.flip()
            clock_out = clock.tick(60)
            dt = clock_out/1000




if __name__ == "__main__":
    main()

