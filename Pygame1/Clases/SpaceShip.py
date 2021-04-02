import pygame
from Clases import Bullet
import os

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self, WIDTH, HEIGHT):
		pygame.sprite.Sprite.__init__(self)
		self.SPSHIMAGE = pygame.image.load(os.path.join('Images', 'nave.jpg'))
		self.EXPIMAGE = pygame.image.load(os.path.join('Images', 'explosion.jpg'))
		
		self.RECT = self.SPSHIMAGE.get_rect()
		self.RECT.centerx = WIDTH/2
		self.RECT.centery = HEIGHT - 30

		self.SHOOTLIST = []
		self.HEALTH = True 

		self.VEL = 20

		self.SOUND_SHOOT = pygame.mixer.Sound("Sounds/shoot.wav")
		self.SOUND_EXP = pygame.mixer.Sound("Sounds/gameover.wav")


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
		MY_BULLET = Bullet.Bullet(x,y,"Images/disparoa.jpg",True)
		self.SHOOTLIST.append(MY_BULLET)
		self.SOUND_SHOOT.play()

	def Destruction(self):
		self.SOUND_EXP.play()
		self.HEALTH = False
		self.VEL = 0
		self.SPSHIMAGE = self.EXPIMAGE

	def Draw(self, WIN):
		WIN.blit(self.SPSHIMAGE, self.RECT)