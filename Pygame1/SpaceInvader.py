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

		self.RECT = self.SPSHIMAGE.get_rect()
		self.RECT.centerx = WIDTH/2
		self.RECT.centery = HEIGHT - 30

		self.SHOOTLIST = []
		self.HEALTH = True 

		self.VEL = 20

	def MovementRight(self):
		self.RECT.right += self.VEL
		self.__movement()

	def MovementLeft(self):
		self.RECT.left -= self.VEL
		self.__movement()

	def __movement(self):
		if self.HEALTH == True:
			if self.RECT.left <= 0:
				self.RECT.left = 0
			elif self.RECT.left > 870:
				self.RECT.left = 840

	def Shoot(self, x, y):
		MY_BULLET = Bullet(x,y)
		self.SHOOTLIST.append(MY_BULLET)

	def Draw(self, WIN):
		WIN.blit(self.SPSHIMAGE, self.RECT)

# Clase para disparar
class Bullet(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.IMAGEBULLET = pygame.image.load(os.path.join('Images', 'disparoa.jpg'))
		self.RECT = self.IMAGEBULLET.get_rect()

		self.BULLSPEED = 5

		self.RECT.left = posx
		self.RECT.top = posy

	def Trayectory(self):
		self.RECT.top = self.RECT.top - self.BULLSPEED

	def Draw(self, surface):
		surface.blit(self.IMAGEBULLET, self.RECT)

# Clase para invasor
class Invader(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.INVADERIMAGE_A = pygame.image.load(os.path.join('Images', 'MarcianoA.jpg'))
		self.INVADERIMAGE_B = pygame.image.load(os.path.join('Images', 'MarcianoB.jpg'))
		self.IMAGELIST = [self.INVADERIMAGE_A, self.INVADERIMAGE_B]
		self.POSIMAGES = 0

		self.IMAGEINVADER = self.IMAGELIST[self.POSIMAGES]
		self.RECT = self.IMAGEINVADER.get_rect()

		self.BULLSPEED = 5
		self.VEL = 20

		self.BULLETLIST = []

		self.RECT.left = posx
		self.RECT.top = posy

		self.TIMECHANGE = 1 

	def Draw(self, surface):
		self.IMAGEINVADER = self.IMAGELIST[self.POSIMAGES]
		surface.blit(self.IMAGEINVADER, self.RECT)

	def Behavior(self,time):
		if self.TIMECHANGE == time:
			self.POSIMAGES += 1
			self.TIMECHANGE += 1

			if self.POSIMAGES > len(self.IMAGELIST) - 1:
				self.POSIMAGES = 0

def SpaceInvader():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Invader")

	BACKGROUND = pygame.image.load(os.path.join('Images', 'Fondo.png'))
	PLAYER = SpaceShip()
	ENEMY = Invader(100,100)

	IN_GAME = True
	DEMO_BULLET = Bullet(WIDTH/2, HEIGHT - 30) 

	CLOCK = pygame.time.Clock()
	while True:
		#WIN.fill(WHITE)

		CLOCK.tick(60)

		DEMO_BULLET.Trayectory()

		TIME = pygame.time.get_ticks()/1000

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if IN_GAME == True:
				if event.type == pygame.KEYDOWN:
					if event.key == K_LEFT:
						PLAYER.MovementLeft()
					elif event.key == K_RIGHT:
						PLAYER.MovementRight()
					elif event.key == K_s:
						x,y = PLAYER.RECT.center
						PLAYER.Shoot(x,y)

		WIN.blit(BACKGROUND, (0,0))

		ENEMY.Behavior(TIME)

		PLAYER.Draw(WIN)
		ENEMY.Draw(WIN)

		if len(PLAYER.SHOOTLIST) > 0:
			for x in PLAYER.SHOOTLIST:
				x.Draw(WIN)
				x.Trayectory()
				if x.RECT.top < -10:
					PLAYER.SHOOTLIST.remove(x)

		pygame.display.update()

SpaceInvader() 