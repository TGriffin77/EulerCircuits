import pygame

class Screen:
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((600,800))
		pygame.display.set_caption("Euler's Circuit")

	def loop(self):
		running = True

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

				self.window.fill((255,255,0))

				pygame.display.flip()


screen = Screen()
screen.loop()