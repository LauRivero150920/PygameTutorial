import pygame
from Assets import *
from Bricks import *
from Scenes import *
from Level import *
from Pad import *
from Ball import *
from HighScore import *
from Shared import GameConstants

class Breakout:
	def __init__(self):
		self.__lives = 5
		self.__score = 0

		self.__level = Level(self)
		self.__level.load(0)

		self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2,
						 GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]),
						 pygame.image.load(GameConstants.SPRITE_PAD)
						 )		
		self.__balls = [
			Ball((400, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)
		]

		pygame.init()
		pygame.mixer.init()
		pygame.display.set_caption("Game Pew Pew")

		self.__CLOCK = pygame.time.Clock()

		self.WIN = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

		pygame.mouse.set_visible(0)

		self.__scenes = (
			PlayingGameScene(self),
			GameOverScene(self),
			HighScoreScene(self),
			MainMenuScene(self)
		)

		self.__currentScene = 0

		self.__sounds = ()

	def start(self):
		while True:
			self.__CLOCK.tick(100)

			self.WIN.fill((GameConstants.BLACK))

			currentScene = self.__scenes[self.__currentScene]
			currentScene.handleEvents(pygame.event.get())
			currentScene.render()

			pygame.display.update()

	def changeScene(self, scene):
		self.__currentScene = scene

	def getLevel(self):
		return self.__level

	def getScore(self):
		return self.__score

	def increaseScore(self, score):
		self.__score += score

	def getLives(self):
		return self.__lives

	def getBalls(self):
		return self.__balls

	def getPad(self):
		return self.__pad

	def playSound(self, soundClip):
		sound = self.__sounds[soundClip]

		sound.stop()
		sound.play()

	def reduceLives(self):
		self.__lives -= 1

	def increaseLives(self):
		self.__lives += 1
		
	def reset(self):
		pass

Breakout().start()