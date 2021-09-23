import pygame
import random

import game

dt = 35

class Asteroid:
    def __init__(self, x, y, width, height, sprite):
        self.dim = pygame.Vector2(width, height)
        self.hitbox = pygame.Rect(x, y, width, height)
        
        self.sprite = sprite
        
        self.pos = pygame.Vector2(x, y)
        self.vel = random.randint(1, 15)
        
        self.is_destroyed = False
        self.destroy_time = pygame.time.get_ticks()
        self.on_screen = True
                       
    def destroy(self):
        self.is_destroyed = True
        self.destroy_time = pygame.time.get_ticks()
        game.snd_explosion.play()
        
    def tick(self):
        self.pos.x -= self.vel
        
        if self.pos.x < 0:
            self.on_screen = False
            
        self.hitbox.x = self.pos.x
        
    def draw(self, screen):
        if self.is_destroyed:
            current_time = pygame.time.get_ticks()
            
            if current_time - self.destroy_time < 1 * dt:
                screen.blit(game.anim_explosion[0], (self.pos.x, self.pos.y))
            
            elif current_time - self.destroy_time < 2 * dt:
                screen.blit(game.anim_explosion[1], (self.pos.x, self.pos.y))
            
            elif current_time - self.destroy_time < 3 * dt:
                screen.blit(game.anim_explosion[2], (self.pos.x, self.pos.y))
                
            elif current_time - self.destroy_time < 4 * dt:
                screen.blit(game.anim_explosion[3], (self.pos.x, self.pos.y))
                
            elif current_time - self.destroy_time < 5 * dt:
                screen.blit(game.anim_explosion[4], (self.pos.x, self.pos.y))
                
            elif current_time - self.destroy_time < 5 * dt:
                screen.blit(game.anim_explosion[5], (self.pos.x, self.pos.y))
                
            elif current_time - self.destroy_time < 8 * dt:
                screen.blit(game.anim_explosion[6], (self.pos.x, self.pos.y))
                
            elif current_time - self.destroy_time < 9 * dt:
                screen.blit(game.anim_explosion[7], (self.pos.x, self.pos.y))
            
            elif current_time - self.destroy_time < 10 * dt:
                self.on_screen = False
                    
        else:
            screen.blit(self.sprite, (self.pos.x, self.pos.y))
