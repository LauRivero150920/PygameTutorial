import pygame

import game
import colors

class Bullet:
    def __init__(self, position, direction):
        self.pos = pygame.Vector2(position)
        self.vel = 10 * pygame.Vector2(direction)
        
        self.on_screen = True
        
    def tick(self):
        self.pos += self.vel
        
        if not (0 < self.pos.x < game.width and 0 < self.pos.y < game.height):
            self.on_screen = False
        
    def draw(self, screen):
        pygame.draw.circle(screen, colors.red, self.pos, 5)
        pygame.draw.circle(screen, colors.yellow, self.pos, 3)
