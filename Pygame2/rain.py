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
pygame.display.set_caption("Tutorial Pygame2: Rain Animation")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

COOR_LIST = []

for i in range(60):
		x = random.randint(0, 800)
		y = random.randint(0,500)
		COOR_LIST.append([x,y])

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	WIN.fill(WHITE)
	for coord in COOR_LIST:
		pygame.draw.circle(WIN, RED, coord, 2)
		coord[1] += 1
		if coord[1] > 500:
			coord[1] = 0

	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)