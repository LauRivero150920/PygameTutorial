import pygame
import os
import sys
from pygame.locals import*

WIDTH, HEIGHT = 900, 480

def SpaceInvader():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Invader")

	while True:
		WIN.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()