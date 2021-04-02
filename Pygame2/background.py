import pygame, sys, random
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

SIZE = (720, 720)

# Crear ventana
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tutorial Pygame2: Background")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

# Variable salir bucke principal
DONE = False

# Cargar Imagen
BACK = pygame.image.load("Images/background.png").convert()
while not DONE:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True
	
	WIN.blit(BACK, [0, 0])
	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)