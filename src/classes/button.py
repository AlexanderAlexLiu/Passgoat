import pygame as pg
from src.text_label import TextLabel

class Button(TextLabel):
    def __init__(self, text: str, font: pg.font.Font, color: pg.Color, hover_color : pg.Color, click_color : pg.Color, anti: bool = False) -> None:
        super().__init__(text, font, color, anti)
        self.hover_color = hover_color
        self.click_color = click_color
        self.hover = False
        self.click = False
        self.hover_surface = font.render(self.text, self.anti, self.hover_color)
        self.click_surface = font.render(self.text, self.anti, self.click_color)
        self.function = None
        self.argument = None # usually a state
    def assign_func(self, func, arg) -> None:
        self.function = func
        self.argument = arg
    def execute_function(self) -> None:
        if self.argument == None:
            self.function()
        else:
            self.function(self.argument)
    def handle_event(self, event : pg.event.Event) -> None:
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if not self.click and self.get_box().collidepoint(event.pos):
                    self.click = True
                    self.queue_render()
            case pg.MOUSEBUTTONUP:
                if self.click:
                    self.click = False
                    self.hover = False
                    self.execute_function()
            case pg.MOUSEMOTION:
                if self.get_box().collidepoint(event.pos):
                    self.hover = True
                    self.queue_render()
                elif self.hover:
                    self.hover = False
                    self.queue_render()
            case _:
                pass
    def draw(self, surface : pg.Surface) -> None:
        if self.do_render:
            if self.click:
                surface.blit(self.click_surface, (self.x, self.y))
            elif self.hover:
                surface.blit(self.hover_surface, (self.x, self.y))
            else:
                surface.blit(self.surface, (self.x, self.y))
            self.do_render = False
