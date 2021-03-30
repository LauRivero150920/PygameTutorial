import pygame
import os
<<<<<<< refs/remotes/origin/main
import sys
from random import randint
# Creación de ventana de juego
WIDTH, HEIGHT = 600, 300
=======
from random import randint
# Creación de ventana de juego
WIDTH, HEIGHT = 500, 300
>>>>>>> Pygame1 7.Random
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")

# Colores : Red Green Blue (0-255)
BLUE1 = (52, 235, 229)
BLUE2 = pygame.Color(52, 162, 235)
ORANGE = (252, 132, 3)
WHITE = pygame.Color(255,255,255)

# Dibujar línea: superficie, color, inicio de la recta, fin de la recta, ancho línea
#pygame.draw.line(WIN,BLUE2,(60,80),(160,100),10)

""" Figuras """

# Dibujar Círculo: superficie, color, coordenadas x,y del punto central, radio, ancho línea
#pygame.draw.circle(WIN,ORANGE,(80,90),20)

# dibujar Rectángulo: superficie, color, 4 valores (esquina superior izquierda, ancho línea 
# y alto), radio, ancho
#pygame.draw.rect(WIN,BLUE2,(0,0,100,50))

# Dibujar Poligono: superficie, color, tupla de tuplas (posiciones xy de puntos)
#pygame.draw.polygon(WIN,BLUE1,((140,0),(291,106),(237,277),(56,277),(0,106)),5)


# Métodos de los colores / Filtros, para usar debe ser pygame.Color
# Saturación en rojo
#print(BLUE2.r)
# Saturación en rojo
#print(BLUE2.g)
# Saturación en azul
#print(BLUE2.b)

""" Cargar imagenes """
<<<<<<< refs/remotes/origin/main
#IMAGE1 = pygame.image.load(os.path.join('Images', 'red_panda.png'))
=======
IMAGE1 = pygame.image.load(os.path.join('Images', 'red_panda.png'))
>>>>>>> Pygame1 7.Random

# Imagen en posición random
IMAGE1_x, IMAGE1_y = randint(10,300), randint(10,200)
# blit: imagen, tupla (posx, posy)
<<<<<<< refs/remotes/origin/main
#WIN.blit(IMAGE1,(IMAGE1_x,IMAGE1_y))

""" Movimiento de imagenes """
VEL = 5
RIGHT = True

""" Colisiones de rectangulos """
RECT1 = pygame.Rect(0,0,100,50)
RECT2 = pygame.Rect(200,200,100,50)
=======
WIN.blit(IMAGE1,(IMAGE1_x,IMAGE1_y))


>>>>>>> Pygame1 7.Random
while True:
	WIN.fill(WHITE)

	#WIN.blit(IMAGE1,(IMAGE1_x,IMAGE1_y))

	pygame.draw.rect(WIN, BLUE1, RECT1)
	pygame.draw.rect(WIN, BLUE2, RECT2)

	# left -> coordenada en x, top -> corrdenada en y, mueve con mouse
	RECT1.left, RECT1.top = pygame.mouse.get_pos()

	if RECT1.colliderect(RECT2):
		VEL = 0
		print("Colision")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		""" Keys + Mouse
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				IMAGE1_x -= VEL
			if event.key == pygame.K_RIGHT:
				IMAGE1_x += VEL
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				print("Tecla izquierda liberada")
			if event.key == pygame.K_RIGHT:
				IMAGE1_x += VEL
				print("Tecla derecha  liberada")
	#IMAGE1_x, IMAGE1_y = pygame.mouse.get_pos()
	#IMAGE_x, IMAGE_y = IMAGE1_x - 100, IMAGE1_y - 50
		"""
	# Mover animación 
	if RIGHT == True:
		if IMAGE1_x < 400:
			IMAGE1_x += VEL
			RECT2.left = IMAGE1_x
		else:
			RIGHT = False
	else:
		if IMAGE1_x > 1:
			IMAGE1_x -= VEL 
			RECT2.left = IMAGE1_x
		else:
			RIGHT = True
	pygame.display.update()
