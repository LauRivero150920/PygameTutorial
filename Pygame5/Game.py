import pygame, sys, random
from pygame.locals import *
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
pygame.display.set_caption("Mario")

BACK =  pygame.image.load(os.path.join('Images', 'fondo.png')).convert()
MARIO = pygame.image.load(os.path.join("Images", "mario.png")).convert()

# Controlar frames per second 
CLOCK = pygame.time.Clock()

def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		WIN.fill(WHITE)
		# Actualizar pantalla
		pygame.display.flip()
		# Controlar frames por segundo (Normalmente 60)
		CLOCK.tick(60)

 
if __name__ == '__main__': 
	main()