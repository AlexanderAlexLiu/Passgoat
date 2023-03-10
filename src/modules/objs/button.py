from __future__ import annotations
from modules.objs.textlabel import TextLabel
import pygame as pg
from typing import Callable
import modules.color as COLOR


class Button(TextLabel):
    def __init__(self, text: str, font: pg.font.Font, colors: tuple[tuple], func: Callable = None, param=None) -> None:
        super().__init__(text, font, colors)
        self.surface_hover = self.font.render(
            self.text, Button.ANTIALIAS, self.colors[1])
        self.surface_click = self.font.render(
            self.text, Button.ANTIALIAS, self.colors[2])
        self.hover, self.click, self.func, self.param = False, False, func, param

    def set_text(self, text: str) -> Button:
        super().set_text(text)
        self.surface_hover = self.font.render(
            self.text, TextLabel.ANTIALIAS, self.colors[1])
        self.surface_click = self.font.render(
            self.text, TextLabel.ANTIALIAS, self.colors[2])
        return self

    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            if self.click:
                surface.blit(self.surface_click, self.rect)
            elif self.hover:
                surface.blit(self.surface_hover, self.rect)
            else:
                surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            pg.draw.rect(surface, COLOR.RED, self.rect, 1)
            pg.draw.rect(surface, COLOR.BLACK, self.old_rect, 1)
            self.set_dirty(False)

    def handle_event(self, event: pg.event.Event) -> bool:
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.collidepoint(event.pos):
                        self.click = True
                        self.set_dirty()
            case pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.click:
                        self.click = False
                        if self.func:
                            if self.param == None:
                                self.func()
                            else:
                                self.func(self.param)
                        self.set_dirty()
            case pg.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    if not self.hover:
                        self.hover = True
                        self.set_dirty()
                elif self.hover:
                    self.hover = False
                    self.set_dirty()
        return self.dirty

    def reset(self) -> None:
        self.hover, self.click = False, False
