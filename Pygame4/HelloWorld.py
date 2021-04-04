import pygame, sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (159, 231, 245)
DARK_BLUE = (76, 185, 212)

WIDTH = 800
HEIGHT = 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont("Berlin Sans FB", 30)
HelloWorld = FONT.render("Hello World", False, DARK_BLUE, LIGHT_BLUE)
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	WIN.blit(HelloWorld,(0, 0))
	pygame.display.update()