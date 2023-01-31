'''
Alex Liu
2023-01-31

State class to clean up main code readability
'''

from enum import Enum

class GameState(Enum):
    '''
    simple enumerator to improve readability in main code of game
    '''
    TITLE = 0
    OPTIONS = 1
    INGAME = 2
    PAUSE = 3
    GAMEOVER = 4
    LEADERBOARD = 5