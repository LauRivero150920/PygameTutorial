from Shared import *

 class Ball(GameObject):
 	def __init__(self, position, sprite, game):
 		self.__game = game
 		self.__speed = 3
 		self.__increment = [2, 2]
 		self.__direction = [2, 2]
 		self.__inMotion = 0

 		super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

 	def setSpeed(self, newSpeed):
 		self.__speed = newSpeed

 	def resetSpeed(self):
 		self.__setSpeed(3)

 	def getSpeed(self):
 		return self.__speed

 	def isInMotion(self):
 		return self.__inMotion

 	def setMotion(self, isMoving):
 		self.__inMotion = isMoving
 		self.resetSpeed()

 	def chamgeDirection(self, gameObject):
 		pass

 	def updatePosition(self):
 		pass

 	def isBallDead(self):
 		pass