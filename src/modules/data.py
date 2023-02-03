'''
Alex Liu
2023-02-03

class to keep track of all I/O of the game
this includes loading images, fonts, etc.
'''

import shelve, sys, pygame, os, __main__

class GameData:
    OPTIONS = {
        'mode' : 0,
        'dark' : False,
        'hard' : False,
        'scores' : []
    }
    def __init__(self) -> None:
        self.__get_dir()
        self.__load_fonts()
        self.__load_images()
        self.__load_data()
    def get_font(self, key : int) -> pygame.font.Font:
        '''
        returns a pygame font object given a integer key
        for passgoat, its 0 to 4
        if it doesn't exist, return None
        '''
        if key in self.__font.keys():
            return self.__font[key]
        return None
    def get_image(self, key : str) -> pygame.Surface:
        '''
        returns a pygame surface object given a string key
        for passgoat, the valid keys are hardcoded
        if it doesn't exist, return None
        '''
        if key in self.__images.keys():
            return self.__images[key]
        return None
    def save_data(self) -> None:
        with shelve.open(self.__data_path) as data:
            for key in self.settings.keys():
                data[key] = self.settings[key]
    def __load_data(self) -> None:
        self.settings = {}
        self.__data_path = os.path.join(self.__game_dir, 'data')
        with shelve.open(self.__data_path) as data:
            for key in GameData.OPTIONS.keys():
                try:
                    self.settings[key] = data[key]
                except KeyError:
                    self.settings[key] = GameData.OPTIONS[key]
    def __load_images(self) -> None:
        self.__images = {}
        img_dir = os.path.join(self.asset_dir, 'images')
        image_names = ['icon', 'goat']
        # everything is a png
        for string in image_names:
            self.__images[string] = pygame.image.load(os.path.join(img_dir, f'{string}.png')).convert_alpha()
    def __load_fonts(self) -> None:
        self.__font = {}
        font_path = os.path.join(self.asset_dir, 'font.ttf')
        # 0 smallest 4 largest
        for i in range(5):
            self.__font[i] = pygame.font.Font(font_path, 8*(i+1))
    
    def __get_dir(self) -> None:
        if getattr(sys, 'frozen', False):
            # game is frozen
            # where the executable is
            self.__game_dir = os.path.dirname(sys.executable)
        else:
            # should be where passgoat.py is
            self.__game_dir = os.path.dirname(__main__.__file__)
        self.asset_dir = os.path.join(self.__game_dir, 'assets')