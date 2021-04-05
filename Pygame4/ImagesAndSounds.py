import pygame, sys

pygame.init()
pygame.mixer.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (159, 231, 245)
DARK_BLUE = (76, 185, 212)

WIDTH = 800
HEIGHT = 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

image_cat = pygame.image.load("Assets/cat.png").convert()
image_cat.set_colorkey(WHITE)
image_cat_size = image_cat.get_size()

sound = pygame.mixer.Sound("Assets/sound_cat.wav")
pygame.mouse.set_visible(0)

CLOCK = pygame.time.Clock()

while True:
	CLOCK.tick(40)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	mousePosition = pygame.mouse.get_pos()
 
	x, y = mousePosition
	
	if x + image_cat_size[0] > 800:
		x = 800 - image_cat_size[0]
		sound.stop()
		sound.play()

	if y + image_cat_size[1] > 600:
		y = 600 - image_cat_size[1]
		sound.stop()
		sound.play()

	if x == 0 or y == 0:
		sound.stop()
		sound.play()

	if y + image_cat_size[1] > 600:
		y = 600 - image_cat_size[1]
		sound.stop()
		sound.play()

	WIN.fill(BLACK)

	WIN.blit(image_cat,(x, y))

	pygame.display.update()