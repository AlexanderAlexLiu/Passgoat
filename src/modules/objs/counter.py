from __future__ import annotations
from modules.objs.button import Button
import pygame as pg
from typing import Callable

class Counter(Button):
    def __init__(self, text: str, font: pg.font.Font, colors: tuple[tuple], lower: int, upper: int, called : Callable) -> None:
        super().__init__(text, font, colors)
        self.lower, self.upper = lower, upper
        self.count = self.lower
        self.label = self.text
        self.func = self.increase
        self.called = called

    def move(self, x: float = None, y: float = None) -> Counter:
        super().move(x, y)
        return self

    def center(self, x: bool = False, y: bool = False) -> Counter:
        super().center(x, y)
        return self

    def increase(self) -> None:
        self.count += 1
        if self.count > self.upper:
            self.count = self.lower
        self.set_text(f'{self.label} : {self.count}')
        self.called()

    def get_count(self) -> int:
        return self.count

    def set_count(self, count: int) -> Counter:
        if self.lower <= count <= self.upper:
            self.count = count
            self.set_text(f'{self.label} : {self.count}')
        return self
