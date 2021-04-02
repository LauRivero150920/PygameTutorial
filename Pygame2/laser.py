import pygame, sys, random
pygame.init()
pygame.font.init()

# Fonts
FONT1 = pygame.font.SysFont("Arial", 30)

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

WIDTH = 900
HEIGHT = 600

#pygame.mouse.set_visible(0)

class Meteorite(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/meteor.png").convert()
		self.image.set_colorkey(BLACK)
		# Posicionar Sprite
		self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/player.png").convert()
		self.image.set_colorkey(BLACK)
		# Posicionar Sprite
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0

	def change_speed(self,x):
	 	self.speed_x += x

	def update(self):
		self.rect.x += self.speed_x
		PLAYER.rect.y = 520


class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/laser.png").convert()
		self.image.set_colorkey(BLACK)
		# Posicionar Sprite
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y -= 5

# Crear ventana
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tutorial Pygame2: Sprites 2.0")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

DONE = False

SCORE = 0

ALL_SPRITE_LIST = pygame.sprite.Group()
METEOR_LIST = pygame.sprite.Group()
LASER_LIST = pygame.sprite.Group()

for i in range(50):
	METEOR = Meteorite()
	METEOR.rect.x = random.randrange(880)
	METEOR.rect.y = random.randrange(450)

	METEOR_LIST.add(METEOR)
	ALL_SPRITE_LIST.add(METEOR)

PLAYER = Player()
ALL_SPRITE_LIST.add(PLAYER)

while not DONE:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				PLAYER.change_speed(-3)
			if event.key == pygame.K_RIGHT:
				PLAYER.change_speed(3)
			if event.key == pygame.K_SPACE:
				LASER = Laser()
				LASER.rect.x = PLAYER.rect.x + 45
				LASER.rect.y = PLAYER.rect.y - 20
				LASER_LIST.add(LASER)
				ALL_SPRITE_LIST.add(LASER)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				PLAYER.change_speed(3)
			if event.key == pygame.K_RIGHT:
				PLAYER.change_speed(-3)

	ALL_SPRITE_LIST.update()

	for LASER in LASER_LIST:
		METEOR_HIT_LIST = pygame.sprite.spritecollide(LASER, METEOR_LIST, True)
		for METEOR in METEOR_HIT_LIST:
			ALL_SPRITE_LIST.remove(LASER)
			LASER_LIST.remove(LASER)
			SCORE += 1
			#TEXT1 = FONT1.render("Score: " + str(SCORE), 0, BLACK)
		if LASER.rect.y < -10:
			ALL_SPRITE_LIST.remove(LASER)
			LASER_LIST.remove(LASER)
	WIN.fill(WHITE)

	ALL_SPRITE_LIST.draw(WIN)
	#WIN.blit(TEXT1,(10,10))
	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)