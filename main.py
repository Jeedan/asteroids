import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    print("Starting Asteroids with pygame version: pygame 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
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
