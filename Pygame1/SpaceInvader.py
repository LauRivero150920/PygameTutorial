import pygame
import os
import sys
from pygame.locals import*

WIDTH, HEIGHT = 900, 480

# Clase para las naves 
class SpaceShip(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.SPSHIMAGE = pygame.image.load(os.path.join('Images', 'nave.jpg'))

		self.SPSHRECT = self.SPSHIMAGE.get_rect()
		self.SPSHRECT.centerx = WIDTH/2
		self.SPSHRECT.centery = HEIGHT - 30

		self.SHOOTLIST = []
		self.HEALTH = True 

	def Shoot(self):
		self

	def Draw(self, WIN):
		WIN.blit(self.SPSHIMAGE, self.SPSHRECT)

def SpaceInvader():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Invader")

	BACKGROUND = pygame.image.load(os.path.join('Images', 'Fondo.png'))
	PLAYER = SpaceShip()
	while True:
		#WIN.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		WIN.blit(BACKGROUND, (0,0))
		PLAYER.Draw(WIN)
		pygame.display.update()

SpaceInvader()