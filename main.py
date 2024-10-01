import pygame
from constants import * 
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for upd in updatables:
            upd.update(dt)
        
        screen.fill("black")
            
        for draw in drawables:
            draw.draw(screen)

        pygame.display.flip()
        
        # limit to 60 fps
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()