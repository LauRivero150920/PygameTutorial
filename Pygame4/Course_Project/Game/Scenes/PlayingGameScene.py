import pygame
from Scenes import Scene
class PlayingGameScene(Scene):
	def __init__(self, game):
		super(PlayingGameScene, self).__init__(game)
	
	def render(self):
		super(PlayingGameScene, self).render()

		game = self.getGame()
		
		balls = game.getBalls()

		for ball in balls:
			for ball2 in balls:
				if ball != ball2 and ball.intersects(ball2):
					ball.changeDirection(ball2)

			for brick in game.getLevel().getBricks():
				if not brick.isDestroyed() and ball.intersects(brick):
					brick.hit()
					ball.changeDirection(brick)
					break

			ball.updatePosition()

			game.WIN.blit(ball.getSprite(), ball.getPosition())

		for brick in game.getLevel().getBricks():
			if not brick.isDestroyed():
				game.WIN.blit(brick.getSprite(), brick.getPosition())
	
	def handleEvents(self, events):
		super(PlayingGameScene, self).handleEvents(events)

		for event in events:
			if event.type == pygame.QUIT:
				exit()