from __future__ import annotations
from modules.objs.gameobject import GameObject
from modules.objs.colorgroups import ColorGroup
import pygame as pg

class TextLabel(GameObject):
    ALIAS = True
    def __init__(self, text : str, font : pg.font.Font, colors : ColorGroup) -> None:
        super().__init__()
        self.text = text
        self.colors = colors
        print(self.colors)
        self.font = font
        self.surface = self.font.render(self.text, TextLabel.ALIAS, self.colors[0])
        self.rect = self.surface.get_rect()
        self.old_rect = self.rect.copy()
    def move_to(self, x : float = None, y : float = None) -> TextLabel:
        self.old_rect = self.rect.copy()
        if x:
            self.rect.x = x
        if y:
            self.rect.y = y
        return self
    def center(self, x : bool = False, y : bool = False) -> TextLabel:
        if x:
            self.move_to(x = (600 - self.rect.w) / 2)
        if y:
            self.move_to(y = (400 - self.rect.h) / 2)
        return self
    def set_text(self, text : str) -> TextLabel:
        self.text = text
        self.old_rect = self.rect.copy()
        self.surface = self.font.render(self.text, TextLabel.ALIAS, self.colors[0])
        self.rect.size = self.surface.get_size()
        return self
    def update(self) -> list[pg.Rect]:
        if self.dirty:
            return [self.rect, self.old_rect]
    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            super().draw(surface)
            surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            self.dirty = False