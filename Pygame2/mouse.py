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
pygame.display.set_caption("Tutorial Pygame2: Mouse")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

pygame.mouse.set_visible(0)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	MOUSE_POS = pygame.mouse.get_pos()
	x = MOUSE_POS[0]
	y = MOUSE_POS[1]
	WIN.fill(WHITE)

	#pygame.draw.rect(WIN, RED, (x, y, 100, 100))

	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)