import pygame as pg
from src.game_object import GameObject

class TextLabel(GameObject):
    def __init__(self, text : str, font : pg.font.Font, color : pg.Color, anti : bool = False) -> None:
        super().__init__()
        self.text = text
        self.font = font
        self.color = color
        self.anti = anti
        self.surface = self.font.render(self.text, self.anti, self.color)
        self.w, self.h = self.surface.get_size()
    def set_text(self, text : str) -> None:
        self.text = text
        self.surface = self.font.render(text, self.anti, self.color)
        self.w, self.h = self.surface.get_size()
        self.do_render = True
    def center_x(self, x : float = 600) -> None:
        self.x = (x - self.w) / 2
    def center_y(self, y : float = 400) -> None:
        self.y = (y - self.h) / 2