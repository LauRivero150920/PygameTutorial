import pygame
from Scenes import Scene
class PlayingGameScene(Scene):
	def __init__(self, game):
		super(PlayingGameScene, self).__init__(game)
	
	def render(self):
		super(PlayingGameScene, self).render()

		game = self.getGame()

		for ball in game.getBalls():
			ball.updatePosition()

			game.WIN.blit(ball.getSprite(), ball.getPosition())

		for brick in game.getLevel().getBricks():
			game.WIN.blit(brick.getSprite(), brick.getPosition())
	def handleEvents(self, events):
		super(PlayingGameScene, self).handleEvents(events)

		for event in events:
			if event.type == pygame.QUIT:
				exit()