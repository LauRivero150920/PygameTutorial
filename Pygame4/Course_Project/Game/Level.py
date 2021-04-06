import os
import fileinput
from Bricks import *
import pygame
from Shared import GameConstants
class Level():
	def __init__(self, game):
		self.__game = game
		self.__bricks = []
		self.__amountOfBricksLeft = 0
		self.__currentLevel = 0

	def getBricks(self):
		return self.__bricks

	def getAmountofBricks(self):
		return self.__amountOfBricksLeft

	def brickHit(self):
		self.__amountOfBricksLeft -= 1

	def loadNextLevel(self):
		pass

	def load(self, level):
		self.__currentLevel = level
		self.__bricks = []

		x, y = 0, 0

		for line in fileinput.input(os.path.join("Assets", "Levels", "level" + str(level) + ".dat")):
			for currentBrick in line:
				if currentBrick == "1":
					brick = Brick((x, y), pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
					self.__bricks.append(brick);
					self.__amountOfBricksLeft += 1
				elif currentBrick == "2":
					brick = SpeedBrick((x, y), pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
					self.__bricks.append(brick);
					self.__amountOfBricksLeft += 1
				elif currentBrick == "3":
					brick = LifeBrick((x, y), pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
					self.__bricks.append(brick);
					self.__amountOfBricksLeft += 1

				x += GameConstants.BRICK_SIZE[0]

			x = 0
			y += GameConstants.BRICK_SIZE[1]