from pygame.time import Clock
from states import GameStates
class GameManager:
    def __init__(self) -> None:
        self.clock = Clock()
        self.active_objects = []
        self.dirty_rects = []
        self.debug = False
        self.state = GameStates.TITLE
    