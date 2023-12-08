from pygame import draw
from typing import Tuple

from constants import *

class Vertex:
    def __init__(self, window, position: Tuple[int, int]):
        self.window = window
        self.position = position
        self.color = VERTEX_COLOR

    def draw(self):
        draw.circle(self.window, self.color, self.position, VERTEX_SIZE)

class Edge:
    pass