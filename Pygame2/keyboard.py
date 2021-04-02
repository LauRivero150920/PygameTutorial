import pygame, sys, random
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

SIZE = (800, 500)

# Crear ventana
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tutorial Pygame2: Keyboard")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

#Coordenadas del cuadrado
COORD_X = 10
COORD_Y = 10

#Velocidad
X_SPEED = 0
Y_SPEED = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# Eventos teclado (dentro del for)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				X_SPEED = -3
			if event.key == pygame.K_RIGHT:
				X_SPEED = 3
			if event.key == pygame.K_UP:
				Y_SPEED = -3
			if event.key == pygame.K_DOWN:
				Y_SPEED = 3

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				X_SPEED = 0
			if event.key == pygame.K_RIGHT:
				X_SPEED = 0
			if event.key == pygame.K_UP:
				Y_SPEED = 0
			if event.key == pygame.K_DOWN:
				Y_SPEED = 0

	WIN.fill(WHITE)

	COORD_X += X_SPEED 
	COORD_Y += Y_SPEED 
	pygame.draw.rect(WIN, RED, (COORD_X, COORD_Y, 100, 100))

	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)