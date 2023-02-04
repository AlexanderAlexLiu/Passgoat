from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.toggle import Toggle
from modules.objs.textlabel import TextLabel
from modules.objs.counter import Counter
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates

class Scores(Container):
    def __init__(self, data : GameData, change_state : Callable) -> None:
        super().__init__()
        self.pause_label = TextLabel('Pause', data.get_font(3), ColorGroups.LABEL).center(x=True).move(y=40)
        self.resume_button = Button('Resume', data.get_font(2), ColorGroups.BUTTON, change_state, GameStates.INGAME).center(x=True).move(y=150)
        self.quit_button = Button('Quit', data.get_font(2), ColorGroups.BUTTON_LESSER, change_state, GameStates.TITLE).center(x=True).move(y=280)
        self.children.extend((self.pause_label, self.resume_button, self.quit_button))