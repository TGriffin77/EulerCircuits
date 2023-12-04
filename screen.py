import pygame
from typing import Tuple

class Screen:
    def __init__(self) -> None:
        # pygame window initialization
        pygame.init()
        self.window = pygame.display.set_mode((600,800))
        pygame.display.set_caption("Euler's Circuit")

		# class variables
        self.dots = []
        self.buttons = []

    def loop(self) -> None:
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill('BLACK')

            self.mouse = pygame.mouse.get_pos()
            self.dot_follow_mouse()

            pygame.display.flip()

    def dot_follow_mouse(self) -> None:
        if self.mouse == (0,0):
            return
        pygame.draw.circle(self.window, 'white', self.mouse, 16)

class Button:
    def __init__(self, window: pygame.Surface, color: Tuple[int, int, int], 
                 coordinates: Tuple[int, int], 
                 width: float, height: float, text: str) -> None:
		
        self.button_rect = pygame.draw.rect(window, color, pygame.rect.Rect(coordinates[0], coordinates[1], width, height))
