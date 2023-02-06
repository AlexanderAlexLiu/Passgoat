from __future__ import annotations
from modules.objs.gameobject import GameObject
import pygame as pg
import modules.color as COLOR


class TextLabel(GameObject):
    ANTIALIAS = True

    def __init__(self, text: str, font: pg.font.Font, color: tuple[tuple]) -> None:
        super().__init__()
        self.text = text
        self.font = font
        self.colors = color
        self.surface = self.font.render(
            self.text, TextLabel.ANTIALIAS, self.colors[0])
        self.rect = self.surface.get_rect()
        self.old_rect = self.rect.copy()

    def move(self, x: float = None, y: float = None) -> TextLabel:
        if self.dirty:
            self.old_rect = self.rect.copy()
        if x:
            self.rect.x = x
        if y:
            self.rect.y = y
        return self

    def center(self, x: bool = False, y: bool = False) -> TextLabel:
        if x:
            self.move(x=(800-self.rect.w)/2)
        if y:
            self.move(y=(400-self.rect.h)/2)
        return self

    def set_text(self, text: str) -> TextLabel:
        self.text = text
        self.old_rect = self.rect.copy()
        self.surface = self.font.render(
            self.text, TextLabel.ANTIALIAS, self.colors[0])
        self.rect.size = self.surface.get_size()
        return self

    def update(self):
        if self.dirty:
            return [self.old_rect, self.rect]

    def draw(self, surface: pg.Surface):
        if self.dirty:
            surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            pg.draw.rect(surface, COLOR.RED, self.rect, 1)
            pg.draw.rect(surface, COLOR.BLACK, self.old_rect, 1)
            self.set_dirty(False)
