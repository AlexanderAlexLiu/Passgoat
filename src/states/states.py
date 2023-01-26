from enum import Enum

class GameStates(Enum):
    '''
    class to increase readability of if statements for game states
    '''
    TITLE = 0
    IN_GAME = 1
    PAUSE = 2
    GAME_OVER = 3
    SETTINGS = 4
    HIGH_SCORES = 5
