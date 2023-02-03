from __future__ import annotations
from modules.objs.gameobject import GameObject
import pygame as pg


class Image(GameObject):
    def __init__(self, image: pg.Surface) -> None:
        super().__init__()
        self.surface = image
        self.rect = self.surface.get_rect()
        self.old_rect = self.rect.copy()

    def move(self, x: float = None, y: float = None) -> Image:
        self.old_rect = self.rect.copy()
        if x:
            self.rect.x = x
        if y:
            self.rect.y = y
        return self

    def center(self, x: bool = False, y: bool = False) -> Image:
        if x:
            self.move(x=(600-self.rect.w)/2)
        if y:
            self.move(y=(400-self.rect.h)/2)
        return self

    def update(self) -> list[pg.Rect]:
        if self.dirty:
            return [self.old_rect, self.rect]

    def draw(self, surface):
        if self.dirty:
            surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            self.set_dirty(False)
