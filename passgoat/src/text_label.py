from pygame import Surface, Color
from pygame.font import Font
from pygame.event import Event
from pygame import Rect

ALIAS = True

class TextLabel:
    def __init__(self, font: Font, text: str = '', color: Color = (0, 0, 0)) -> None:
        self.x, self.y = 0, 0
        self.font, self.text, self.color = font, text, color
        self.surface = self.font.render(self.text, ALIAS, self.color)
        self.rect = self.surface.get_rect()
        self.old_rect = self.rect
        # straight up misinformation, this dictates if the textlabel should update too (sometimes)
        self.do_render = False

    def set_text(self, text: str = ''):
        self.text = text
        self.surface = self.font.render(self.text, ALIAS, self.color)
        self.old_rect = self.rect.copy()
        self.rect.width, self.rect.height = self.surface.get_size()
    
    def center(self, do_x : bool = False, do_y : bool = False) -> None:
        if do_x:
            self.move_to(x = (600 - self.rect.w) / 2)
        if do_y:
            self.move_to(y = (400 - self.rect.h) / 2)

    def move_to(self, x: float = None, y: float = None) -> None:
        # didn't use if not x because 0 will trigger not
        self.old_rect = self.rect.copy()
        if x != None:
            self.rect.x = x
        if y != None:
            self.rect.y = y
    
    def move_by(self, x : float = None, y : float = None) -> None:
        self.old_rect = self.rect.copy()
        if x != None:
            self.rect.x+=x
        if y != None:
            self.rect.y+=y

    def handle_event(self, event: Event) -> None:
        pass

    def update(self) -> list[Rect] | None:
        '''
        this will update self.do_render but will also obey by self.do_render (sometimes?)
        '''
        if self.do_render:
            return [self.rect, self.old_rect]

    def render(self, surface: Surface):
        if self.do_render:
            print('DRAWING: {}'.format(self))
            surface.blit(self.surface, (self.rect.x, self.rect.y))
            self.do_render = False

    def wake(self) -> None:
        self.do_render = True
    
    def add_to(self, active_objects : list) -> None:
        self.wake()
        active_objects.append(self)
