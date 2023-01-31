from button_label import ButtonLabel
from text_label import TextLabel
from toggle_label import ToggleLabel
from colors import Colors
from pygame import Rect, Surface
import pygame as pg
from pygame.event import Event
'''
List of numbers to cross out -> A bunch of toggle buttons
Ghost numbers (lock feature?) -> ghost numbers will be replaced with any input, lock with double click?
| lock means that the number will automatically be placed there
| maximum of 3 locks (why tf would you want 4?)
different difficulties:
	5 numbers (one of each) -> oh my god I want to jump
	anything beyond (repeated numbers ok) -> jesus christ I want to jump
minutes, hours... -> pass in clock object to the game
scroll with mouse pwease uwu -> mouse scroll event on game
personal record? -> uhh leaderboard? how to sort?
reset history placement	-> this should be done in reset()
number of guesses to solve - shown at end -> easy clap
Fix description -> done in cx_freeze
'''

class GameManager:
    DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    def __init__(self, font_dict : dict) -> None:
        self.font = font_dict
        self.rect_list = [] # list of rectangles to pass to the upper render() function once all the sub components have been updated
        self.number_toggles = [ToggleLabel(self.font[1], str(i), Colors.BLACK, Colors.CYAN, Colors.ORANGE, Colors.RED) for i in range(10)]
        self.components = []
        self.guess_label = TextLabel(self.font[-1], '_ _ _ _', Colors.BLACK)
        #self.guess_label.center(do_x=True)
        self.guess = []
        self.answer_label = TextLabel(self.font[3], '_ _ _ _ _ _ _ _ _ _', Colors.BLACK)
        self.answer_label.center(do_x=True)
        self.answer_label.move_to(y=40)
        self.answer_label.add_to(self.components)
        self.guess_label.add_to(self.components)
        for i in range(10):
            self.number_toggles[i].move_to(200, 250)
            self.number_toggles[i].move_by(20*i)
            self.number_toggles[i].add_to(self.components)
    
    def start(self, digits : int):
        self.guess_slots = [ButtonLabel(self.font[2], '_', Colors.BLACK, Colors.RED, Colors.CYAN)]
        
    def handle_event(self, event: Event) -> None:
        match event.type:
            case pg.KEYDOWN:
                if event.unicode in GameManager.DIGITS:
                    self.guess.append(event.unicode)
                    self.guess_label.wake()
        for obj in self.components:
            obj.handle_event(event)
    def update(self) -> list[Rect] | None:
        '''
        this will update self.do_render but will also obey by self.do_render (sometimes?)
        '''
        rect_list = []
        self.guess_label.set_text(''.join(self.guess))
        for obj in self.components:
            rects = obj.update()
            if rects:
                rect_list.extend(rects)
        return rect_list

    def render(self, surface: Surface):
        for obj in self.components:
            obj.render(surface)

    def add_to(self, active_objects: list) -> None:
        '''
        change so it appends whatever it needs to the list'''
        active_objects.append(self)
