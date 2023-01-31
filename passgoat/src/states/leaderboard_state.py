from state_container import StateContainer
from game_objects.text_label import TextLabel
from game_objects.button_label import ButtonLabel
from helpers.font import Fonts
from helpers.colors import Colors

class LeaderboardState(StateContainer):
    def __init__(self) -> None:
        super().__init__()
        leaderboard_label = TextLabel(Fonts.LARGE, 'SCORES', Colors.BLACK)
        leaderboard_label.center(do_x=True).move_to(y=40)
        
        to_title_button = ButtonLabel(Fonts.BIG, 'Back to Title', Colors.RED, Colors.BLACK, Colors.BLUE, self.placeholder, None)
        to_title_button.center(do_x=True).move_to(y=240)
        
        self.children.append(leaderboard_label)
        self.children.append(to_title_button)