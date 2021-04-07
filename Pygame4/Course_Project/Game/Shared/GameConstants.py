import os
class GameConstants:
	BRICK_SIZE = (100, 40)

	WIDTH = 800
	HEIGHT = 600
	SCREEN_SIZE = (WIDTH, HEIGHT)

	BALL_SIZE = [16,16]

	PAD_SIZE = [139, 13]

	# Colors
	BLACK = (0, 0 , 0)
	WHITE = (255, 255, 255)

	SPRITE_BALL = os.path.join("Assets", "Ball.png")

	SPRITE_BRICK = os.path.join("Assets", "standard.png")
	SPRITE_SPEEDBRICK = os.path.join("Assets", "speed.png")
	SPRITE_LIFEBRICK = os.path.join("Assets", "life.png")

	SPRITE_PAD = os.path.join("Assets", "pad.png")

	PLAYING_SCENE = 0
	GAMEOVER_SCENE = 1
	HIGHSCORE_SCENE = 2
	MENU_SCENE = 3