from modules.objs.gameobject import GameObject
import pygame as pg


class Container(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.children = []

    def update(self) -> list[pg.Rect]:
        if self.dirty:
            rect_list = []
            for obj in self.children:
                rect = obj.update()
                if rect:
                    rect_list.extend(rect)
            print(rect_list)
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
        super().add_to(arr)
        for obj in self.children:
            obj.set_dirty()
