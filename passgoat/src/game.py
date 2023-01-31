'''
Alex Liu
2023-01-30
Pygame number guessing game
For R.Y
'''

import pygame as pg
import os, sys
from states.states import GameState
from helpers.font import Fonts
class Game:

    def __init__(self) -> None:
        '''
        main function, initializes display, and does any setup before running the main loop
        
        pygame.display.set_mode() should be the last thing that's called to ensure no lag with
        a blank window at the start?
        '''
        
        pg.display.init()

        # eventually need mixer to be init here

        self.register_events()  # blocks and allows certain events needed for the game, 100% will be here

        
        # variables to do with the game itself
        # attribute to keep track of game state, will always start at title
        self.game_state = GameState.TITLE

        # RELATED TO ASSETS
        self.asset_dir = os.path.join(self.get_game_dir(), 'assets')
        Fonts.init(self.asset_dir)
        # RENDERING RELATED
        self.on_screen_objs = [] # a list to keep track of objects that should be on screen
        self.refresh_rects = []
        self.states = {}
        # is this lazy loading?
        from states.title_state import TitleState
        from states.pause_state import PauseState
        from states.gameover_state import GameOverState
        from states.options_state import OptionsState
        from states.leaderboard_state import LeaderboardState
        from states.ingame_state import InGameState
        self.states['title'] = TitleState()
        self.states['pause'] = PauseState()
        self.states['gameover'] = GameOverState()
        self.states['options'] = OptionsState()
        self.states['leaderboard'] = LeaderboardState()
        self.states['ingame'] = InGameState()
        self.game_clock = pg.time.Clock()
        self.WINDOW_SIZE = (600, 400)
        self.surface = pg.display.set_mode(self.WINDOW_SIZE)
        self.decorate_window()

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
        pg.event.set_blocked(None)  # this line blocks every event to the window
        # not gonna lie, these are basically all events possible in pygame but a few
        pg.event.set_allowed((pg.QUIT,pg.MOUSEMOTION,pg.KEYDOWN,pg.KEYUP,pg.WINDOWMOVED,pg.WINDOWMINIMIZED,pg.MOUSEBUTTONDOWN,pg.MOUSEBUTTONUP))

    def decorate_window(self) -> None:
        '''
        adds a little spice to the game window, removes the default pygame icon
        and sets the window title to the game's title
        '''
        self.icon = pg.image.load(os.path.join(self.asset_dir, 'icon.png')).convert()
        pg.display.set_caption('Passgoat')
        pg.display.set_icon(self.icon)

    def handle_events(self) -> None:
        for event in pg.event.get():
            print(event)
            match event.type:
                case pg.QUIT:
                    sys.exit()
            for game_obj in self.on_screen_objs:
                game_obj.handle_event(event)

    def update_logic(self) -> None:
        pass

    def render_screen(self) -> None:
        pass

    def run(self) -> None:
        while 1:
            self.handle_events()
            self.update_logic()
            self.render_screen()
            # currently empty, when settings kick in, fill with something
            self.game_clock.tick_busy_loop()
