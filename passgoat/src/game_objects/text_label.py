from __future__ import annotations
from pygame import Surface, Color, Rect
from pygame.font import Font
from pygame.event import Event

ALIAS = True

class TextLabel:
    def __init__(self, font: Font, text: str, color: Color) -> None:
        self.font, self.text, self.color = font, text, color
        self.surface = self.font.render(self.text, ALIAS, self.color)
        self.rect = self.surface.get_rect()
        self.old_rect = self.rect
        self.do_render = False

    def set_text(self, text: str = '') -> TextLabel:
        self.text = text
        self.surface = self.font.render(self.text, ALIAS, self.color)
        self.old_rect = self.rect.copy()
        self.rect.width, self.rect.height = self.surface.get_size()
        return self

    def center(self, do_x: bool = False, do_y: bool = False) -> TextLabel:
        if do_x:
            self.move_to(x=(600 - self.rect.w) / 2)
        if do_y:
            self.move_to(y=(400 - self.rect.h) / 2)
        return self

    def move_to(self, x: float = None, y: float = None) -> TextLabel:
        # didn't use if not x because 0 will trigger not
        self.old_rect = self.rect.copy()
        if x != None:
            self.rect.x = x
        if y != None:
            self.rect.y = y
        return self

    def move_by(self, x: float = None, y: float = None) -> TextLabel:
        self.old_rect = self.rect.copy()
        if x != None:
            self.rect.x += x
        if y != None:
            self.rect.y += y
        return self

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
            surface.blit(self.surface, (self.rect.x, self.rect.y))
            self.do_render = False
            self.old_rect = self.rect.copy()

    def wake(self) -> None:
        self.do_render = True

    def add_to(self, active_objects: list) -> None:
        self.wake()
        active_objects.append(self)
