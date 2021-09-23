import pygame

import game
import colors
import bullet

ace = 500

class Player:
    def __init__(self, x, y, width, height, sprite):
        self.dim = pygame.Vector2(width, height)
        self.hitbox = pygame.Rect(x, y, width, height)
        
        self.sprite = sprite
        self.health = 5
        
        self.ace = pygame.Vector2(0, 0)
        self.vel = pygame.Vector2(0, 0)
        self.pos = pygame.Vector2(x, y)
        
        self.center = self.pos + self.dim / 2
        self.crosshair = pygame.Vector2()
        
        self.last_shot = pygame.time.get_ticks()
        
    def take_damage(self):
        self.health -= 1
        game.snd_damage.stop()
        game.snd_damage.play()
        
    def tick(self):
        keys = pygame.key.get_pressed()
        
        if self.ace.magnitude() < 1000:
            if keys[pygame.K_a]:
                self.ace.x += -ace
                
            if keys[pygame.K_d]:
                self.ace.x += ace
                
            if keys[pygame.K_w]:
                self.ace.y += -ace
                
            if keys[pygame.K_s]:
                self.ace.y += ace
            
        self.vel += self.ace * game.dt
        self.pos += self.vel * game.dt
        self.ace *= 0.5
        
        self.center = self.pos + self.dim / 2
        
        self.hitbox.x = self.pos.x
        self.hitbox.y = self.pos.y
        
        self.crosshair = pygame.mouse.get_pos() - self.center
        self.crosshair.normalize_ip()
        
        clicks = pygame.mouse.get_pressed()
        
        if clicks[0] and game.mouse_released:
            game.mouse_released = False
            new_shot = pygame.time.get_ticks()
            
            if pygame.time.get_ticks() - self.last_shot > 100:
                self.last_shot = pygame.time.get_ticks()
            
                new_bullet = bullet.Bullet(
                        self.center + 65 * self.crosshair,
                        self.crosshair)
                        
                game.bullets.append(new_bullet)
                game.snd_lasershot.stop()
                game.snd_lasershot.play()
        
    def draw(self, screen):
        screen.blit(self.sprite, (self.pos.x, self.pos.y))
        
        pygame.draw.circle(
                screen,
                colors.red,
                65 * self.crosshair + self.center,
                5)
                
        pygame.draw.circle(
                screen,
                colors.yellow,
                65 * self.crosshair + self.center,
                3)
                
        text = game.font.render(f'Health: {self.health}', True, colors.white)
        screen.blit(text, (10, 10))
