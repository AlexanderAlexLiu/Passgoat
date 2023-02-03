from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.image import Image
from modules.objs.textlabel import TextLabel
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates

class Title(Container):
    def __init__(self, data : GameData, change_state : Callable) -> None:
        super().__init__()
        title_label = TextLabel('PASSGOAT', data.get_font(4), ColorGroups.LABEL).center(x=True).move(y=40)
        title_caption = TextLabel('mehhhhhhhhh', data.get_font(1), ColorGroups.CAPTION).center(x=True).move(100)
        goat_pic = Image(data.get_image('goat')).move(-30, 280)
        # CHANGE THIS TO RESET THE GAME
        play_button = Button('Play', data.get_font(2), ColorGroups.BUTTON, change_state, GameStates.INGAME).center(x=True).move(y=200)
        options_button = Button('Options', data.get_font(2), ColorGroups.BUTTON, change_state, GameStates.OPTIONS).center(x=True).move(y=240)
        self.children.extend((title_label, title_caption, play_button, options_button, goat_pic))