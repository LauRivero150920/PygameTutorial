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
pygame.display.set_caption("Tutorial Pygame2")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	# Color de fondo
	WIN.fill(WHITE)
	# ----- Zona de Dibujo
	pygame.draw.line(WIN, GREEN, (0, 100), (200, 300), 5)
	pygame.draw.rect(WIN, BLACK, (100, 100, 80, 80))
	pygame.draw.circle(WIN, RED, (400,250), 100)
	# ----- Zona de Dibujo

	# Actualizar pantalla
	pygame.display.flip()