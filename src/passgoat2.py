'''
Alex Liu
2023-02-03

number guessing game with pygame

for R.Y
'''

import pygame as pg
from modules.containers.ingame import InGame
from modules.containers.options import Options
from modules.containers.pause import Pause
from modules.containers.scores import Scores
from modules.containers.title import Title
from modules.containers.end import End
from modules.game_states import GameStates as GS
import modules.color as Color
from modules.data import GameData
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


class Passgoat:
    def __init__(self) -> None:
        self.SIZE = 600, 400
        pg.display.init()
        pg.font.init()
        self.surface = pg.display.set_mode(self.SIZE, pg.HIDDEN)
        self.register_events()
        self.data = GameData()
        self.decorate_window()
        self.state = GS.TITLE
        self.clock = pg.time.Clock()
        self.alive_objs = []
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
             pg.KEYUP,
             pg.KEYDOWN,
             pg.WINDOWMOVED,
             pg.WINDOWMINIMIZED
             )
        )

    def change_state(self, state: GS):
        self.state = state
        self.state_init = False

    def decorate_window(self):
        pg.display.set_icon(self.data.get_image('icon'))
        pg.display.set_caption('Passgoat', 'goat')

    def create_objs(self):
        self.objs = {}
        self.objs['title'] = Title(self.data, self.change_state, self.quit_game)
        self.objs['options'] = Options(self.data, self.change_state)
        self.objs['ingame'] = InGame(self.data, self.change_state)
        self.objs['pause'] = Pause(self.data, self.change_state)
        self.objs['scores'] = Scores(self.data, self.change_state)
        self.objs['end'] = End(self.data, self.change_state)

    def handle_events(self):
        for event in pg.event.get():
            #print(event)
            match event.type:
                case pg.QUIT:
                    self.quit_game()
            for obj in self.alive_objs:
                obj.handle_event(event)
    def quit_game(self):
        self.data.save_data()
        pg.quit()
        sys.exit()
    def update(self):
        if not self.state_init:
            self.alive_objs.clear()
            self.dirty_rects.append(self.surface.get_rect())
            self.state_init = True
            match self.state:
                case GS.TITLE:
                    self.objs['title'].add_to(self.alive_objs)
                case GS.OPTIONS:
                    self.objs['options'].add_to(self.alive_objs)
                case GS.INGAME:
                    self.objs['ingame'].add_to(self.alive_objs)
                case GS.PAUSE:
                    self.objs['pause'].add_to(self.alive_objs)
                case GS.END:
                    self.objs['end'].add_to(self.alive_objs)
                case GS.SCORES:
                    self.objs['scores'].add_to(self.alive_objs)
        for obj in self.alive_objs:
            rect_list = obj.update()
            if rect_list:
                self.dirty_rects.extend(rect_list)

    def draw(self):
        self.surface.fill(Color.WHITE)
        for obj in self.alive_objs:
            obj.draw(self.surface)
        pg.display.update(self.dirty_rects)
        self.clock.tick_busy_loop(690)
        self.dirty_rects.clear()

    def run(self):
        self.surface = pg.display.set_mode(self.SIZE)
        while 1:
            self.handle_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Passgoat()
    game.run()
