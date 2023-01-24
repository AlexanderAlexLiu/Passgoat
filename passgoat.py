import pygame as pg
import sys, os, shelve

from src.colors import Colors
from src.states import GameStates

class Passgoat:
    def __init__(self) -> None:
        self.asset_directory = self.get_asset_directory() # path for assets to be searched in
        pg.display.init()
        pg.font.init()
        self.WIN_SIZE = (600, 400) # constant to store window size
        self.screen = pg.display.set_mode(self.WIN_SIZE) # an instance of the 'main' screen that is shown
        self.decorate_window() # decorate window immediately after setting video mode
        self.clock = pg.time.Clock() # clock object to calculate time between frames
        self.run = True # run boolean for the main method
        self.active_objects = [] # objects that are on screen and should be updated
        self.game_objects = {}
        self.update_rects = [] # rectangles that should be updated
        self.state = GameStates.TITLE
        self.font = {}
        self.load_fonts()
        self.update_rects.append(self.screen.get_rect()) # for first draw

    def decorate_window(self) -> None:
        pg.display.set_caption('Passgoat')
        self.icon = pg.image.load(os.path.join(self.asset_directory, 'icon.png')).convert()
        pg.display.set_icon(self.icon)

    def load_fonts(self) -> None:
        font_path = os.path.join(self.asset_directory, 'font.ttf')
        self.font['extralarge'] = pg.font.Font(font_path, 40)
        self.font['large'] = pg.font.Font(font_path, 32)
        self.font['normal'] = pg.font.Font(font_path, 24)
        self.font['tiny'] = pg.font.Font(font_path, 16)

    def get_asset_directory(self) -> str:
        '''
        returns where assets SHOULD be looked for if the program is frozen vs running in ide
        '''
        asset_folder_path = ''
        if getattr(sys, 'frozen', False):
            # frozen program
            asset_folder_path = os.path.dirname(sys.executable)
        else:
            # not frozen
            asset_folder_path = os.path.dirname(__file__)
        return os.path.join(asset_folder_path, 'assets')

    def configure_events(self) -> None:
        '''
        configures allowed and blocked events so that the game can process things faster
        '''
        pg.event.set_blocked(None)
        pg.event.set_allowed((
            pg.KEYDOWN,
            pg.KEYUP,
            pg.QUIT
        ))

    def update_logic(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
        self.screen.fill(Colors.WHITE) # usually not done like this, but it is an exception 
        if self.state == GameStates.TITLE:
            pass
        elif self.state == GameStates.IN_GAME:
            pass
        elif self.state == GameStates.PAUSE:
            pass
        elif self.state == GameStates.GAME_OVER:
            pass
        elif self.state == GameStates.SETTINGS:
            pass
        elif self.state == GameStates.HIGH_SCORES:
            pass
        
    def update_render(self) -> None:
        '''
        this method should NEVER try and update anything! it just renders
        '''
        print(self.clock.get_fps())
        for object in self.active_objects:
            object.update()
            self.update_rects.append(object.draw(self.screen))
        pg.display.update(self.update_rects)
        self.update_rects.clear()
        self.active_objects.clear()
        self.clock.tick_busy_loop()
        

    def start(self) -> None:
        '''
        'main method' of the game, nothing important should happen here but calling the update functions
        '''
        while self.run:
            self.update_logic()
            self.update_render()
        pg.quit()

if __name__ == '__main__':
    game = Passgoat()
    game.start()