import pygame
import constants
from logger import log_state

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def main():
    print("Starting Asteroids with pygame version: pygame 2.6.1")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    
    # infinite game loop
    while True:
        log_state()
        # event management for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill screen with a solid black color
        screen.fill("black")
        #make sure to call this last
        pygame.display.flip()


if __name__ == "__main__":
    main()
