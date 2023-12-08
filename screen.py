import pygame
from typing import Tuple

from constants import *
from euler import Vertex, Edge

class Screen:
    def __init__(self) -> None:
        # pygame window initialization
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Euler's Circuit")

		# class variables
        self.vertices = []
        self.menu = Menu(self.window, MENU_COLOR)
        self.mode = "Vertex"

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
                        self.vertices.append(Vertex(self.window, self.mouse, VERTEX_COLOR))
                    for button in self.menu.buttons:
                        if button.rect.left < self.mouse[0] < button.rect.right and button.rect.top < self.mouse[1] < button.rect.bottom:
                            button.press()

            pygame.display.flip()

    def draw(self):
        self.window.fill(SCREEN_BACKGROUND)
            
        for vertex in self.vertices:
            vertex.draw()
        
        self.vertex_follow_mouse()
        self.menu.draw()

    def vertex_follow_mouse(self) -> None:
        if self.mouse == (0,0):
            return
        if self.mouse[1] < MENU_HEIGHT:
            return
        pygame.draw.circle(self.window, CURSOR_COLOR, self.mouse, VERTEX_SIZE)


class Button:
    def __init__(self, window: pygame.Surface, color: Tuple[int, int, int], 
                 coordinates: Tuple[int, int], 
                 width: float, height: float, text: str) -> None:
		
        self.window = window
        self.color = color
        self.rect = pygame.rect.Rect(coordinates[0], coordinates[1], width, height)
        self.text = text
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def press(self):
        pass


class Menu:
    def __init__(self, window: pygame.Surface, color: Tuple[int, int, int]):

        self.window = window
        self.color = color
        self.buttons = self.init_buttons()
        self.rect = pygame.rect.Rect(0, 0, WIDTH, MENU_HEIGHT)

    def init_buttons(self):
        res = []

        # Append all buttons required.
        size = (int(WIDTH*.395), int(MENU_HEIGHT*0.86))

        coords1 = (int(WIDTH*0.07), int(MENU_HEIGHT*0.07))
        res.append(Button(self.window, BUTTON_COLOR, coords1, size[0], size[1], 'Vertex'))

        coords2 = (int(WIDTH*0.535), int(MENU_HEIGHT*0.07))
        res.append(Button(self.window, BUTTON_COLOR, coords2, size[0], size[1], 'Edge'))

        return res

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        for button in self.buttons:
            button.draw()