from pygame import Surface, Color
from pygame.font import Font
from pygame.event import Event
from pygame import Rect
from text_label import ALIAS
from text_label import TextLabel
from typing import Callable
import pygame as pg


class ButtonLabel(TextLabel):
    def __init__(self, font: Font, text: str = '', color: Color = (0, 0, 0), hover_color: Color = (0, 0, 0), click_color: Color = (0, 0, 0), click_function: Callable = None, click_argument=None) -> None:
        super().__init__(font, text, color)
        self.hover_color, self.click_color = hover_color, click_color
        self.click_function = click_function
        self.click_argument = click_argument
        self.hover, self.click = False, False
        self.hover_surface = self.font.render(
            self.text, ALIAS, self.hover_color)
        self.click_surface = self.font.render(
            self.text, ALIAS, self.click_color)

    def set_text(self, text: str = ''):
        self.text = text
        self.surface = self.font.render(self.text, ALIAS, self.color)
        self.hover_surface = self.font.render(
            self.text, ALIAS, self.hover_color)
        self.click_surface = self.font.render(
            self.text, ALIAS, self.click_color)
        self.old_rect = self.rect.copy()
        self.rect.width, self.rect.height = self.surface.get_size()

    def run_function(self) -> None:
        self.click = False
        if self.click_argument:
            self.click_function(self.click_argument)
        else:
            self.click_function()

    def handle_event(self, event: Event) -> None:
        match event.type:
            case pg.MOUSEBUTTONUP:
                if event.button == 1 and self.click:
                    self.run_function()
                    self.wake()
            case pg.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    self.click = True
                    self.wake()
            case pg.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    if not self.hover:
                        self.hover = True
                        self.wake()
                elif self.hover:
                    self.hover = False
                    self.wake()

    def render(self, surface: Surface):
        if self.do_render:
            if self.click:
                surface.blit(self.click_surface, (self.rect.x, self.rect.y))
            elif self.hover:
                surface.blit(self.hover_surface, (self.rect.x, self.rect.y))
            else:
                surface.blit(self.surface, (self.rect.x, self.rect.y))
            self.do_render = False
            self.old_rect = self.rect.copy()
