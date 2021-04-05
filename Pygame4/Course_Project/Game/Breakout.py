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

		self.__pad = Pad([0,0], 0)
		self.__balls = [Ball((0,0), 0, self)]

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
		pass

	def getLevel(self):
		pass

	def getScore(self):
		pass

	def increaseScore(self, score):
		pass

	def getLives(self):
		pass

	def getBalls(self):
		pass

	def getPad(self):
		pass

	def playSound(self, soundClip):
		pass

	def reduceLives(self):
		pass

	def increaseLives(self):
		pass
		
	def reset(self):
		pass

Breakout().start()