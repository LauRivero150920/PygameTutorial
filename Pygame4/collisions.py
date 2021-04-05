import pygame, sys
from GameObject import GameObject

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

#Load resoruces
image_cat = pygame.image.load("Assets/cat.png").convert()
image_cat.set_colorkey(WHITE)
BERLIN_FONT = pygame.font.SysFont("Berlin Sans FB", 40)
intersect_text = BERLIN_FONT.render("Intersecting", 1, DARK_BLUE, LIGHT_BLUE)
sound = pygame.mixer.Sound("Assets/sound_cat.wav")
pygame.mouse.set_visible(0)

#Prepare logo
image_cat_size = image_cat.get_size()
image_cat.fill(BLACK, None, pygame.BLEND_RGBA_MAX)

CLOCK = pygame.time.Clock()

x, y = 0, 0

def playSound():
	sound.stop()
	sound.play()

rectangle = GameObject(100, 100, 400, 400)
logo = GameObject(0, 0, image_cat_size[0], image_cat_size[1])

while True:
	CLOCK.tick(40)

	WIN.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	mouse_position = pygame.mouse.get_pos()

	x = mouse_position[0]
	y = mouse_position[1]

	logo.setPosition(x, y)

	if logo.intersects(rectangle):
		WIN.blit(intersect_text, (10, 10))

	if x + image_cat_size[0] > 800:
		x = 800 - image_cat_size[0]

	if y + image_cat_size[1] > 600:
		y = 600 - image_cat_size[1]

	if x <= 0:
		x = 0

	if y <= 0:
		y = 0

	pygame.draw.rect(WIN, WHITE, (100, 100, 400, 400), 1)
	
	WIN.blit(image_cat, (x, y))

	pygame.display.update()