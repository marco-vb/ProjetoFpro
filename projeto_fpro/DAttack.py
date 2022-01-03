import pygame, os
from constants import *
from images import *
from player import Player

WINDOW = pygame.display.set_mode((WID, HEI))
CLOCK = pygame.time.Clock()


class Game:
    def __init__(self):
        player_sprite = Player((WID // 2, int(0.9 * HEI)))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.sprite.bullets.draw(WINDOW)
        self.player.draw(WINDOW)


def main():
    running = True
    game = Game()

    while running:

        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
    
        WINDOW.blit(SPACE, (0, 0))
        game.run()
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()