import pygame as pg


class GameObject:
    def __init__(self) -> None:
        self.dirty = False

    def handle_event(self, event: pg.event.Event) -> None:
        pass

    def update(self) -> list[pg.Rect]:
        pass

    def draw(self, surface : pg.Surface) -> None:
        print(f"DRAWING {self}")

    def add_to(self, arr: list) -> None:
        arr.append(self)
        self.dirty = True

    def set_dirty(self, val: bool = True) -> None:
        self.dirty = val
