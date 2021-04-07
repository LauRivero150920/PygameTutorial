import pygame
from Scenes import Scene
from Shared import *
class GameOverScene(Scene):
	def __init__(self, game):
		super(GameOverScene, self).__init__(game)

	def render(self):
		super(GameOverScene, self).render()

		self.clearText()
		self.addText("Press F1 to restart the game", 400, 300, size = 30)
	
	def handleEvents(self, events):
		super(GameOverScene, self).handleEvents(events)

		for event in events:
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F1:
					self.getGame().reset()
					self.getGame().changeScene(GameConstants.PLAYING_SCENE)