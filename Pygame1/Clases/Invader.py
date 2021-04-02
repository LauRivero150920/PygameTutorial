import pygame
from Clases import Bullet
from random import randint

class Invader(pygame.sprite.Sprite):
	def __init__(self, posx, posy, distance, image1, image2):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.INVADERIMAGE_A = pygame.image.load(image1)
		self.INVADERIMAGE_B = pygame.image.load(image2)
		self.IMAGELIST = [self.INVADERIMAGE_A, self.INVADERIMAGE_B]
		self.POSIMAGES = 0

		self.IMAGEINVADER = self.IMAGELIST[self.POSIMAGES]
		self.RECT = self.IMAGEINVADER.get_rect()

		self.VEL = 20

		self.SHOOTLIST = []

		self.RECT.left = posx
		self.RECT.top = posy

		self.SHOOTRANGE = 5
		self.TIMECHANGE = 1 

		self.CONQUEST = False

		self.RIGHT = True
		self.CONT = 0
		self.MAXDOWN = self.RECT.top + 40

		self.LIM_RIGHT = posx + distance
		self.LIM_LEFT = posx + distance

	def Draw(self, surface):
		self.IMAGEINVADER = self.IMAGELIST[self.POSIMAGES]
		surface.blit(self.IMAGEINVADER, self.RECT)

	def Behavior(self,time):
		if self.CONQUEST == False:
			self.__Movement()
			self.__Attack()
		
			if self.TIMECHANGE == time:
				self.POSIMAGES += 1
				self.TIMECHANGE += 1

				if self.POSIMAGES > len(self.IMAGELIST) - 1:
					surfaceelf.POSIMAGES = 0
					
	def __Movement(self):
		if self.CONT < 3:
			self.__LateralMovement()
		else:
			self.__Down()

	def __LateralMovement(self):
		if self.RIGHT == True:
			self.RECT.left = self.RECT.left + self.VEL
			if self.RECT.left > self.LIM_RIGHT:
				self.RIGHT = False

				self.CONT += 1

		else:
			self.RECT.left = self.RECT.left - self.VEL
			if self.RECT.left < self.LIM_LEFT:
				self.RIGHT = True

	def __Down(self):
 		if self.MAXDOWN == self.RECT.top:
 			self.CONT = 0
 			self.MAXDOWN = self.RECT.top + 40
 		else:
 			self.RECT.top += 1

	def __Attack(self):
		if (randint(0,100) < self.SHOOTRANGE):
			self.__Shoot()

	def __Shoot(self):
		x,y = self.RECT.center
		MY_BULLET = Bullet.Bullet(x,y,"Images/disparob.jpg",False)
		self.SHOOTLIST.append(MY_BULLET)