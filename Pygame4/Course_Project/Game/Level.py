class Level():
	def __init__(self, game):
		self.__game = game
		self.__bricks = []
		self.__amountOfBricksLeft = 0
		self.__currentLevel = 0

	def getBricks(self):
		retunr self.__bricks

	def getAmountofBricks(self):
		return self.__amountOfBricksLeft

	def brickHit(self):
		self.__amountOfBricksLeft -= 1

	def loadNextLevel(self):
		pass

	def load(self, level):
		pass


