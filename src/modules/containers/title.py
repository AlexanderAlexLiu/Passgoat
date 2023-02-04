from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.image import Image
from modules.objs.textlabel import TextLabel
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates

class Title(Container):
    def __init__(self, data : GameData, change_state : Callable, quit_game : Callable, start_game : Callable) -> None:
        super().__init__()
        self.title_label = TextLabel('PASSGOAT', data.get_font(4), ColorGroups.LABEL).center(x=True).move(y=40)
        self.title_caption = TextLabel('mehhhhhhhhh', data.get_font(1), ColorGroups.CAPTION).center(x=True).move(y=100)
        self.goat_pic = Image(data.get_image('goat')).move(-30, 280)
        self.play_button = Button('Play', data.get_font(2), ColorGroups.BUTTON, start_game).center(x=True).move(y=200)
        self.options_button = Button('Options', data.get_font(2), ColorGroups.BUTTON, change_state, GameStates.OPTIONS).center(x=True).move(y=240)
        self.quit_button = Button('Quit', data.get_font(2), ColorGroups.BUTTON_LESSER, quit_game).center(x=True).move(y=280)
        self.children.extend((self.title_label, self.title_caption, self.play_button, self.options_button, self.quit_button, self.goat_pic))