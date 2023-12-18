from pygame import draw, Surface, Rect
from typing import Tuple

from constants import *

class Vertex:
    def __init__(self, window: Surface, position: Tuple[int, int]):
        self.window = window
        self.position = position
        self.rect = Rect

    def draw(self):
        self.rect = draw.circle(self.window, VERTEX_COLOR, self.position, VERTEX_SIZE)

class Edge:
    def __init__(self, window: Surface, vertex1: Vertex, vertex2: Vertex):
        self.window = window
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.rect = Rect

    def draw(self):
        self.rect = draw.line(self.window, EDGE_COLOR, self.vertex1.position, self.vertex2.position, EDGE_SIZE)