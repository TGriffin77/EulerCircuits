import pygame
from typing import Tuple

from constants import *
from euler import Dot, Line

class Screen:
    def __init__(self) -> None:
        # pygame window initialization
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Euler's Circuit")

		# class variables
        self.dots = []
        self.menu = Menu(self.window, MENU_COLOR)

    def loop(self) -> None:
        running = True

        while running:
            self.mouse = pygame.mouse.get_pos()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mouse[1] > MENU_HEIGHT:
                        self.dots.append(Dot(self.window, self.mouse, DOT_COLOR))

            pygame.display.flip()

    def draw(self):
        self.window.fill('BLACK')
            
        for dot in self.dots:
            dot.draw()
        
        self.dot_follow_mouse()
        self.menu.draw()

    def dot_follow_mouse(self) -> None:
        if self.mouse == (0,0):
            return
        if self.mouse[1] < MENU_HEIGHT:
            return
        pygame.draw.circle(self.window, 'white', self.mouse, 16)

class Button:
    def __init__(self, window: pygame.Surface, color: Tuple[int, int, int], 
                 coordinates: Tuple[int, int], 
                 width: float, height: float, text: str) -> None:
		
        self.window = window
        self.color = color
        self.rect = pygame.rect.Rect(coordinates[0], coordinates[1], width, height)
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

class Menu:
    def __init__(self, window: pygame.Surface, color: Tuple[int, int, int]):

        self.window = window
        self.color = color
        self.buttons = self.init_buttons()
        self.rect = pygame.rect.Rect(0, 0, WIDTH, MENU_HEIGHT)

    def init_buttons(self):
        res = []

        # Append all buttons required.

        return res

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        for button in self.buttons:
            button.draw()