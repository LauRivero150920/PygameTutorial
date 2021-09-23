import pygame
import os

pygame.display.init()
pygame.display.set_mode()

pygame.mixer.init()

img_path = os.path.join('Assets', 'Images')
snd_path = os.path.join('Assets', 'Sounds')

def load_image(filename):
    return pygame.image.load(os.path.join(img_path, filename)).convert_alpha()
    
def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(snd_path, filename))

def set_music(filename):
    pygame.mixer.music.load(os.path.join(snd_path, filename))
    pygame.mixer.music.play(-1)
