'''
Alex Liu
2023-01-26
Class for any text label in passgoat
'''
from pygame.font import Font
from pygame.color import Color
from obj import GameObject

class TextLabel(GameObject):
    def __init__(self, text : str, font : Font, color : Color, anti_alias : bool = False) -> None:
        super().__init__()
        self.__text, self.__font, self.__color, self.__anti_alias = text, font, color, anti_alias
        self.__surface = self.__font.render(self.__text, self.__anti_alias, self.__color)
        rect = self.__surface.get_rect()
        self.__w, self.__h = rect.size()
        self.__prev_rect, self.__next_rect = rect, rect

    def center(self, on_x : bool = False, on_y : bool = False) -> None:
        # 600 and 400 are hardcoded values for window height and width
        self.move_to((600 - self.__w) / 2 if on_x else None, (400 - self.__h) / 2 if on_y else None)
    
    def set_text(self, new_text : str) -> None:
        self.__text = new_text
        self.__surface = self.__font.render(self.__text, self.__anti_alias, self.__color)
        rect = self.__surface.get_rect()
        self.__w, self.__h = rect.size()
        self.__next_rect = rect
        self.__render = True # assume it needs to change