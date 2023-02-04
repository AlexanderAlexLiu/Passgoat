from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.toggle import Toggle
from modules.objs.textlabel import TextLabel
from modules.objs.counter import Counter
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates
import pygame as pg

class InGame(Container):
    def __init__(self, data : GameData, change_state : Callable) -> None:
        super().__init__()
        self.change_state = change_state
        self.pause_label = TextLabel('INGAME', data.get_font(3), ColorGroups.LABEL).center(x=True).move(y=40)
        self.children.extend((self.pause_label,))
    def handle_event(self, event: pg.event.Event) -> None:
        match event.type:
            case pg.WINDOWMOVED | pg.WINDOWMINIMIZED:
                self.change_state(GameStates.PAUSE)
            case pg.KEYDOWN:
                if event.key == 27:
                    self.change_state(GameStates.PAUSE)
        return super().handle_event(event)