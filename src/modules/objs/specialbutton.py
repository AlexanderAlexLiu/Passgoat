from __future__ import annotations
from modules.objs.button import Button
import pygame as pg
from typing import Callable

class SpecialButton(Button):
    def __init__(self, text: str, font: pg.font.Font, colors: tuple[tuple], func : Callable) -> None:
        super().__init__(text, font, colors, func)
        self.surface_wait = self.font.render(self.text, SpecialButton.ANTIALIAS, self.colors[3])
        self.surface_lock = self.font.render(self.text, SpecialButton.ANTIALIAS, self.colors[4])
        self.surface_ghost = self.font.render(self.text, SpecialButton.ANTIALIAS, self.colors[5])
        self.wait, self.lock, self.ghost, self.locked, self.ghosted = False, False, False, False, False
        self.next = None
        self.original = text
        self.ghost_value = ''
    def set_next(self, btn : SpecialButton) -> None:
        self.next = btn
    def get_lock(self) -> bool:
        return self.locked
    def get_text(self) -> str:
        return self.text
    def handle_event(self, event: pg.event.Event) -> bool:
        if self.wait:
            match event.type:
                case pg.MOUSEBUTTONDOWN:
                    if not self.rect.collidepoint(event.pos):
                        self.wait, self.ghost, self.locked = False, False, False
                        self.hover = False
                        self.set_dirty(True)
                case pg.KEYDOWN:
                    if event.key == 32:
                        # clear a button
                        self.wait = False
                        self.ghost_value = ''
                        self.lock, self.locked, self.ghost, self.ghosted = False, False, False, False
                        self.set_text(self.original)
                        self.set_dirty(True)
                    elif event.unicode.isnumeric():
                        # check stuff?
                        self.wait = False
                        if self.ghost:
                            self.ghost = False
                            self.ghosted = True
                            self.ghost_value = event.unicode
                            self.lock, self.locked = False, False
                        elif self.lock:
                            self.ghost_value = ''
                            self.lock = False
                            self.locked = True
                            self.ghost, self.ghosted = False, False
                        self.func() # hacky input deny
                        self.set_text(event.unicode)
                        self.set_dirty(True)
        else:
            match event.type:
                case pg.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        if event.button == 1:
                            self.ghost = True
                        elif event.button == 3:
                            self.lock = True
                        self.click = True
                        self.set_dirty()
                case pg.MOUSEBUTTONUP:
                    if self.click:
                        self.click = False
                        self.wait = True
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
    def set_text(self, text: str) -> SpecialButton:
        super().set_text(text)
        self.surface_wait = self.font.render(self.text, SpecialButton.ANTIALIAS, self.colors[3])
        self.surface_lock = self.font.render(self.text, SpecialButton.ANTIALIAS, self.colors[4])
        self.surface_ghost = self.font.render(self.text, SpecialButton.ANTIALIAS, self.colors[5])
        return self
    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            if self.wait:
                surface.blit(self.surface_wait, self.rect)
            elif self.click:
                surface.blit(self.surface_click, self.rect)
            elif self.locked:
                surface.blit(self.surface_lock, self.rect)
            elif self.ghosted:
                surface.blit(self.surface_ghost, self.rect)
            elif self.hover:
                surface.blit(self.surface_hover, self.rect)
            else:
                surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()
            self.set_dirty(False)