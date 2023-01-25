import pygame as pg

class GameObject:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.w = 1
        self.h = 1
        self.surface = pg.Surface((self.w, self.h))
        self.surface.fill((255, 0, 0)) # fill with red
        self.do_render = True # everything will try to render once when created
    def queue_render(self):
        self.do_render = True
    def move_to(self, x : float = 0, y : float = 0) -> None:
        self.x = x
        self.y = y
    def set_y(self, y : float):
        self.y = y
    def set_x(self, x : float):
        self.x = x
    def get_box(self) -> pg.Rect:
        return self.surface.get_rect().move(self.x, self.y)
    def handle_event(self, event : pg.event.Event) -> None:
        match event.type:
            case _:
                return
    def update(self) -> list[pg.Rect]:
        if self.do_render:
            return self.get_box()
    def draw(self, surface : pg.Surface) -> None:
        if self.do_render:
            surface.blit(self.surface, (self.x, self.y))
            self.do_render = False
    def add_to(self, lst : list) -> None:
        lst.append(self)
        self.do_render = True