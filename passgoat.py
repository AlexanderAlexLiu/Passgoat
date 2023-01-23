import pygame as pg
import sys, os, shelve

from src.colors import Colors
from src.states import GameStates
'''
TODO:
- make something to handle events
- figure out program structure
    - UPDATE POSITIONS/LOOKS -> DRAW AND UPDATE -> 
'''

ANTI = False

class GameObject:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.surface = pg.Surface((1, 1))
        self.redraw = True
    
    def change_x(self, x : float) -> None:
        self.x = x
    
    def change_y(self, y : float) -> None:
        self.y = y
    
    def change_pos(self, x : float, y : float) -> None:
        self.change_x(x)
        self.change_y(y)

    def update(self) -> None:
        '''
        updates values and stuff
        '''
        pass

    def draw(self, surface : pg.Surface, update_rects : list) -> None:
        if not self.redraw:
            return
        surface.blit(self.surface, (self.x, self.y))
        update_rects.append((self.x, self.y, self.w, self.h))
        self.redraw = False

class TextLabel(GameObject):

    def __init__(self, text : str, font : pg.font.Font, color : pg.Color):
        super().__init__()
        self.font = font
        self.color = color
        self.text = text
        self.change_text(self.text) # initialize the surface
    def change_text(self, text : str) -> None:
        self.text = text # sets a new text
        self.surface = self.font.render(self.text, ANTI, self.color) # renders that text
        self.w, self.h = self.surface.get_width(), self.surface.get_height() # sets the width and height for later
    def change_color(self, new_color : pg.Color) -> None:
        self.color = new_color # changes the color
        self.change_text(self.text) # updates the text label with the new color
    def center_x(self, x : float):
        self.x = (x - self.w) / 2
    def center_y(self, y : float):
        self.y = (y - self.h) / 2

class ButtonText(TextLabel):
    
    def __init__(self, text: str, font: pg.font.Font, color: pg.Color, hover_color: pg.Color):
        self.hover_color = hover_color
        self.hovered = True
        super().__init__(text, font, color)
        
    def change_text(self, text : str) -> None:
        self.text = text # sets a new text
        self.surface = self.font.render(self.text, ANTI, self.color) # renders that text
        self.inactive_surface = self.font.render(self.text, ANTI, self.hover_color) 
        self.w, self.h = self.surface.get_width(), self.surface.get_height() # sets the width and height for later

    def update(self) -> None:
        if self.surface.get_rect().collidepoint(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]):
            temp = self.surface
            self.surface = self.inactive_surface
            self.inactive_surface = temp
            self.redraw = True


    def draw(self, surface : pg.Surface, update_rects : list) -> None:
        if not self.redraw:
            return
        surface.blit(self.surface, (self.x, self.y))
        update_rects.append((self.x, self.y, self.w, self.h))
        self.redraw = False

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
        self.create_game_objects()
        self.update_rects.append(self.screen.get_rect()) # for first draw

    def decorate_window(self) -> None:
        pg.display.set_caption('Passgoat')
        self.icon = pg.image.load(os.path.join(self.asset_directory, 'icon.png')).convert()
        pg.display.set_icon(self.icon)
    
    def create_game_objects(self) -> None:
        self.game_objects['title'] = TextLabel('PASSGOAT', self.font['extralarge'], Colors.RED)
        self.game_objects['title'].center_x(self.WIN_SIZE[0])
        self.game_objects['title'].change_y(40)
        self.game_objects['caption'] = TextLabel('mehhhhhhhhhhh', self.font['tiny'], Colors.BLUE)
        self.game_objects['caption'].center_x(self.WIN_SIZE[0])
        self.game_objects['caption'].change_y(100)
        self.game_objects['play'] = ButtonText('play', self.font['extralarge'], Colors.RED, Colors.BLACK)

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
            self.active_objects.append(self.game_objects['title'])
            self.active_objects.append(self.game_objects['caption'])
            self.active_objects.append(self.game_objects['play'])

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
        for object in self.active_objects:
            object.update()
            object.draw(self.screen, self.update_rects)
        pg.display.update(self.update_rects)
        self.update_rects.clear()
        self.active_objects.clear()
        print(self.clock.get_fps())
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