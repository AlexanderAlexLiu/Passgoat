from state_container import StateContainer
from game_objects.text_label import TextLabel
from game_objects.button_label import ButtonLabel
from helpers.font import Fonts
from helpers.colors import Colors

class GameOverState(StateContainer):
    def __init__(self) -> None:
        super().__init__()
        pause_label = TextLabel(Fonts.LARGE, 'PAUSE', Colors.BLACK)
        pause_label.center(do_x=True).move_to(y=40)
        resume_button = ButtonLabel(Fonts.BIG, 'Resume', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        resume_button.center(do_x=True).move_to(y=200)
        quit_button = ButtonLabel(Fonts.BIG, 'Options', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        quit_button.center(do_x=True).move_to(y=240)
        self.children.append(pause_label)
        self.children.append(resume_button)
        self.children.append(quit_button)