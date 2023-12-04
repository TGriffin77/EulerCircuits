import pygame

class Screen:
	def __init__(self):
		# pygame window initialization
		pygame.init()
		self.window = pygame.display.set_mode((600,800))
		pygame.display.set_caption("Euler's Circuit")

		# class variables
		self.dots = []

	def loop(self):
		running = True

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			self.window.fill('BLACK')

			self.mouse = pygame.mouse.get_pos()
			self.dot_follow_mouse()


			pygame.display.flip()

	def dot_follow_mouse(self):
		if self.mouse == (0,0):
			return
		pygame.draw.circle(self.window, 'white', self.mouse, 16)