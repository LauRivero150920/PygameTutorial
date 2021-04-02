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
pygame.display.set_caption("Tutorial Pygame2: Player Move")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

# Variable salir bucke principal
DONE = False

# Cargar Imagen
BACK = pygame.image.load("Images/background.png").convert()
PLAYER = pygame.image.load("Images/player.png").convert()

# Quitar fondo de la imagen
PLAYER.set_colorkey(BLACK)

# Quitar mouse visible
pygame.mouse.set_visible(0)

while not DONE:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True
	
	MOUSE_POS = pygame.mouse.get_pos()
	x = MOUSE_POS[0]
	y = MOUSE_POS[1]

	WIN.blit(BACK, [0, 0])
	WIN.blit(PLAYER, [x,y])

	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)