from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.toggle import Toggle
from modules.objs.textlabel import TextLabel
from modules.objs.counter import Counter
import modules.objs.colorgroups as ColorGroups
from modules.objs.particle import Particle
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates
import random
import pygame as pg
class End(Container):
    def __init__(self, data : GameData, change_state : Callable, clock : pg.time.Clock) -> None:
        super().__init__()
        self.clock = clock
        self.answer_label = TextLabel('', data.get_font(3), ColorGroups.LABEL).center(x=True).move(y=40)
        self.guesses_label = TextLabel('', data.get_font(2), ColorGroups.LABEL).center(x=True).move(y=100)
        self.continue_button = Button('Continue', data.get_font(2), ColorGroups.BUTTON_LESSER, change_state, GameStates.SCORES).center(x=True).move(y=280)
        self.children.extend((self.answer_label, self.continue_button, self.guesses_label))
    def set_result(self, ans : list[str], guesses : int) -> None:
        self.particles = [Particle(random.randint(100, 700), random.randint(-400, -10), self.clock) for  i in range(200)]
        self.answer_label.set_text(' '.join(ans)).center(x=True)
        self.guesses_label.set_text(f'GOT IN {guesses} GUESSES!').center(x=True)
        self.children.clear()
        self.children.extend((self.answer_label, self.continue_button, self.guesses_label))
        self.children.extend(self.particles)
    def update(self) -> list[pg.Rect]:
        rect_list = []
        for obj in self.children:
            obj.set_dirty()
            rect = obj.update()
            rect_list.extend(rect)
        self.set_dirty()
        return rect_list