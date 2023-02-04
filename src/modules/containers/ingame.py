from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.toggle import Toggle
from modules.objs.textlabel import TextLabel
from modules.objs.counter import Counter
from modules.objs.specialbutton import SpecialButton
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates
import random
import pygame as pg

class InGame(Container):
    DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    def __init__(self, data : GameData, change_state : Callable) -> None:
        super().__init__()
        self.data, self.change_state = data, change_state
        self.answer_label = TextLabel('', self.data.get_font(3), ColorGroups.LABEL)
        self.number_tickers = [Toggle(str(i), self.data.get_font(2), ColorGroups.TICKER) for i in range(10)]
        self.move_tickers()
    def reset_game(self) -> None:
        self.hard, self.mode = self.data.get_setting('hard'), self.data.get_setting('mode')
        self.answer = []
        text = SpecialButton('_', self.data.get_font(2), ColorGroups.SPECIAL)
        self.guess = []
        self.guess_buttons = []
        self.children.clear()
        if not self.hard:
            self.children.extend(self.number_tickers)
        self.children.append(self.answer_label)
        self.children.append(text)
        self.reset_tickers()
        self.answer_label.set_text(' '.join('_' for i in range(self.data.get_setting('mode'))))
        self.move_answer_label()
    def move_answer_label(self) -> None:
        self.answer_label.center(x=True).move(y=40)
    def handle_event(self, event: pg.event.Event) -> None:
        super().handle_event(event)
        match event.type:
            case pg.KEYDOWN:
                if event.key == 27:
                    self.change_state(GameStates.PAUSE)
            case pg.WINDOWMOVED | pg.WINDOWMINIMIZED:
                self.change_state(GameStates.PAUSE)
    def reset_tickers(self) -> None:
        for ticker in self.number_tickers:
            ticker.set_toggle(False)
    def move_tickers(self) -> None:
        ticker_width = self.number_tickers[0].rect.w
        ticker_spacing = 10
        tickers_width = ticker_width * 10 + ticker_spacing * 9
        tickers_start_x = (800 - tickers_width) / 2
        tickers_y = 300
        for i, ticker in enumerate(self.number_tickers):
            ticker.move(x=tickers_start_x+(ticker_width+ticker_spacing)*i, y=tickers_y)