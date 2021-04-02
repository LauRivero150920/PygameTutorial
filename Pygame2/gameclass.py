import pygame, sys, random
pygame.font.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dimensiones ventana
WIDTH = 900
HEIGHT = 600

SCORE = 0

class Meteorite(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/meteor.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1
		if self.rect.y > 600:
			self.rect.y = -10
			self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Images/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		MOUSE_POS = pygame.mouse.get_pos()
		self.rect.x = MOUSE_POS[0]
		self.rect.y = MOUSE_POS[1]

class Game(object):
	def __init__(self):
		self.GAME_OVER = False
		self.SCORE = 0
		self.METEOR_LIST = pygame.sprite.Group()
		self.ALL_SPRITE_LIST = pygame.sprite.Group()

		for i in range(50):
			METEOR = Meteorite()
			METEOR.rect.x = random.randrange(WIDTH)
			METEOR.rect.y = random.randrange(HEIGHT)
			
			self.METEOR_LIST.add(METEOR)
			self.ALL_SPRITE_LIST.add(METEOR)

		self.PLAYER = Player()
		self.ALL_SPRITE_LIST.add(self.PLAYER)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True 
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.GAME_OVER:
					self.__init__()
		return False
	
	def run_logic(self):
		if not self.GAME_OVER:
			self.ALL_SPRITE_LIST.update()
			METEOR_HIT_LIST = pygame.sprite.spritecollide(self.PLAYER, self.METEOR_LIST, True)
			for METEOR in METEOR_HIT_LIST:
				self.SCORE += 1
				print(self.SCORE)
			if len(self.METEOR_LIST) == 0:
				self.GAME_OVER = True

	def display_frame(self, screen):
		screen.fill(WHITE)
		if self.GAME_OVER:
			FONT = pygame.font.SysFont("Arial", 25)
			TEXT = FONT.render("Game Over, Click to Continue", True, BLACK)
			CENTER_x = (WIDTH // 2) - (TEXT.get_width() // 2)
			CENTER_y = (HEIGHT // 2) - (TEXT.get_height() // 2)
			screen.blit(TEXT, [CENTER_x, CENTER_y])

		if not self.GAME_OVER:
			self.ALL_SPRITE_LIST.draw(screen)
		pygame.display.flip()

def main():
	pygame.init()

	WIN = pygame.display.set_mode([WIDTH, HEIGHT])
	CLOCK = pygame.time.Clock()
	DONE = False

	GAME = Game()

	while not DONE:
		DONE = GAME.process_events()
		
		GAME.run_logic()
		GAME.display_frame(WIN)

		CLOCK.tick(60)

	pygame.quit()

if __name__ == "__main__":
	main()