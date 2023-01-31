from pygame import Surface, Color
from pygame.font import Font
from pygame.event import Event
from pygame import Rect
from text_label import ALIAS
from text_label import TextLabel
from typing import Callable
import pygame as pg


class ToggleLabel(TextLabel):
    '''
    haha im done with this function, it's miles too long for the init
    '''

    def __init__(self, font: Font, text: str = '', color: Color = (0, 0, 0), hover_color: Color = (0, 0, 0), click_color: Color = (0, 0, 0), toggle_color: Color = (0, 0, 0), toggle_on_function: Callable = None, toggle_off_function: Callable = None, toggle_on_argument=None, toggle_off_argument=None) -> None:
        super().__init__(font, text, color)
        self.hover_color, self.click_color, self.toggle_color = hover_color, click_color, toggle_color
        self.toggle_on_function = toggle_on_function
        self.toggle_on_argument = toggle_on_argument
        self.toggle_off_function = toggle_off_function
        self.toggle_off_argument = toggle_off_argument
        self.hover, self.click, self.toggle = False, False, False
        self.hover_surface = self.font.render(
            self.text, ALIAS, self.hover_color)
        self.click_surface = self.font.render(
            self.text, ALIAS, self.click_color)
        self.toggle_surface = self.font.render(
            self.text, ALIAS, self.toggle_color
        )

    def set_text(self, text: str = ''):
        self.text = text
        self.surface = self.font.render(self.text, ALIAS, self.color)
        self.hover_surface = self.font.render(
            self.text, ALIAS, self.hover_color)
        self.click_surface = self.font.render(
            self.text, ALIAS, self.click_color)
        self.toggle_surface = self.font.render(
            self.text, ALIAS, self.toggle_color)
        self.old_rect = self.rect.copy()
        self.rect.width, self.rect.height = self.surface.get_size()

    def run_toggle_on(self) -> None:
        self.click, self.hover, self.toggle = False, False, True
        if self.toggle_on_argument:
            self.toggle_on_function(self.toggle_on_argument)
        else:
            self.toggle_on_function()

    def run_toggle_off(self) -> None:
        self.click, self.hover, self.toggle = False, False, False
        if self.toggle_off_argument:
            self.toggle_off_function(self.toggle_off_argument)
        else:
            self.toggle_off_function()

    def handle_event(self, event: Event) -> None:
        match event.type:
            case pg.MOUSEBUTTONUP:
                if event.button == 1 and self.click:
                    if self.toggle:
                        self.run_toggle_off()
                    else:
                        self.run_toggle_on()
                    self.wake()
            case pg.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    self.click = True
                    self.wake()
            case pg.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.hover = True
                else:
                    self.hover = False
                self.wake()

    def render(self, surface: Surface):
        print('DRAWING: {}'.format(self.text))
        if self.do_render:
            if self.click:
                surface.blit(self.click_surface, (self.rect.x, self.rect.y))
            elif self.hover:
                surface.blit(self.hover_surface, (self.rect.x, self.rect.y))
            elif self.toggle:
                surface.blit(self.toggle_surface, (self.rect.x, self.rect.y))
            else:
                surface.blit(self.surface, (self.rect.x, self.rect.y))
            self.do_render = False
