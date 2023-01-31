'''
Alex Liu
2023-01-30
Pygame number guessing game
For Rachel
'''



from colors import Colors
import os
import sys
import math
import shelve
from enum import Enum

# hides the extra text when importing pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

class State(Enum):
    TITLE = 0
    OPTIONS = 1
    INGAME = 2
    PAUSE = 3
    GAMEOVER = 4
    LEADERBOARD = 5

import pygame as pg
from button_label import ButtonLabel
from text_label import TextLabel

class Game:

    def __init__(self) -> None:
        '''
        main function, initializes display, and does any setup before running the main loop
        pygame.display.set_mode() should be the last thing that's called to ensure no lag with
        a blank window at the start
        '''
        # importss
        if not pg.display.get_init():
            pg.display.init()
        if not pg.font.get_init():
            pg.font.init()
        # eventually need mixer to be init here

        self.register_events()  # blocks and allows certain events needed for the game

        # variables to do with the game itself
        # attribute to keep track of game state, will always start at title
        self.state = State.TITLE

        # RELATED TO ASSETS
        self.asset_dir = os.path.join(self.get_game_dir(), 'assets')
        print(self.asset_dir)
        # RENDERING RELATED
        # dirt rectangles
        self.on_screen_objects = []
        self.all_objects = {}
        self.dirty_rects = []
        self.clock = pg.time.Clock()
        self.SIZE = (600, 400)
        self.font = {}
        self.load_fonts()
        self.create_all_objects()
        self.state_init = False
        self.surface = pg.display.set_mode(self.SIZE)
        self.decorate_window()

    def placeholder_click(self, arg) -> None:
        print('I WAS CLICKED + ' + arg)

    def quit_game(self) -> None:
        sys.exit()

    def change_state(self, to_state: State) -> None:
        self.state = to_state
        self.state_init = False

    def delete_save(self) -> None:
        print('DELETE')

    def create_all_objects(self) -> None:
        # TITLE ADD THE TINY GOAT AND WE SHOULD BE DONE HERE
        self.all_objects['title.label'] = TextLabel(
            self.font[3], 'PASSGOAT', Colors.RED)
        self.all_objects['title.label'].center(do_x=True)
        self.all_objects['title.label'].move_to(y=40)
        self.all_objects['title.caption'] = TextLabel(
            self.font[0], 'mehhhhhhhhhhhh', Colors.BLUE)
        self.all_objects['title.caption'].center(do_x=True)
        self.all_objects['title.caption'].move_to(y=90)
        self.all_objects['title.play'] = ButtonLabel(
            self.font[2], 'Play', Colors.RED, Colors.ORANGE, Colors.BLUE, self.change_state, State.INGAME)
        self.all_objects['title.play'].move_to(200, 200)
        self.all_objects['title.options'] = ButtonLabel(
            self.font[2], 'Options', Colors.RED, Colors.ORANGE, Colors.BLUE, self.change_state, State.OPTIONS)
        self.all_objects['title.options'].move_to(300, 200)
        self.all_objects['title.quit'] = ButtonLabel(
            self.font[2], 'Quit', Colors.GREY, Colors.GREEN, Colors.CYAN, self.quit_game)
        self.all_objects['title.quit'].center(do_x=True)
        self.all_objects['title.quit'].move_to(y=270)

        # OPTIONS
        self.all_objects['options.label'] = TextLabel(
            self.font[3], 'OPTIONS', Colors.RED)
        self.all_objects['options.label'].center(do_x=True)
        self.all_objects['options.label'].move_to(y=40)
        '''GOT TO INCLUDE SOME SETTINGS TO TWEAK'''
        self.all_objects['options.delete_hs'] = ButtonLabel(
            self.font[1], 'Delete Scores', Colors.RED, Colors.ORANGE, Colors.BLUE, self.delete_save)
        self.all_objects['options.delete_hs'].center(do_x=True)
        self.all_objects['options.delete_hs'].move_to(y=100)
        # 5 Digit Mode? -> Included in the scroller
        # Up to 10 Digit Mode? -> Make a scroller : add warning of > 5 digits
        # Delete HS -> Just deletes the file, don't know why you'd want to do this

        self.all_objects['options.save'] = ButtonLabel(
            self.font[0], 'Back to Title', Colors.RED, Colors.ORANGE, Colors.BLUE, self.change_state, State.TITLE)
        self.all_objects['options.save'].center(do_x=True)
        self.all_objects['options.save'].move_to(y=270)
        # INGAME

        '''MAKE A TOGGLE BUTTON CLASS TO INCLUDE HERE'''
        # PAUSE
        self.all_objects['pause.label'] = TextLabel(
            self.font[3], 'PAUSE', Colors.RED)
        self.all_objects['pause.label'].center(do_x=True)
        self.all_objects['pause.label'].move_to(
            y=40)  # COPY FOR GAME MANAGER'S _ _ _ _
        self.all_objects['pause.resume'] = ButtonLabel(
            self.font[2], 'Resume', Colors.RED, Colors.ORANGE, Colors.BLUE, self.change_state, State.INGAME)
        self.all_objects['pause.resume'].center(do_x=True)
        self.all_objects['pause.resume'].move_to(y=200)
        self.all_objects['pause.quit'] = ButtonLabel(
            self.font[1], 'Quit', Colors.GREY, Colors.GREEN, Colors.CYAN, self.change_state, State.TITLE)
        self.all_objects['pause.quit'].center(do_x=True)
        self.all_objects['pause.quit'].move_to(y=250)
        # GAMEOVER
        '''
        should literally just display the answer + a continue button with confetti if I have time'''
        self.all_objects['gameover.label'] = TextLabel(
            self.font[3], 'YOU WIN!', Colors.BLACK)
        # looking at this, it might be nice to return itself and so I can "chain" changes
        self.all_objects['gameover.label'].center(do_x=True)
        self.all_objects['gameover.label'].move_to(y=40)

        self.all_objects['gameover.continue'] = ButtonLabel(
            self.font[1], 'Continue', Colors.RED, Colors.ORANGE, Colors.BLUE, self.change_state, State.LEADERBOARD)
        self.all_objects['gameover.continue'].center(do_x=True)
        self.all_objects['gameover.continue'].move_to(y=300)
        # LEADERBOARD
        self.all_objects['leaderboard.label'] = TextLabel(
            self.font[2], 'Saved Scores', Colors.CYAN)
        self.all_objects['leaderboard.label'].center(do_x=True)
        self.all_objects['leaderboard.label'].move_to(y=40)
        self.all_objects['leaderboard.continue'] = ButtonLabel(
            self.font[1], 'Back to Title', Colors.RED, Colors.GREEN, Colors.BLUE, self.change_state, State.TITLE)
        self.all_objects['leaderboard.continue'].center(do_x=True)
        self.all_objects['leaderboard.continue'].move_to(y=300)

    def load_fonts(self) -> None:
        font_path = os.path.join(self.asset_dir, 'font.ttf')
        self.font[0] = pg.font.Font(font_path, 16)
        self.font[1] = pg.font.Font(font_path, 24)
        self.font[2] = pg.font.Font(font_path, 32)
        self.font[3] = pg.font.Font(font_path, 40)

    def get_game_dir(self) -> str:
        path = ''
        if getattr(sys, 'frozen', False):
            path = os.path.dirname(sys.executable)
        else:
            path = os.path.dirname(os.path.dirname(__file__))
        return path

    def register_events(self) -> None:
        '''
        blocks and sets the events for pygame to process
        heard this improves performance before since pygame
        '''
        pg.event.set_blocked(
            None)  # this line blocks every event to the window
        # not gonna lie, these are basically all events possible in pygame but a few
        pg.event.set_allowed(
            (pg.QUIT,
             pg.MOUSEMOTION,
             pg.KEYDOWN,
             pg.KEYUP,
             pg.WINDOWMOVED,
             pg.WINDOWMINIMIZED,
             pg.MOUSEBUTTONDOWN,
             pg.MOUSEBUTTONUP))

    def decorate_window(self) -> None:
        '''
        adds a little spice to the game window, removes the default pygame icon
        and sets the window title to the game's title
        '''
        self.icon = pg.image.load(os.path.join(
            self.asset_dir, 'icon.png')).convert()
        pg.display.set_caption('PASSGOAT')
        pg.display.set_icon(self.icon)

    def handle_events(self) -> None:
        for event in pg.event.get():
            print(event)
            match event.type:
                case pg.QUIT:
                    sys.exit()
                case pg.WINDOWMOVED | pg.WINDOWMINIMIZED:
                    if self.state == State.INGAME:
                        self.change_state(State.PAUSE)
                case pg.KEYDOWN:
                    if event.key == 96:
                        if self.state == State.TITLE:
                            self.change_state(State.INGAME)
                        elif self.state == State.INGAME:
                            self.change_state(State.PAUSE)
                        elif self.state == State.PAUSE:
                            self.change_state(State.GAMEOVER)
                        elif self.state == State.GAMEOVER:
                            self.change_state(State.LEADERBOARD)
                        elif self.state == State.LEADERBOARD:
                            self.change_state(State.OPTIONS)
                        elif self.state == State.OPTIONS:
                            self.change_state(State.TITLE)
                    elif event.key == 27:
                        if self.state == State.INGAME:
                            self.change_state(State.PAUSE)
            for game_obj in self.on_screen_objects:
                game_obj.handle_event(event)

    def update_logic(self) -> None:
        if not self.state_init:
            self.on_screen_objects.clear()
            self.state_init = True
            self.dirty_rects.append(self.surface.get_rect())
            match self.state:
                case State.TITLE:
                    self.all_objects['title.label'].add_to(
                        self.on_screen_objects)
                    self.all_objects['title.play'].add_to(
                        self.on_screen_objects)
                    self.all_objects['title.options'].add_to(
                        self.on_screen_objects)
                    self.all_objects['title.caption'].add_to(
                        self.on_screen_objects)
                    self.all_objects['title.quit'].add_to(
                        self.on_screen_objects)
                case State.OPTIONS:
                    self.all_objects['options.label'].add_to(
                        self.on_screen_objects)
                    self.all_objects['options.delete_hs'].add_to(
                        self.on_screen_objects)
                    self.all_objects['options.save'].add_to(
                        self.on_screen_objects)
                case State.INGAME:
                    # ASK GAME MANAGAER TO ADD IT'S OBJECTS TO THE ONSCREEN OBJECTS
                    pass
                case State.PAUSE:
                    self.all_objects['pause.label'].add_to(
                        self.on_screen_objects)
                    self.all_objects['pause.resume'].add_to(
                        self.on_screen_objects)
                    self.all_objects['pause.quit'].add_to(
                        self.on_screen_objects)
                case State.GAMEOVER:
                    self.all_objects['gameover.continue'].add_to(
                        self.on_screen_objects)
                    self.all_objects['gameover.label'].add_to(
                        self.on_screen_objects)
                case State.LEADERBOARD:
                    self.all_objects['leaderboard.continue'].add_to(
                        self.on_screen_objects)
                    self.all_objects['leaderboard.label'].add_to(
                        self.on_screen_objects)
        for game_obj in self.on_screen_objects:
            rects = game_obj.update()
            if rects:
                self.dirty_rects.extend(rects)

    def render_screen(self) -> None:
        self.surface.fill(Colors.WHITE)
        for game_obj in self.on_screen_objects:
            game_obj.render(self.surface)
        pg.display.update(self.dirty_rects)
        self.dirty_rects.clear()

    def run(self) -> None:
        while 1:
            self.handle_events()
            self.update_logic()
            self.render_screen()
            # currently empty, when settings kick in, fill with something
            self.clock.tick_busy_loop(240)
