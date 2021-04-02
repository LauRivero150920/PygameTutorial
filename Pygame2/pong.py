import pygame, random
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

SIZE = (800, 600)
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 90
# Crear ventana
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tutorial Pygame2: PONG!!!")

# Controlar frames per second 
CLOCK = pygame.time.Clock()

# Coordenadas y velocidad jugador 1
PLAYER1_x_coor = 50
PLAYER1_y_coor = 300 - (PLAYER_HEIGHT/2)
PLAYER1_y_speed = 0

# Coordenadas y velocidad jugador 2
PLAYER2_x_coor = 750 - PLAYER_WIDTH
PLAYER2_y_coor = 300 - (PLAYER_HEIGHT/2)
PLAYER2_y_speed = 0

# Coordenadas de la pelota
BALL_x = 400
BALL_y = 300
BALL_SPEED_x = 3
BALL_SPEED_y = 3

GAME_OVER = False

while not GAME_OVER :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME_OVER = True
		if event.type == pygame.KEYDOWN:
			# Jugador 1
			if event.key == pygame.K_w:
				PLAYER1_y_speed = -3
			if event.key == pygame.K_s:
				PLAYER1_y_speed = 3

			# Jugador 2
			if event.key == pygame.K_UP:
				PLAYER2_y_speed = -3
			if event.key == pygame.K_DOWN:
				PLAYER2_y_speed = 3
		
		if event.type == pygame.KEYUP:
			# Jugador 1
			if event.key == pygame.K_w:
				PLAYER1_y_speed = 0
			if event.key == pygame.K_s:
				PLAYER1_y_speed = 0

			# Jugador 2
			if event.key == pygame.K_UP:
				PLAYER2_y_speed = 0
			if event.key == pygame.K_DOWN:
				PLAYER2_y_speed = 0
	
	# Pelota rebota arriba y abajo
	if BALL_y > 590 or BALL_y < 10:
		BALL_SPEED_y *= -1

	if BALL_x > 790 or BALL_x < 10:
		BALL_SPEED_x *= -1

	# Revisas si pelota sale del lado derecho
	if BALL_x > 800 or BALL_x < 0:
		BALL_x = 400
		BALL_y = 300
		# Si sale de la pantalla, invierte dirección
		BALL_SPEED_X *= -1
		BALL_SPEED_y *= -1

	# Modifica coordenads para dar movimiento a los jugadores/pelota

	PLAYER1_y_coor += PLAYER1_y_speed
	PLAYER2_y_coor += PLAYER2_y_speed

	# Movimiento Pelota
	BALL_x += BALL_SPEED_x
	BALL_y += BALL_SPEED_y
	WIN.fill(BLACK)

	#Jugadores -> Rectangulos
	PLAYER1 = pygame.draw.rect(WIN, WHITE, (PLAYER1_x_coor, PLAYER1_y_coor, PLAYER_WIDTH, PLAYER_HEIGHT))
	PLAYER2 = pygame.draw.rect(WIN, WHITE, (PLAYER2_x_coor, PLAYER2_y_coor, PLAYER_WIDTH, PLAYER_HEIGHT))
	BALL = pygame.draw.circle(WIN, WHITE, (BALL_x, BALL_y), 10)
	
	# Colisiones
	if BALL.colliderect(PLAYER1) or BALL.colliderect(PLAYER2):
		BALL_SPEED_x *= -1
	# Actualizar pantalla
	pygame.display.flip()
	# Controlar frames por segundo (Normalmente 60)
	CLOCK.tick(60)

pygame.quit()