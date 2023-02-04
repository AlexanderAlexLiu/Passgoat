from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.toggle import Toggle
from modules.objs.textlabel import TextLabel
from modules.objs.counter import Counter
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates

class Options(Container):
    def __init__(self, data : GameData, change_state : Callable) -> None:
        super().__init__()
        self.data = data
        self.options_label = TextLabel('Options', data.get_font(3), ColorGroups.LABEL).center(x=True).move(y=40)
        self.hard_button = Toggle('Hard Mode', data.get_font(2), ColorGroups.TOGGLE).center(x=True).move(y=120)
        self.hard_button.set_toggle(self.data.get_setting('hard'))
        self.number_count = Counter('Number Count', data.get_font(2), ColorGroups.BUTTON, 4, 10).move(200, 170)
        self.number_count.set_count(self.data.get_setting('mode'))
        self.delete_button = Button('Wipe Scores', data.get_font(2), ColorGroups.BUTTON, self.clear_scores).center(x=True).move(y=220)
        self.save_button = Button('Save', data.get_font(2), ColorGroups.BUTTON_LESSER, self.save, change_state).center(x=True).move(y=300)
        self.children.extend((self.options_label, self.hard_button, self.number_count, self.delete_button, self.save_button))
    def save(self, change_state : Callable):
        self.data.set_setting('mode', self.number_count.get_count())
        self.data.set_setting('hard', self.hard_button.get_toggle()) 
        change_state(GameStates.TITLE)
    def clear_scores(self):
        self.data.get_setting('scores').clear()