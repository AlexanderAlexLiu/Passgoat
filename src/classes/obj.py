'''
Alex Liu
2023-01-26
The base class for everything shown in Passgoat

Notes:
TAILORED TO PASSGOAT, DOES NOT INCLUDE ALL IDEAL THINGS FOR A GAME OBJECT
- have to have a position to be shown somewhere <
- have to have a bounding box to be shown too (with the surface) <
- have to have a surface to be shown <
- implements dirty rectangles <
- will draw itself on a given surface <
- can be moved <
- handles events <
- can be updated <
'''

from pygame import Rect, Surface
from pygame.event import Event


class GameObject:

    def __init__(self) -> None:
        # numerical values
        self.__x, self.__y, self.__w, self.__h = 0, 0, 0, 0
        self.__prev_rect, self.__next_rect = Rect(0, 0, 0, 0), Rect(0, 0, 0, 0)
        self.__surface = Surface((0, 0))
        # flag to draw
        self.__render = False

    def move_to(self, x: float = None, y: float = None) -> None:
        '''
        moves whatever object to the location
        '''
        if x != None:
            self.__x = x
        if y != None:
            self.__y = y
        self.__next_rect.move(self.__x, self.__y)
        self.__render = True

    def handle_event(self, event: Event):
        '''
        handle whatever pygame event object given to the object, by defualt doesn't handle anything
        will set the __render flag
        '''
        '''
        match event.type:
            case _:
                pass
        '''
        pass

    def tick(self) -> Rect | None:
        '''
        any tick of any object should be entirely independent with no parameters
        also can set the __render flag in the code somewhere
        '''
        if self.__render:
            union = self.__next_rect.union(self.__prev_rect)
            self.__prev_rect = self.__next_rect 
            return union
        return None

    def render(self, surface: Surface) -> None:
        '''
        try not to override render too much because it should always remain the same
        '''
        if self.__render:
            surface.blit(self.__surface, (0, 0))
            self.__render = False  # sets the flag so the object doesn't render again
