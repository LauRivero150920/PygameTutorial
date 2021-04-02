import pygame
import os
import sys
from random import randint
from pygame.locals import*
from Clases import SpaceShip
from Clases import Invader


WIDTH, HEIGHT = 900, 480
ENEMY_LIST = []

def Stop_Everything():
	for ENEMY in ENEMY_LIST:
		for MY_BULLET in ENEMY.SHOOTLIST:
			ENEMY.SHOOTLIST.remove(MY_BULLET)
		ENEMY.CONQUEST = True

def Load_Enemies():
	posx = 100
	for x in range (1, 5):
		ENEMY = Invader.Invader(posx, 100, 40,'Images/MarcianoA.jpg', 'Images/MarcianoB.jpg')

		ENEMY_LIST.append(ENEMY)
		posx = posx + 200

	posx = 100
	for x in range (1, 5):
		ENEMY = Invader.Invader(posx, 0, 40,'Images/Marciano2A.jpg', 'Images/Marciano2B.jpg')
		ENEMY_LIST.append(ENEMY)
		posx = posx + 200

	posx = 100
	for x in range (1, 5):
		ENEMY = Invader.Invader(posx, -100, 40,'Images/Marciano3A.jpg', 'Images/Marciano3B.jpg')
		ENEMY_LIST.append(ENEMY)
		posx = posx + 200
	
def SpaceInvader():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Invader")

	BACKGROUND = pygame.image.load(os.path.join('Images', 'Fondo.png'))

	pygame.mixer.music.load('Sounds/intro.mp3')
	pygame.mixer.music.play(3)

	FONT1 = pygame.font.SysFont("Arial", 30)
	TEXT1 = FONT1.render("GAME OVER", 0, (120,100,40))

	PLAYER = SpaceShip.SpaceShip(WIDTH, HEIGHT)
	Load_Enemies()

	IN_GAME = True
	#DEMO_BULLET = Bullet(WIDTH/2, HEIGHT - 30) 

	CLOCK = pygame.time.Clock()
	while True:
		#WIN.fill(WHITE)

		CLOCK.tick(60)

		#DEMO_BULLET.Trayectory()

		TIME = int(pygame.time.get_ticks()/1000)

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

		PLAYER.Draw(WIN)

		if len(PLAYER.SHOOTLIST) > 0:
			for x in PLAYER.SHOOTLIST:
				x.Draw(WIN)
				x.Trayectory()
				if x.RECT.top < -10:
					PLAYER.SHOOTLIST.remove(x)
				else:
					for ENEMY in ENEMY_LIST:
						if x.RECT.colliderect(ENEMY.RECT):
							ENEMY_LIST.remove(ENEMY)
							PLAYER.SHOOTLIST.remove(x)

		if len(ENEMY_LIST) > 0:
			for ENEMY in ENEMY_LIST:
				ENEMY.Behavior(TIME)
				ENEMY.Draw(WIN)

				if ENEMY.RECT.colliderect(PLAYER.RECT):
					player.Destruction()
					IN_GAME == False
					Stop_Everything()

				if len(ENEMY.SHOOTLIST) > 0:
					for x in ENEMY.SHOOTLIST:
						x.Draw(WIN)
						x.Trayectory()

						if x.RECT.colliderect(PLAYER.RECT):
							PLAYER.Destruction()
							IN_GAME == False
							Stop_Everything()

						if x.RECT.top > 900:
							ENEMY.SHOOTLIST.remove(x)
						else:
							for MY_BULLET in PLAYER.SHOOTLIST:
								if x.RECT.colliderect(MY_BULLET.RECT):
									PLAYER.SHOOTLIST.remove(MY_BULLET)
									ENEMY.SHOOTLIST.remove(x)


		if IN_GAME == False:
			pygame.mixer.music.fadeout(3000)
			WIN.blit(TEXT1,(300,300))

		pygame.display.update()

SpaceInvader() 