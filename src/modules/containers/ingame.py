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
        self.number_tickers = [Toggle(str(i), self.data.get_font(0), ColorGroups.TOGGLE) for i in range(10)]
        self.move_tickers()
        self.children.append(self.answer_label)
        self.children.extend(self.number_tickers)
    def move_tickers(self) -> None:
        ticker_width = self.number_tickers[0].rect.w
        ticker_height = self.number_tickers[0].rect.h
        ticker_spacing = 10
        tickers_width = ticker_width * 10 + ticker_spacing * 9
        tickers_start_x = (600 - tickers_width) / 2
        tickers_y = 390 - ticker_height
        for i, ticker in enumerate(self.number_tickers):
            ticker.move(x=tickers_start_x+(tickers_width+ticker_spacing)*i, y=tickers_y)