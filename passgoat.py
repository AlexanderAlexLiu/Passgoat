'''
Alex Liu
2023-01-24
"I want a number guessing game" - R.Y

Practice for commenting and doing things the OOP way!
'''
import pygame as pg
import sys, os, shelve

from src.colors import Colors
from src.states import GameStates

ANTIALIAS = True

class GameObject:
    '''
    base object for something in the game
    '''
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.redraw = False
    def queue_draw(self) -> None:
        self.redraw = True
    def update(self) -> list:
        '''
        update is usually for moving or whatever. It should return a list rectangles that need to be re-flipped
        '''
        pass
    def draw(self, surface : pg.Surface) -> None:
        '''
        draw itself and nothing else
        '''
        pass
    def set_pos(self, x : float, y : float) -> None:
        self.x = x
        self.y = y
    def set_x(self, x : float):
        self.x = x
    def set_y(self, y : float):
        self.y = y

class TextObject(GameObject):
    def __init__(self, text : str, font : pg.font.Font, color : pg.color.Color) -> None:
        super().__init__()
        self.text = text
        self.color = color
        self.font = font
        self.font_surface = self.font.render(self.text, ANTIALIAS, self.color)
        self.w, self.h = self.font_surface.get_size()
    def draw(self, surface : pg.Surface) -> None:
        if self.redraw:
            surface.blit(self.font_surface, (self.x, self.y))
            self.redraw = False
    def update(self) -> tuple:
        if self.redraw:
            return (self.x, self.y, self.w, self.h)
        else:
            return 
    def center_x(self, x : float):
        self.x = (x - self.w) / 2
    def center_y(self, y : float):
        self.y = (y - self.h) / 2

class TextButton(TextObject):
    def __init__(self, text: str, font: pg.font.Font, color: pg.color.Color, hcolor: pg.color.Color) -> None:
        super().__init__(text, font, color)
        self.hcolor = hcolor
        self.hover = False
        self.hover_font_surface = self.font.render(self.text, ANTIALIAS, self.hcolor)
    def draw(self, surface : pg.surface) -> None:
        if self.redraw:
            if self.hover:
                surface.blit(self.hover_font_surface, (self.x, self.y))
            else:
                surface.blit(self.font_surface, (self.x, self.y))
            self.redraw = False
    def update(self) -> tuple:
        if self.redraw:
            return (self.x, self.y, self.w, self.h)
        if pg.Rect(self.x, self.y, self.w, self.h).collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                self.click_behavior(self.state)
            self.hover = True
            self.redraw = True
            return (self.x, self.y, self.w, self.h)
        elif self.hover:
            self.hover = False
            self.redraw = True
            return (self.x, self.y, self.w, self.h)
    def click_state_behavior(self, function, state) -> None:
        self.click_behavior = function
        self.state = state
class Passgoat:

    def __init__(self) -> None:
        self.asset_directory = self.get_asset_directory() # path for assets to be searched in
        pg.display.init()
        self.configure_events()
        pg.font.init()
        self.WIN_SIZE = (600, 400) # constant to store window size
        self.screen = pg.display.set_mode(self.WIN_SIZE) # an instance of the 'main' screen that is shown
        self.decorate_window() # decorate window immediately after setting video mode
        self.clock = pg.time.Clock() # clock object to calculate time between frames
        self.run = True # run boolean for the main method
        self.active_objects = [] # objects that are on screen and should be updated
        self.game_objects = {} # dictionary of existing game objects
        self.update_rects = [] # rectangles that should be updated
        self.state = GameStates.TITLE # attribute to store game state
        self.init_state = False
        self.font = {} # font dictionary
        self.load_fonts() # load all the fonts in
        self.create_game_objects()
        #self.update_rects.append(self.screen.get_rect()) # for first draw
    def change_to_state(self, state):
        self.init_state = False
        temp = self.state
        self.state = state
        print("FROM {} TO {}".format(temp, self.state))
        
    def create_game_objects(self):
        self.game_objects['title'] = TextObject('PASSGOAT', self.font['extralarge'], Colors.RED)
        self.game_objects['title'].center_x(self.WIN_SIZE[0])
        self.game_objects['title'].set_y(40)
        self.game_objects['caption'] = TextObject('mehhhhhhhhhhhhhhh', self.font['tiny'], Colors.BLUE)
        self.game_objects['caption'].center_x(self.WIN_SIZE[0])
        self.game_objects['caption'].set_y(100)
        self.game_objects['play'] = TextButton('PLAY', self.font['large'], Colors.BLUE, Colors.BLACK)
        self.game_objects['play'].center_x(self.WIN_SIZE[0] - 200)
        self.game_objects['play'].set_y(240)
        self.game_objects['play'].click_state_behavior(self.change_to_state, GameStates.IN_GAME)

        self.game_objects['settings'] = TextButton('OPTIONS', self.font['large'], Colors.BLUE, Colors.BLACK)
        self.game_objects['settings'].center_x(self.WIN_SIZE[0] + 200)
        self.game_objects['settings'].set_y(240)
        self.game_objects['settings'].click_state_behavior(self.change_to_state, GameStates.SETTINGS)

    def decorate_window(self) -> None:
        '''
        sets the title of the pygame window and changes the icon
        '''
        pg.display.set_caption('Passgoat')
        self.icon = pg.image.load(os.path.join(self.asset_directory, 'icon.png')).convert()
        pg.display.set_icon(self.icon)

    def load_fonts(self) -> None:
        '''
        loads all the fonts for the game
        '''
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
            pg.QUIT,
            pg.MOUSEMOTION,
            pg.MOUSEWHEEL,
            pg.MOUSEBUTTONUP,
            pg.MOUSEBUTTONDOWN,
            pg.WINDOWFOCUSLOST
        ))

    def update_logic(self) -> None:
        '''
        updates the "logic" part of game objects, does not draw in any way 
        '''
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                # add saving
                print("ADD SAVING MF")
                self.run = False
            elif event.type == pg.WINDOWFOCUSLOST:
                if self.state == GameStates.IN_GAME:
                    self.change_to_state(GameStates.PAUSE)
            elif event.type == pg.MOUSEBUTTONDOWN:
                pass
            elif event.type == pg.MOUSEBUTTONUP:
                pass
            elif event.type == pg.KEYDOWN:
                pass
            elif event.type == pg.KEYUP:
                pass
            elif event.type == pg.MOUSEMOTION:
                pass
            elif event.type == pg.MOUSEWHEEL:
                pass
        if not self.init_state:
            # these should ONLY be used to add/remove objects!
            self.active_objects.clear()
            self.update_rects.append(self.screen.get_rect())
            if self.state == GameStates.TITLE:
                self.active_objects.append(self.game_objects['title'])
                self.active_objects.append(self.game_objects['caption'])
                self.active_objects.append(self.game_objects['play'])
                self.active_objects.append(self.game_objects['settings'])
                self.game_objects['title'].queue_draw()
                self.game_objects['caption'].queue_draw()
                self.game_objects['play'].queue_draw()
                self.game_objects['settings'].queue_draw()
            elif self.state == GameStates.IN_GAME:
                self.active_objects.append(self.game_objects['ingame'])
                self.game_objects['ingame'].queue_draw()
            elif self.state == GameStates.PAUSE:
                self.active_objects.append(self.game_objects['pause'])
                self.game_objects['pause'].queue_draw()
            elif self.state == GameStates.GAME_OVER:
                self.active_objects.append(self.game_objects['gameover'])
                self.game_objects['gameover'].queue_draw()
            elif self.state == GameStates.SETTINGS:
                self.active_objects.append(self.game_objects['settings'])
                self.game_objects['settings'].queue_draw()
            elif self.state == GameStates.HIGH_SCORES:
                self.active_objects.append(self.game_objects['highscores'])
                self.game_objects['highscores'].queue_draw()
            self.init_state = True
        for object in self.active_objects:
            self.update_rects.append(object.update()) # the physics update of the object
        
    def update_render(self) -> None:
        '''
        this method should NEVER try and update anything! it just renders
        '''
        #print(self.clock.get_fps())
        self.screen.fill(Colors.WHITE) # usually not done like this, but it is an exception (always white background)
        for things in self.active_objects:
            things.draw(self.screen)
        pg.display.update(self.update_rects) # updates all the rectangles
        self.update_rects.clear() # clear all the rectangles that need to be updated
        self.clock.tick() # could use tick_busy_loop, but heard it uses more CPU.
        # also don't think it matters TOO much that the timing resolution is insane
        

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