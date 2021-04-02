import pygame, sys
pygame.init()

SIZE = (800, 500)

# Crear ventana
WIN = pygame.display.set_mode(SIZE)

while True:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()
