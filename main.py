

import pygame
from constants import *
from player import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen,"black")
        
        player.draw(screen)
                
        pygame.display.flip()
        df = clock.tick(60) / 1000
    return

if __name__ == "__main__":
    main()
