'''
Alex Liu
2023-01-26
Class for any button label in passgoat
'''

from pygame.font import Font
from pygame.color import Color
from pygame.event import Event
from txtlbl import TextLabel
import pygame.constants as pg
from pygame import Surface

class ButtonLabel(TextLabel):
    def __init__(self, text: str, font: Font, color: Color, hover : Color, click : Color, anti_alias: bool = False) -> None:
        super().__init__(text, font, color, anti_alias)
        self.__hover_color, self.__click_color, self.__click, self.__hover = hover, click, False, False
        self.__hover_surface = self.__font.render(self.__text, self.__anti_alias, self.__hover_color)
        self.__click_surface = self.__font.render(self.__text, self.__anti_alias, self.__click_color)
        self.__function, self.__argument = None, None
    def assign_function(self, function, argument) -> None:
        self.__function, self.__argument = function, argument
    def __execute_function(self) -> None:
        self.__function(self.__argument)
    def handle_event(self, event: Event) -> None:
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if self.__next_rect.collidepoint(event.pos):
                    self.__click = True
                    self.__render = True
            case pg.MOUSEBUTTONUP:
                if self.__click:
                    self.__click = False
                    self.__hover = False
                    self.__execute_function()
            case pg.MOUSEMOTION:
                if self.__next_rect.collidepoint(event.pos):
                    self.__hover = True
                    self.__render = True
                elif self.__hover:
                    self.__hover = False
                    self.__render = True
            case _:
                return
    def render(self, surface: Surface) -> None:
        if self.__render:
            if self.__click:
                surface.blit(self.__click_surface, (self.__x, self.__y))
            elif self.__hover:
                surface.blit(self.__hover_surface, (self.__x, self.__y))
            else:
                surface.blit(self.__surface, (self.__x, self.__y))
            self.__render = False
