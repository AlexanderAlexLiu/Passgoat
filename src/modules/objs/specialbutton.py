from __future__ import annotations
from modules.objs.textlabel import TextLabel
import pygame as pg


class SpecialButton(TextLabel):
    def __init__(self, font: pg.font.Font, colors: tuple[tuple]) -> None:
        text = '_'
        super().__init__(text, font, colors)
        self.surface_hover = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[1])
        self.surface_click = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[2])
        self.surface_ghost = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[3])
        self.surface_lock = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[4])
        self.surface_wait = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[5])
        self.g_value = ''
        self.hover, self.click, self.ghost, self.lock = False, False, False, False
        self.waiting = False
        self.ghosted, self.locked = False, False

    def get_lock(self):
        return self.locked

    def get_text(self):
        return self.text
    
    def get_ghost(self):
        return self.ghosted

    def move(self, x: float = None, y: float = None) -> SpecialButton:
        super().move(x, y)
        return self

    def center(self, x: bool = False, y: bool = False) -> SpecialButton:
        super().center(x, y)
        return self

    def set_text(self, text: str) -> SpecialButton:
        super().set_text(text)
        self.surface_hover = self.font.render(
            self.text, TextLabel.ANTIALIAS, self.colors[1])
        self.surface_click = self.font.render(
            self.text, TextLabel.ANTIALIAS, self.colors[2])
        self.surface_ghost = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[3])
        self.surface_lock = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[4])
        self.surface_wait = self.font.render(
            self.text, SpecialButton.ANTIALIAS, self.colors[5])
        return self

    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            if self.waiting:
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

    def handle_event(self, event: pg.event.Event) -> bool:
        if self.waiting:
            match event.type:
                case pg.KEYDOWN:
                    if event.unicode.isnumeric():
                        self.set_text(event.unicode)
                        self.waiting = False
                        if self.ghost:
                            self.g_value = event.unicode
                            self.ghosted = True
                            self.ghost = False
                            self.locked = False
                        elif self.lock:
                            self.locked = True
                            self.lock = False
                            self.ghosted = False
                        self.set_dirty()
                        return True
                    elif event.key == 32:
                        self.waiting = False
                        self.ghosted, self.locked = False, False
                        if not self.rect.collidepoint(pg.mouse.get_pos()):
                            self.hover = False
                        self.set_text('_')
                        self.set_dirty()
                        return True
                case pg.MOUSEBUTTONDOWN:
                    if not self.rect.collidepoint(event.pos):
                        self.waiting, self.hover = False, False
                        self.set_dirty()
                        return True
        else:
            match event.type:
                case pg.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        self.click = True
                        if event.button == 1 or event.button == 3:
                            if event.button == 1:
                                self.ghost = True
                            elif event.button == 3:
                                self.lock = True
                        self.set_dirty()
                        return True
                case pg.MOUSEMOTION:
                    if self.rect.collidepoint(event.pos):
                        if not self.hover:
                            self.hover = True
                            self.set_dirty()
                            return True
                    elif self.hover:
                        self.hover = False
                        self.set_dirty()
                        return True
                case pg.MOUSEBUTTONUP:
                    if self.click:
                        if not self.rect.collidepoint(event.pos):
                            self.hover = False
                        if event.button == 1 or event.button == 3:
                            self.waiting = True
                            self.click = False
                            self.set_dirty()
                            return True
        return False

    def add_to(self, arr: list) -> None:
        super().add_to(arr)
        self.hover, self.click = False, False
