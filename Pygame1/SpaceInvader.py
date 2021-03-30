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

		self.VEL = 20
	
	def Movement(self):
		if self.HEALTH == True:
			if self.SPSHRECT.left <= 0:
				self.SPSHRECT.left = 0
			elif self.SPSHRECT.left > 870:
				self.SPSHRECT.left = 840

	def Shoot(self, x, y):
		MY_BULLET = Bullet(x,y)
		self.SHOOTLIST.append(MY_BULLET)

	def Draw(self, WIN):
		WIN.blit(self.SPSHIMAGE, self.SPSHRECT)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.IMAGEBULLET = pygame.image.load(os.path.join('Images', 'disparoa.jpg'))
		self.BULLRECT = self.IMAGEBULLET.get_rect()
		self.BULLSPEED = 5
		self.BULLRECT.left = posx
		self.BULLRECT.top = posy
	def Trayectory(self):
		self.BULLRECT.top = self.BULLRECT.top - self.BULLSPEED
	def Draw(self, surface):
		surface.blit(self.IMAGEBULLET, self.BULLRECT)

def SpaceInvader():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Invader")

	BACKGROUND = pygame.image.load(os.path.join('Images', 'Fondo.png'))
	PLAYER = SpaceShip()

	IN_GAME = True
	DEMO_BULLET = Bullet(WIDTH/2, HEIGHT - 30) 
	while True:
		#WIN.fill(WHITE)

		PLAYER.Movement()

		DEMO_BULLET.Trayectory()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if IN_GAME == True:
				if event.type == pygame.KEYDOWN:
					if event.key == K_LEFT:
						PLAYER.SPSHRECT.left -= PLAYER.VEL
					elif event.key == K_RIGHT:
						PLAYER.SPSHRECT.right += PLAYER.VEL
					elif event.key == K_s:
						x,y = PLAYER.SPSHRECT.center
						PLAYER.Shoot(x,y)

		WIN.blit(BACKGROUND, (0,0))

		PLAYER.Draw(WIN)

		if len(PLAYER.SHOOTLIST) > 0:
			for x in PLAYER.SHOOTLIST:
				x.Draw(WIN)
				x.Trayectory()
				if x.BULLRECT.top < -10:
					PLAYER.SHOOTLIST.remove(x)

		pygame.display.update()

SpaceInvader() 