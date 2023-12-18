import pygame
from typing import Tuple

from constants import *
from euler import Vertex, Edge

class Screen:
    def __init__(self) -> None:
        # pygame window initialization
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Euler's Circuit")

		# class variables
        self.vertices = []
        self.edges = []
        self.menu = Menu(self.window)
        self.mode = "Vertex"
        self.selection = Vertex
        self.selecting = False

    def loop(self) -> None:
        running = True

        while running:
            self.mouse = pygame.mouse.get_pos()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
 
                if event.type == pygame.MOUSEMOTION:
                    self.button_motion_loop()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.vertex_loop()
                    self.edge_loop(event)

                    self.button_click_loop()

            pygame.display.flip()

    def draw(self) -> None:
        self.window.fill(SCREEN_BACKGROUND)
            
        for vertex in self.vertices:
            vertex.draw()
        for edge in self.edges:
            edge.draw()
        
        if self.mode == "Vertex":
            self.vertex_follow_mouse()
        elif self.mode == "Edge":
            pass
        else:
            raise Exception("Invalid mode activated, terminating application")
        
        self.menu.draw()

    def vertex_follow_mouse(self) -> None:
        if self.mouse == (0,0):
            return
        if self.mouse[1] < MENU_HEIGHT:
            return
        pygame.draw.circle(self.window, CURSOR_COLOR, self.mouse, VERTEX_SIZE)

    def vertex_loop(self) -> None:
        # Place vertices on click
        if self.mouse[1] > MENU_HEIGHT and self.mode == "Vertex":
            self.vertices.append(Vertex(self.window, self.mouse))

    def edge_loop(self, event: pygame.event.Event) -> None:
        # Place edges on hold
        if self.mouse[1] > MENU_HEIGHT and self.mode == "Edge":
            # left click
            if event.button == 1:
                for vertex in self.vertices:
                    if vertex.rect.collidepoint(event.pos):
                        if not self.selecting:
                            self.selecting = True
                            self.selection = vertex
                        else:
                            new_edge = Edge(self.window, self.selection, vertex)
                            for edge in self.edges:
                                if (new_edge.vertex1 == edge.vertex1 and new_edge.vertex2 == edge.vertex2) or (new_edge.vertex1 == edge.vertex2 and new_edge.vertex2 == edge.vertex1):
                                    self.selecting = False
                            if self.selecting:
                                self.edges.append(new_edge)
                                self.selecting = False
                                self.selection = None
                        
            # right click 
            if event.button == 3:
                self.selecting = False

    def button_click_loop(self) -> None:
        # Check for button clicks
        for button in self.menu.buttons:
            if button.rect.left < self.mouse[0] < button.rect.right and button.rect.top < self.mouse[1] < button.rect.bottom:
                self.mode = button.press()

    def button_motion_loop(self) -> None:
        for button in self.menu.buttons:
            if button.rect.left < self.mouse[0] < button.rect.right and button.rect.top < self.mouse[1] < button.rect.bottom:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                button.hover()
                break
            else:
                button.idle()
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    

class Button:
    def __init__(self, window: pygame.Surface,  
                 coordinates: Tuple[int, int], 
                 width: float, height: float, text: str) -> None:
		
        self.window = window
        self.color = BUTTON_COLOR
        self.rect = pygame.rect.Rect(coordinates[0], coordinates[1], width, height)
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.button_text = self.font.render(self.text, True, (0,0,0))
    
    def draw(self) -> None:
        pygame.draw.rect(self.window, self.color, self.rect)

        self.window.blit(self.button_text, self.button_text.get_rect(center = self.rect.center))

    def press(self) -> None:
        self.color = PRESS_BUTTON_COLOR
        return self.text
    
    def hover(self) -> None:
        self.color = HOVER_BUTTON_COLOR

    def idle(self) -> None:
        self.color = BUTTON_COLOR


class Menu:
    def __init__(self, window: pygame.Surface) -> None:

        self.window = window
        self.color = MENU_COLOR
        self.buttons = self.init_buttons()
        self.rect = pygame.rect.Rect(0, 0, WIDTH, MENU_HEIGHT)

    def init_buttons(self) -> list[Button]:
        res = []

        # Append all buttons required.
        size = (int(WIDTH*.395), int(MENU_HEIGHT*0.86))

        coords1 = (int(WIDTH*0.07), int(MENU_HEIGHT*0.07))
        res.append(Button(self.window, coords1, size[0], size[1], 'Vertex'))

        coords2 = (int(WIDTH*0.535), int(MENU_HEIGHT*0.07))
        res.append(Button(self.window, coords2, size[0], size[1], 'Edge'))

        return res

    def draw(self) -> None:
        pygame.draw.rect(self.window, self.color, self.rect)
        for button in self.buttons:
            button.draw()