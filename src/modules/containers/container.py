from modules.objs.gameobject import GameObject
import pygame as pg


class Container(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.children = []

    def update(self) -> list[pg.Rect]:
        rect_list = []
        for obj in self.children:
            rect = obj.update()
            if rect:
                rect_list.extend(rect)
        if rect_list:
            self.dirty = True
            return rect_list

    def draw(self, surface: pg.Surface) -> None:
        if self.dirty:
            for obj in self.children:
                obj.draw(surface)
            self.set_dirty(False)

    def handle_event(self, event: pg.event.Event) -> None:
        for obj in self.children:
            if obj.handle_event(event) and not self.dirty:
                self.dirty = True
    
    def add_to(self, arr: list) -> None:
        arr.append(self)
        for obj in self.children:
            obj.reset()
            obj.set_dirty()
        self.set_dirty()