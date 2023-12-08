from pygame import draw
from typing import Tuple

class Dot:
    def __init__(self, window, position: Tuple[int, int], color: Tuple[int, int, int]):
        self.window = window
        self.position = position
        self.color = color

    def draw(self):
        draw.circle(self.window, self.color, self.position, 16)

class Line:
    pass