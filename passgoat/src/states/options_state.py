from state_container import StateContainer
from game_objects.text_label import TextLabel
from game_objects.button_label import ButtonLabel
from helpers.font import Fonts
from helpers.colors import Colors

class OptionsState(StateContainer):
    def __init__(self) -> None:
        super().__init__()
        options_label = TextLabel(Fonts.LARGE, 'OPTIONS', Colors.BLACK)
        options_label.center(do_x=True).move_to(y=40)
        
        delete_scores_button = ButtonLabel(Fonts.BIG, 'Delete Scores', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        delete_scores_button.center(do_x=True).move_to(y=200)
        
        to_title_button = ButtonLabel(Fonts.BIG, 'Back to Title', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        to_title_button.center(do_x=True).move_to(y=240)
        
        self.children.append(options_label)
        self.children.append(delete_scores_button)
        self.children.append(to_title_button)