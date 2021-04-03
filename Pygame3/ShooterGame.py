import pygame, random

WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (84, 255, 130)

pygame.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ShooterGame!")

CLOCK = pygame.time.Clock()

def Draw_Text(surface, text, size, x, y):
	FONT = pygame.font.SysFont("Berlin Sans FB", size)
	text_surface = FONT.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x ,y)
	surface.blit(text_surface, text_rect)

def Draw_Shield_Bar(surface, x, y, percentage):
	BAR_LENGTH = 200
	BAR_HEIGHT = 20
	FILL = (percentage / 100) * BAR_LENGTH
	BORDER = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
	FILL = pygame.Rect(x, y, FILL, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, FILL)
	pygame.draw.rect(surface, WHITE, BORDER, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2;
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.shield = 100

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
		# LASER_SOUND.play()

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(METEOR_IMAGES)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speed_y = random.randrange(1, 10)
		self.speed_x = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speed_y
		self.rect.x += self.speed_x

		if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 25:
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

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = EXPLOSION_ANIM[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0 # Recorre el arreglo de imagenes
		self.last_update = pygame.time.get_ticks() # Tiempo transcurrido del inicio
		self.frame_rate = 50 # Velocidad de la explosión

	def update(self):
		NOW = pygame.time.get_ticks() # Tiempo cuando quiero crear explosión
		if NOW - self.last_update > self.frame_rate:
			self.last_update = NOW
			self.frame += 1
			if self.frame == len(EXPLOSION_ANIM): # Si llegue al final de la lista elimina sprites
				self.kill()
			else:
				center = self.rect.center
				self.image = EXPLOSION_ANIM[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

def Show_GO_Screen():
	WIN.blit(BACK, [0, 0])
	Draw_Text(WIN, "Space Shooter", 65, WIDTH // 2, HEIGHT // 4)
	Draw_Text(WIN, "Start your adventure sapce pilot!", 27, WIDTH // 2, HEIGHT // 2)
	Draw_Text(WIN, "Press Key to beign", 20, WIDTH // 2, HEIGHT *  3 / 4)
	pygame.display.flip()
	waiting = True
	while waiting:
		CLOCK.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False


METEOR_IMAGES = []
METEOR_ROUTES = ["assets/meteorGrey_big1.png", "assets/meteorGrey_big2.png", "assets/meteorGrey_big3.png", "assets/meteorGrey_big4.png",
				"assets/meteorGrey_med1.png", "assets/meteorGrey_med2.png", "assets/meteorGrey_small1.png", "assets/meteorGrey_small2.png",
				"assets/meteorGrey_tiny1.png", "assets/meteorGrey_tiny2.png"]

for img in METEOR_ROUTES:
	METEOR_IMAGES.append(pygame.image.load(img).convert())

# ..................... Explosión Imagenes
EXPLOSION_ANIM = []
for i in range(9):
	FILE = "assets/regularExplosion0{}.png".format(i)
	IMG = pygame.image.load(FILE).convert()
	IMG.set_colorkey(BLACK)
	IMG_SCALE = pygame.transform.scale(IMG, (70, 70))
	EXPLOSION_ANIM.append(IMG_SCALE)

# Cargar Sonidos
LASER_SOUND = pygame.mixer.Sound("assets/laser5.ogg")
EXPLOSION_SOUND = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music.ogg")
#Volumen
pygame.mixer.music.set_volume(0.2)

# Cargar imagen de fondo
BACK = pygame.image.load("assets/background.png").convert()

# Game Over
GAME_OVER = True

RUNNING = True

# Repetir infinitamente (-1)
#pygame.mixer.music.play(loops = -1)

while RUNNING:

	if GAME_OVER:

		Show_GO_Screen()

		GAME_OVER = False
		ALL_SPRITES = pygame.sprite.Group()
		METEOR_LIST = pygame.sprite.Group()
		BULLETS = pygame.sprite.Group()

		PLAYER = Player()
		ALL_SPRITES.add(PLAYER)

		for i in range(8):
			METEOR = Meteor()
			ALL_SPRITES.add(METEOR)
			METEOR_LIST.add(METEOR)

		SCORE = 0

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
		SCORE += 10
		EXPLOSION = Explosion(HIT.rect.center)
		ALL_SPRITES.add(EXPLOSION)
		# EXPLOSION_SOUND.play()
		METEOR = Meteor()
		ALL_SPRITES.add(METEOR)
		METEOR_LIST.add(METEOR)

	# Checar colisiones jugador - meteoro
	HITS = pygame.sprite.spritecollide(PLAYER, METEOR_LIST, True)
	for HIT in HITS:
		PLAYER.shield -= 25
		METEOR = Meteor()
		ALL_SPRITES.add(METEOR)
		METEOR_LIST.add(METEOR)
		if(PLAYER.shield <= 0):
			GAME_OVER = True

	WIN.blit(BACK, [0,0])

	ALL_SPRITES.draw(WIN)

	# Marcador
	Draw_Text(WIN, "Score: " + str(SCORE), 25, WIDTH // 2, 10)
	Draw_Text(WIN, "Health: ", 20, 40, 10)

	# Barra de Salud
	Draw_Shield_Bar(WIN, 10, 35, PLAYER.shield) 

	pygame.display.flip()

pygame.quit()