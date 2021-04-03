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

ALL_SPRITES = pygame.sprite.Group()
PLAYER = Player()
ALL_SPRITES.add(PLAYER)

RUNNING = True

while RUNNING:
	CLOCK.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUNNING = False

	ALL_SPRITES.update()

	WIN.fill(BLACK)

	ALL_SPRITES.draw(WIN)

	pygame.display.flip()

pygame.quit()