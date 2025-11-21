import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    print("Starting Asteroids with pygame version: pygame 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    current_clock = pygame.time.Clock()
    #delta time for calculating FPS
    dt = 0

    # The Group class is a container that holds and manages multiple game objects. We can organize our objects into various groups to track them more easily.
    # updatable will hold all the objects that can be updated
    # drawable will hold all the objects that can be drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    asteroid_field = AsteroidField()

    #instantiate a player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # infinite game loop
    while True:
        log_state()
        # event management for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill screen with a solid black color
        screen.fill("black")

        # draw the player
        updatable.update(dt)
        asteroids.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

            
        for draw in drawable:
            draw.draw(screen)

        # make sure to call this last
        pygame.display.flip()
        # the time that passed since last tick() call
        # convert from milliseconds to seconds
        dt = current_clock.tick(60)/1000


if __name__ == "__main__":
    main()
