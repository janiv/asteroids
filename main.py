import pygame
from constants import *

def main():
    pygame.init()
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    running = True
    while(running):
        screen.fill(BLACK)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()
