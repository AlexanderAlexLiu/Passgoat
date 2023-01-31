from button_label import ButtonLabel
from text_label import TextLabel
from toggle_label import ToggleLabel
from colors import Colors
class GameManager:
    def __init__(self, font_dict : dict) -> None:
        self.guess = [None, None, None, None]
        self.locked_slots = [0, 0, 0, 0]
        self.font_dict = font_dict
        self.answer = [None, None, None, None]
        self.guess_label = TextLabel(self.font_dict[1], '_ _ _ _', Colors.RED)
        self.show_history = False
        self.numbers = [ToggleLabel(self.font_dict[0], '{}'.format(i), Colors.BLACK, Colors.BLUE, Colors.ORANGE, Colors.RED) for i in range(10)]