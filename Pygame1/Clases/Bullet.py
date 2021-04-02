import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self, posx, posy, route, character):
		pygame.sprite.Sprite.__init__(self)
		self.IMAGEBULLET = pygame.image.load(route)
		self.RECT = self.IMAGEBULLET.get_rect()

		self.BULLSPEED = 5

		self.RECT.left = posx
		self.RECT.top = posy

		self.CHARSHOOT = character
	def Trayectory(self):
		if self.CHARSHOOT == True:
			self.RECT.top = self.RECT.top - self.BULLSPEED
		else:
			self.RECT.top = self.RECT.top + self.BULLSPEED

	def Draw(self, surface):
		surface.blit(self.IMAGEBULLET, self.RECT)