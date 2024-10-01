import pygame
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0, 0, 0)) # screen.fill("black")
        pygame.display.flip()
        
        # limit to 60 fps
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()