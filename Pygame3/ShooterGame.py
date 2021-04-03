import pygame, random

WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ShooterGame!")

CLOCK = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2;
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0

	def update(self):
		self.speed_x = 0
		KEY_STATE = pygame.key.get_pressed()
		if KEY_STATE[pygame.K_LEFT]:
			self.speed_x = -5
		if KEY_STATE[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x

		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

	def Shoot(self):
		BULLET = Bullet(self.rect.centerx, self.rect.top)
		ALL_SPRITES.add(BULLET)
		BULLETS.add(BULLET)

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/meteorGrey_med1.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speed_y = random.randrange(1, 10)
		self.speed_x = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speed_y
		self.rect.x += self.speed_x

		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speed_y = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

# Cargar imagen de fondo
BACK = pygame.image.load("assets/background.png").convert()

ALL_SPRITES = pygame.sprite.Group()
METEOR_LIST = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()

PLAYER = Player()
ALL_SPRITES.add(PLAYER)

for i in range(8):
	METEOR = Meteor()
	ALL_SPRITES.add(METEOR)
	METEOR_LIST.add(METEOR)

RUNNING = True

while RUNNING:
	CLOCK.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUNNING = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				PLAYER.Shoot()

	ALL_SPRITES.update()
	# Checar colisiones meteoro - laser
	HITS = pygame.sprite.groupcollide(METEOR_LIST, BULLETS, True, True)
	for HIT in HITS:
		METEOR = Meteor()
		ALL_SPRITES.add(METEOR)
		METEOR_LIST.add(METEOR)
	# Checar colisiones jugador - meteoro
	HITS = pygame.sprite.spritecollide(PLAYER, METEOR_LIST, True)
	if HITS:
		RUNNING = False

	WIN.blit(BACK, [0,0])

	ALL_SPRITES.draw(WIN)

	pygame.display.flip()

pygame.quit()