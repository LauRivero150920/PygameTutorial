import pygame, sys
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
pygame.display.set_caption("Tutorial Pygame2: Intro")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

# Coordenadas del cuadrado
COOR_X = 400
COOR_Y = 200

# Velocidad del cuadrado
SPEED_X = 3
SPEED_Y = 30
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	# Color de fondo
	WIN.fill(WHITE)
	# ----- Zona de Dibujo
	#pygame.draw.line(WIN, GREEN, (0, 100), (200, 300), 5)
	#pygame.draw.rect(WIN, BLACK, (100, 100, 80, 80))
	#pygame.draw.circle(WIN, RED, (400,250), 100)
	# iniciar, finalizar, i++
	"""
	for x in range(100,700,60):
		pygame.draw.rect(WIN, BLACK, (x, 230, 50, 50))
		pygame.draw.line(WIN, GREEN, (x, 0), (x, 100), 5)
	"""
	# Invertir velocidad para que regrese
	if(COOR_X > 720 or COOR_X < 0):
		SPEED_X *= -1

	if(COOR_Y > 320 or COOR_Y < 0):
		SPEED_Y *= -1

	# Desplazamiento
	COOR_X += SPEED_X
	COOR_Y += SPEED_Y

	pygame.draw.rect(WIN, RED, (COOR_X, COOR_Y, 80, 80))
	# ----- Zona de Dibujo

	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)