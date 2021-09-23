import pygame

pygame.init()

import game

pygame.display.set_caption('Asteroids')
screen = pygame.display.set_mode((game.width, game.height))
clock = pygame.time.Clock()
    
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.MOUSEBUTTONUP:
                game.mouse_released = True
        
        game.tick()
        game.draw(screen)
        pygame.display.update()
        clock.tick(game.fps)

if __name__ == '__main__':
    main()
