from enum import Enum


class GameStates(Enum):
    TITLE = 0
    OPTIONS = 1
    INGAME = 2
    PAUSE = 3
    END = 4
    SCORES = 5
