from __future__ import annotations
from modules.objs.button import Button
import pygame as pg
from typing import Callable


class Toggle(Button):
    def __init__(self, text: str, font: pg.font.Font, colors: tuple[tuple], func: Callable = None, param=None) -> None:
        super().__init__(text, font, colors, param=param)
        self.surface_toggle = self.font.render(
            self.text, Toggle.ANTIALIAS, self.colors[3])
        self.toggle = False
        self.func = self.do_toggle()
        self.on_toggle = func

    def set_toggle(self, toggle: bool) -> None:
        self.toggle = toggle

    def handle_event(self, event: pg.event.Event) -> None:
        super().handle_event(event)

    def do_toggle(self) -> None:
        if self.on_toggle != None:
            if self.param == None:
                self.on_toggle()
            else:
                self.on_toggle(self.param)
        self.toggle = not self.toggle

    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            if self.click:
                surface.blit(self.surface_click, self.rect)
            elif self.hover:
                surface.blit(self.surface_hover, self.rect)
            elif self.toggle:
                surface.blit(self.surface_toggle, self.rect)
            else:
                surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            self.set_dirty(False)

    def get_toggle(self) -> bool:
        return self.toggle
