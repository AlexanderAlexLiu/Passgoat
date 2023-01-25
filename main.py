'''
Alex Liu
2023-01-25
A number guessing game

For Rachel
'''
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
from src.asset_manager import AssetManager
from src.file_manager import FileManager
from src.states import GameStates
from src.text_label import TextLabel
from src.button import Button
from src.colors import Colors
from math import floor
ALIAS = True
class Game:
    def __init__(self) -> None:
        self.file_man = FileManager(__file__)
        pg.display.init()
        self.init_events()
        pg.font.init()
        self.WINDOW_SIZE = (600, 400)
        self.surface = pg.display.set_mode(self.WINDOW_SIZE)
        self.asset_man = AssetManager(__file__)
        self.decorate()
        self.clock = pg.time.Clock()
        self.run = True
        self.active_objects = []
        self.all_objects = {}
        self.update_list = []
        self.debug = False
        self.state = GameStates.TITLE
        self.state_load = False
        self.create_objects()
    def create_objects(self):
        self.all_objects['title'] = TextLabel('PASSGOAT', self.asset_man.get_font(4), Colors.RED, ALIAS)
        self.all_objects['title'].center_x()
        self.all_objects['title'].set_y(60)
        self.all_objects['caption'] = TextLabel('mehhhhhhhhhhhh', self.asset_man.get_font(1), Colors.BLUE, ALIAS)
        self.all_objects['caption'].center_x()
        self.all_objects['caption'].set_y(120)
        self.all_objects['play_button'] = Button('PLAY', self.asset_man.get_font(2), Colors.ORANGE, Colors.BLACK, Colors.RED, ALIAS)
        self.all_objects['play_button'].move_to(170, 250)
        self.all_objects['play_button'].assign_func(self.change_state, GameStates.IN_GAME)
        self.all_objects['settings_button'] = Button('OPTIONS', self.asset_man.get_font(2), Colors.ORANGE, Colors.BLACK, Colors.RED, ALIAS)
        self.all_objects['settings_button'].move_to(340, 250)
        self.all_objects['settings_button'].assign_func(self.change_state, GameStates.SETTINGS)
        self.all_objects['settings_title'] = TextLabel('SETTINGS', self.asset_man.get_font(4), Colors.BLACK, ALIAS)
        self.all_objects['settings_title'].center_x()
        self.all_objects['settings_title'].set_y(20)
        self.all_objects['pause'] = TextLabel('PAUSE', self.asset_man.get_font(4), Colors.RED, ALIAS)
        self.all_objects['pause'].center_x()
        self.all_objects['pause'].set_y(60)
        self.all_objects['exit'] = Button('EXIT', self.asset_man.get_font(2), Colors.GREEN, Colors.RED, Colors.BLACK, ALIAS)
        self.all_objects['exit'].center_x()
        self.all_objects['exit'].set_y(300)
        self.all_objects['exit'].assign_func(self.stop_run, None)
        self.all_objects['resume_button'] = Button('RESUME', self.asset_man.get_font(2), Colors.BLUE, Colors.GREEN, Colors.BLACK, ALIAS)
        self.all_objects['resume_button'].move_to(150, 250)
        self.all_objects['resume_button'].assign_func(self.change_state, GameStates.IN_GAME)
        self.all_objects['quit_button'] = Button('QUIT', self.asset_man.get_font(2), Colors.BLUE, Colors.RED, Colors.BLACK, ALIAS)
        self.all_objects['quit_button'].move_to(360, 250)
        self.all_objects['quit_button'].assign_func(self.change_state, GameStates.TITLE)
        # doesn't actually save, it was a scam
        self.all_objects['save_button'] = Button('SAVE', self.asset_man.get_font(2), Colors.CYAN, Colors.GREEN, Colors.BLACK, ALIAS)
        self.all_objects['save_button'].center_x()
        self.all_objects['save_button'].set_y(300)
        self.all_objects['save_button'].assign_func(self.change_state, GameStates.TITLE) # maybe a save settings thing
        self.all_objects['answer_placeholder'] = TextLabel('_ _ _ _', self.asset_man.get_font(4), Colors.RED, ALIAS)
        self.all_objects['answer_placeholder'].center_x()
        self.all_objects['answer_placeholder'].set_y(60)
        self.all_objects['return_to_title'] = Button('RETURN TO TITLE', self.asset_man.get_font(2), Colors.BLUE, Colors.RED, Colors.BLACK, ALIAS)
        self.all_objects['return_to_title'].center_x()
        self.all_objects['return_to_title'].set_y(300)
        self.all_objects['return_to_title'].assign_func(self.change_state, GameStates.TITLE)
        self.all_objects['continue'] = Button('CONTINUE', self.asset_man.get_font(2), Colors.GREEN, Colors.RED, Colors.BLACK, ALIAS)
        self.all_objects['continue'].center_x()
        self.all_objects['continue'].set_y(300)
        self.all_objects['continue'].assign_func(self.change_state, GameStates.HIGH_SCORES)

        self.all_objects['cheat'] = Button('cheat', self.asset_man.get_font(2), Colors.GREEN, Colors.RED, Colors.BLACK, ALIAS)
        self.all_objects['cheat'].center_x()
        self.all_objects['cheat'].set_y(200)
        self.all_objects['cheat'].assign_func(self.change_state, GameStates.GAME_OVER)
    def stop_run(self):
        self.run = False
    def decorate(self):
        pg.display.set_caption('Passgoat')
        pg.display.set_icon(self.asset_man.get_icon())
    def change_state(self, state):
        self.state_load = False
        from_state = self.state
        self.state = state
        print('FROM {} TO {}'.format(from_state, self.state))
    def init_events(self):
        '''
        configures allowed and blocked events so that the game can process things faster
        '''
        pg.event.set_blocked(None)
        pg.event.set_allowed((
            pg.KEYDOWN,
            pg.KEYUP,
            pg.QUIT,
            pg.MOUSEMOTION,
            pg.MOUSEWHEEL,
            pg.MOUSEBUTTONUP,
            pg.MOUSEBUTTONDOWN,
            pg.WINDOWFOCUSLOST,
            pg.WINDOWMOVED
        ))
    def handle_events(self):
        for event in pg.event.get():
            print(event)
            match event.type:
                case pg.QUIT:
                    self.run = False
                case pg.WINDOWMOVED:
                    if self.state == GameStates.IN_GAME:
                        self.change_state(GameStates.PAUSE)
                case pg.WINDOWFOCUSLOST:
                    if self.state == GameStates.IN_GAME:
                        self.change_state(GameStates.PAUSE)
                case pg.KEYDOWN:
                    if self.state == GameStates.IN_GAME:
                        if event.key == 27:
                            self.change_state(GameStates.PAUSE)
            for obj in self.active_objects:
                obj.handle_event(event)
    def update_logic(self):
        if not self.state_load:
            self.active_objects.clear()
            self.update_list.append(self.surface.get_rect())
            if self.state == GameStates.TITLE:
                self.all_objects['title'].add_to(self.active_objects)
                self.all_objects['caption'].add_to(self.active_objects)
                self.all_objects['play_button'].add_to(self.active_objects)
                self.all_objects['settings_button'].add_to(self.active_objects)
                self.all_objects['exit'].add_to(self.active_objects)
            elif self.state == GameStates.IN_GAME:
                self.all_objects['answer_placeholder'].add_to(self.active_objects)
                self.all_objects['cheat'].add_to(self.active_objects)
            elif self.state == GameStates.PAUSE:
                self.all_objects['pause'].add_to(self.active_objects)
                #TEST
                self.all_objects['quit_button'].add_to(self.active_objects)
                self.all_objects['resume_button'].add_to(self.active_objects)
            elif self.state == GameStates.GAME_OVER:
                self.all_objects['continue'].add_to(self.active_objects)
            elif self.state == GameStates.SETTINGS:
                self.all_objects['settings_title'].add_to(self.active_objects)
                self.all_objects['save_button'].add_to(self.active_objects)
            elif self.state == GameStates.HIGH_SCORES:
                self.all_objects['return_to_title'].add_to(self.active_objects)
            self.state_load = True
        for obj in self.active_objects:
            self.update_list.append(obj.update())
        
    def update_render(self):
        self.surface.fill(Colors.WHITE)
        for obj in self.active_objects:
            obj.draw(self.surface)
        pg.display.update(self.update_list)
        self.update_list.clear()
        self.clock.tick()
    def start(self) -> None:
        while self.run:
            self.handle_events()
            self.update_logic()
            self.update_render()
        pg.quit()
if __name__ == '__main__':
    game = Game()
    game.start()
    pg.quit()