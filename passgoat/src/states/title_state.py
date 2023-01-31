from states.state_container import StateContainer
from game_objects.text_label import TextLabel
from game_objects.button_label import ButtonLabel
from helpers.font import Fonts
from helpers.colors import Colors

class TitleState(StateContainer):
    def __init__(self) -> None:
        super().__init__()
        title_label = TextLabel(Fonts.LARGE, 'PASSGOAT', Colors.BLACK)
        title_label.center(do_x=True).move_to(y=40)
        title_caption = TextLabel(Fonts.SMALL, 'mehhhhhhhhhhhh', Colors.BLACK)
        title_caption.center(do_x=True).move_to(y=100)
        play_button = ButtonLabel(Fonts.BIG, 'Play', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        play_button.center(do_x=True).move_to(y=200)
        options_button = ButtonLabel(Fonts.BIG, 'Options', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        options_button.center(do_x=True).move_to(y=240)
        self.children.append(title_label)
        self.children.append(title_caption)
        self.children.append(play_button)
        self.children.append(options_button)