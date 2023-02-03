'''
Alex Liu
2023-02-03

number guessing game with pg

for R.Y.
'''

from modules.data import GameData as gd
from modules.game_states import GameStates as gs
from modules.colors import Colors as col
import pygame as pg
from modules.objs.image import Image
from modules.objs.button import Button
from modules.objs.textlabel import TextLabel
from modules.objs.colorgroups import ColorGroup
import sys

class Passgoat:
    def __init__(self) -> None:
        self.SIZE = (600, 400)
        pg.display.init()
        pg.font.init()
        self.surface = pg.display.set_mode(self.SIZE, pg.HIDDEN)
        self.register_events()
        self.data = gd()
        self.decorate_window()
        self.state = gs.TITLE
        self.clock = pg.time.Clock()
        self.screen_objs = []
        self.dirty_rects = []
        self.create_objs()
        self.state_init = False
    def register_events(self) -> None:
        pg.event.set_blocked(None)
        pg.event.set_allowed(
            (pg.QUIT,
            pg.MOUSEBUTTONUP,
            pg.MOUSEBUTTONDOWN,
            pg.MOUSEMOTION,
            pg.KEYDOWN,
            pg.KEYUP,
            pg.WINDOWMOVED,
            pg.WINDOWMINIMIZED)
        )
    def quit_game(self) -> None:
        pg.quit()
        sys.exit()
    def decorate_window(self) -> None:
        pg.display.set_icon(self.data.get_image('icon'))
        pg.display.set_caption('Passgoat', 'goat')
    def create_objs(self) -> None:
        self.objs = {}
        # TITLE
        a = TextLabel('PASSGOAT', self.data.get_font(4), ColorGroup.LABEL)
        a.center(x=True).move_to(y=40)
        b = TextLabel('mehhhhhhhhhhh', self.data.get_font(1), ColorGroup.CAPTION)
        b.center(x=True).move_to(y=100)
        c = Image(self.data.get_image('goat'))
        c.move_to(-30, 280)
        d = Button('Play', self.data.get_font(2), ColorGroup.BUTTON, self.change_state, gs.INGAME)
        d.center(x=True).move_to(y=200)
        e = Button('Options', self.data.get_font(2), ColorGroup.BUTTON, self.change_state, gs.OPTIONS)
        e.center(x=True).move_to(y=240)
        f = Button('Quit', self.data.get_font(2), ColorGroup.BUTTON_LESSER, self.quit_game)
        f.center(x=True).move_to(y=280)
        self.objs['title.label'] = a
        self.objs['title.caption'] = b
        self.objs['title.goat'] = c
        self.objs['title.play'] = d
        self.objs['title.options'] = e
        self.objs['title.quit'] = f
        # OPTIONS
        a = TextLabel('OPTIONS', self.data.get_font(3), ColorGroup.LABEL)
        a.center(x=True).move_to(y=40)
        self.objs['options.label'] = a
        # INGAME
        a = TextLabel('3', self.data.get_font(3), ColorGroup.LABEL)
        a.center(x=True).move_to(y=40)
        self.objs['ingame.label'] = a
        # PAUSE
        a = TextLabel('PAUSE', self.data.get_font(3), ColorGroup.LABEL)
        a.center(x=True).move_to(y=40)
        self.objs['pause.label'] = a
        # END
        a = TextLabel('GAME OVER', self.data.get_font(3), ColorGroup.LABEL)
        a.center(x=True).move_to(y=40)
        self.objs['end.label'] = a
        # SCORES
        a = TextLabel('SCORES', self.data.get_font(3), ColorGroup.LABEL)
        a.center(x=True).move_to(y=40)
        self.objs['scores.label'] = a
    def handle_events(self) -> None:
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                self.data.save_data()
                self.quit_game()
            elif event.type == pg.KEYDOWN:
                if event.key == 96:
                    if self.state == gs.TITLE:
                        self.change_state(gs.OPTIONS)
                    elif self.state == gs.OPTIONS:
                        self.change_state(gs.INGAME)
                    elif self.state == gs.INGAME:
                        self.change_state(gs.PAUSE)
                    elif self.state == gs.PAUSE:
                        self.change_state(gs.END)
                    elif self.state == gs.END:
                        self.change_state(gs.SCORES)
                    elif self.state == gs.SCORES:
                        self.change_state(gs.TITLE)
            for obj in self.screen_objs:
                obj.handle_event(event)
    def change_state(self, state : gs):
        self.state = state
        self.state_init = False
    def update(self) -> None:
        if not self.state_init:
            self.screen_objs.clear()
            self.dirty_rects.append(self.surface.get_rect())
            self.state_init = True
            match self.state:
                case gs.TITLE:
                    self.objs['title.label'].add_to(self.screen_objs)
                    self.objs['title.caption'].add_to(self.screen_objs)
                    self.objs['title.goat'].add_to(self.screen_objs)
                    self.objs['title.play'].add_to(self.screen_objs)
                    self.objs['title.options'].add_to(self.screen_objs)
                    self.objs['title.quit'].add_to(self.screen_objs)
                case gs.OPTIONS:
                    self.objs['options.label'].add_to(self.screen_objs)
                case gs.INGAME:
                    self.objs['ingame.label'].add_to(self.screen_objs)
                case gs.PAUSE:
                    self.objs['pause.label'].add_to(self.screen_objs)
                case gs.END:
                    self.objs['end.label'].add_to(self.screen_objs)
                case gs.SCORES:
                    self.objs['scores.label'].add_to(self.screen_objs)
        #print(self.clock.get_fps())
        for obj in self.screen_objs:
            rect_list = obj.update()
            if rect_list:
                self.dirty_rects.extend(rect_list)
    def draw(self) -> None:
        self.surface.fill(col.WHITE)
        for obj in self.screen_objs:
            obj.draw(self.surface)
        pg.display.update(self.dirty_rects)
        self.clock.tick_busy_loop(420)
        self.dirty_rects.clear()
    def run(self) -> None:
        # display when the game is ready
        self.surface = pg.display.set_mode(self.SIZE, pg.SHOWN)
        while 1:
            self.handle_events()
            self.update()
            self.draw()
if __name__ == '__main__':
    game = Passgoat()
    game.run()