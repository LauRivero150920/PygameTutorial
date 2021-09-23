import pygame
import random
import os

import utilities
import player
import bullet
import asteroid

# General game properties
pygame.display.set_caption('Space game')
width, height = 800, 600
fps = 60
dt = 1 / fps

mouse_released = True

bg_offset = 0

# Loading images

img_bg = utilities.load_image('Background.png')
img_bg = pygame.transform.scale(img_bg, ((600 * 256) // 64, 600))

img_player = utilities.load_image('Spaceship.png')
img_player = pygame.transform.scale(img_player, ((100 * 29) // 42, 100))

img_asteroids = []
img_asteroids.append(utilities.load_image('Asteroid_01.png'))
img_asteroids.append(utilities.load_image('Asteroid_02.png'))
img_asteroids.append(utilities.load_image('Asteroid_03.png'))
img_asteroids.append(utilities.load_image('Asteroid_04.png'))

ss_explosions = utilities.load_image('Explosion.png')
ss_explosions = pygame.transform.scale2x(ss_explosions)

frame_size = (64, 64)
anim_explosion = [pygame.Surface(frame_size).convert_alpha()] * 8

for i in range(8):
    frame = pygame.Rect(64 * i, 0, 64, 64)
    anim_explosion[i] = ss_explosions.subsurface(frame)

# Loading sounds

snd_damage = utilities.load_sound('Damage.wav')
snd_explosion = utilities.load_sound('Explosion.wav')
snd_lasershot = utilities.load_sound('Lasershot.wav')

utilities.set_music('Background.mp3')

# Text and fonts

font = pygame.font.SysFont('arial', 40)


# Player
player = player.Player(
        100,
        (height - img_player.get_width()) // 2,
        img_player.get_width(),
        img_player.get_height(),
        img_player)
        
bullets = []

# Asteroids
spawn_cooldown = random.randint(5000, 10000)
last_spawn = pygame.time.get_ticks()

asteroids = []

# Functions

def draw_background(screen):
    if img_bg.get_width() + bg_offset > width:
        screen.blit(img_bg, (bg_offset, 0))
    else:
        screen.blit(img_bg, (bg_offset, 0))
        screen.blit(img_bg, (bg_offset + img_bg.get_width(), 0))
        
def spawn_asteroid(type):
    new_asteroid = asteroid.Asteroid(
            width,
            random.randint(0, height - img_asteroids[type].get_height()),
            img_asteroids[type].get_width(),
            img_asteroids[type].get_height(),
            img_asteroids[type])
            
    asteroids.append(new_asteroid)
    
def tick():
    # Tick background
    global bg_offset
    bg_offset -= 2

    if bg_offset <= -img_bg.get_width():
        bg_offset = 0
    
    # Tick objects
    for bullet in bullets:
        bullet.tick()
        
        if not bullet.on_screen:
            bullets.remove(bullet)
            
    player.tick()
            
    for asteroid in asteroids:
        asteroid.tick()
        
        if not asteroid.on_screen:
            asteroids.remove(asteroid)
            continue
        
        if asteroid.is_destroyed:
            continue
        
        for bullet in bullets:
            if asteroid.hitbox.collidepoint(bullet.pos):
                asteroid.destroy()
        
        if asteroid.hitbox.colliderect(player.hitbox):
            asteroid.destroy()
            player.take_damage()
            
    # Spawn asteroids
    global spawn_cooldown, last_spawn
    
    if pygame.time.get_ticks() - last_spawn > spawn_cooldown:
        spawn_cooldown = random.randint(100, 2500)
        last_spawn = pygame.time.get_ticks()
        spawn_asteroid(random.randint(0, 3))
        
def draw(screen):
    draw_background(screen)
    
    for bullet in bullets:
        bullet.draw(screen)
        
    player.draw(screen)
        
    for asteroid in asteroids:
        asteroid.draw(screen)
