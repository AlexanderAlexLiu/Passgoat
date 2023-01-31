from pygame import Surface, Rect
from pygame.event import Event
class GameObject:
    def __init__(self) -> None:
        '''
        a useless class, almost all code in the class just shows general implementation
        for child classes
        '''
        self.__render = False
        self.__surf = Surface((0, 0))
        self.__rect = self.__surf.get_rect()
        self.__old_rect = self.__rect.copy()
    def handle_event(self, event : Event) -> None:
        pass
    def update(self) -> list[Rect] | None:
        if self.__render:
            return [self.__old_rect, self.rect]
    def render(self, surf : Surface) -> None:
        if self.__render:
            # self.__rect.topleft is equivalent to (self.__rect.x, self.__rect.y)
            surf.blit(self.__surf, (self.__rect.topleft))
            # old rectangle is updated to new rectangle's spot because at this point, it should've been cleaned
            self.__old_rect = self.__rect.copy()
            self.__render = False
    def wake(self) -> None:
        self.__render = True


g = GameObject()
