import pygame as pg


class GameObject:
    def __init__(self) -> None:
        self.dirty = False

    def reset(self) -> None:
        pass

    def handle_event(self, event: pg.event.Event) -> bool:
        pass

    def update(self) -> list[pg.Rect]:
        pass

    def draw(self, surface: pg.Surface) -> None:
        pass
    
    def set_dirty(self, val: bool = True) -> None:
        self.dirty = val
