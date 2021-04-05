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
HelloWorld_size = HelloWorld.get_size()

x, y = 0, 0
direction_x = 1
direction_y = 1

CLOCK = pygame.time.Clock()

while True:
	CLOCK.tick(40)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	WIN.fill(BLACK)

	WIN.blit(HelloWorld,(x, y))

	x += 5 * direction_x
	y += 5 * direction_y
	if x + HelloWorld_size[0] > 800 or x <= 0:
		direction_x *= -1
	if y + HelloWorld_size[1] > 600 or y <= 0:
		direction_y *= -1

	pygame.display.update()