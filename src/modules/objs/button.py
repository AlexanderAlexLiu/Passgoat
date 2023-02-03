from __future__ import annotations
from modules.objs.textlabel import TextLabel
from modules.objs.colorgroups import ColorGroup
import pygame as pg
from typing import Callable
class Button(TextLabel):
    ALIAS = True
    def __init__(self, text: str, font: pg.font.Font, colors: ColorGroup, func : Callable, param = None) -> None:
        super().__init__(text, font, colors)
        self.surface_hover = self.font.render(self.text, Button.ALIAS, self.colors[1])
        self.surface_click = self.font.render(self.text, Button.ALIAS, self.colors[2])
        self.hover, self.click = False, False
        self.func, self.param = func, param
    def set_text(self, text: str) -> Button:
        self.text = text
        self.old_rect = self.rect.copy()
        self.surface = self.font.render(self.text, TextLabel.ALIAS, self.colors[0])
        self.surface_hover = self.font.render(self.text, Button.ALIAS, self.colors[1])
        self.surface_click = self.font.render(self.text, Button.ALIAS, self.colors[2])
        self.rect.size = self.surface.get_size()
        return self
    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            super().draw(surface)
            if self.click:
                surface.blit(self.surface_click, self.rect)
            elif self.hover:
                surface.blit(self.surface_hover, self.rect)
            else:
                surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            self.set_dirty(False)
    def handle_event(self, event: pg.event.Event) -> None:
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.click = True
                    self.set_dirty()
            case pg.MOUSEBUTTONUP:
                if self.click:
                    self.click = False
                    if not self.rect.collidepoint(event.pos):
                        self.hover = False
                    if self.func:
                        if self.param:
                            self.func(self.param)
                        else:
                            self.func()
                    self.set_dirty()
            case pg.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    if not self.hover:
                        self.hover = True
                        self.set_dirty()
                elif self.hover:
                    self.hover = False
                    self.set_dirty()