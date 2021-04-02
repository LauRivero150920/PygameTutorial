import pygame, sys, random
pygame.font.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCORE = 0

# Fonts
FONT1 = pygame.font.SysFont("Arial", 30)

class Meteorite(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/meteor.png").convert()
		self.image.set_colorkey(BLACK)
		# Posicionar Sprite
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1
		if self.rect.y > 600:
			self.rect.y = -10
			self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/player.png").convert()
		self.image.set_colorkey(BLACK)
		# Posicionar Sprite
		self.rect = self.image.get_rect()

	def update(self):
		MOUSE_POS = pygame.mouse.get_pos()
		PLAYER.rect.x = MOUSE_POS[0]
		PLAYER.rect.y = MOUSE_POS[1]

pygame.init()

SIZE = (900, 600)

# Crear ventana
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tutorial Pygame2: Sprites")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

# Variable salir bucle principal
DONE = False

# Lista de meteoros, detectar colisiones
METEOR_LIST = pygame.sprite.Group()
# Lista de todos los sprites, dibujar en pantalla
ALL_SPRITE_LIST = pygame.sprite.Group()

for i in range(50):
	METEOR = Meteorite()
	METEOR.rect.x = random.randrange(900)
	METEOR.rect.y = random.randrange(600)
	
	METEOR_LIST.add(METEOR)
	ALL_SPRITE_LIST.add(METEOR)

PLAYER = Player()
ALL_SPRITE_LIST.add(PLAYER)

while not DONE:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True 
	
	ALL_SPRITE_LIST.update()

	METEOR_HIT_LIST = pygame.sprite.spritecollide(PLAYER, METEOR_LIST, True)
	
	for METEOR in METEOR_HIT_LIST:
		SCORE += 1
		TEXT1 = FONT1.render("Score: " + str(SCORE), 0, BLACK)

	WIN.fill(WHITE)
	WIN.blit(TEXT1,(10,10))
	ALL_SPRITE_LIST.draw(WIN)
	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)