import pygame
from Scenes import Scene
from Shared import *

class PlayingGameScene(Scene):
	def __init__(self, game):
		super(PlayingGameScene, self).__init__(game)
	
	def render(self):
		super(PlayingGameScene, self).render()

		game = self.getGame()

		pad = game.getPad()
		
		balls = game.getBalls()

		for ball in balls:
			for ball2 in balls:
				if ball != ball2 and ball.intersects(ball2):
					ball.changeDirection(ball2)

			for brick in game.getLevel().getBricks():
				if not brick.isDestroyed() and ball.intersects(brick):
					brick.hit()
					game.increaseScore(brick.getHitPoints())
					ball.changeDirection(brick)
					break
			if ball.intersects(pad):
				ball.changeDirection(pad)

			ball.updatePosition()

			game.WIN.blit(ball.getSprite(), ball.getPosition())

		for brick in game.getLevel().getBricks():
			if not brick.isDestroyed():
				game.WIN.blit(brick.getSprite(), brick.getPosition())
		
		pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
		game.WIN.blit(pad.getSprite(), pad.getPosition())
		
		self.clearText()

		self.addText("Score: " + str(game.getScore()), x = 0, y = GameConstants.HEIGHT - 70, size = 30)
		self.addText("Lives: " + str(game.getLives()), x = 0, y = GameConstants.HEIGHT - 40, size = 30)
	
	def handleEvents(self, events):
		super(PlayingGameScene, self).handleEvents(events)

		for event in events:
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for ball in self.getGame().getBalls():
					ball.setMotion(1)
