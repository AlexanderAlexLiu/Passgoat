import pygame as pg
import shelve
import sys
import os
import __main__


class GameData:
    OPTIONS = {'mode': 4, 'hard': False, 'scores': []}

    def __init__(self) -> None:
        self.__get_dir()
        self.__load_fonts()
        self.__load_images()
        self.__load_data()

    def set_setting(self, key: str, val) -> None:
        self.settings[key] = val

    def get_setting(self, key: str) -> None:
        return self.settings[key]

    def get_font(self, key: int) -> pg.font.Font:
        return self.__font[key]

    def get_image(self, key: str) -> pg.Surface:
        return self.__images[key]

    def save_data(self) -> None:
        with shelve.open(self.__data_path) as data:
            for key in self.settings.keys():
                data[key] = self.settings[key]

    def __load_data(self) -> None:
        self.settings = {}
        self.__data_path = os.path.join(self.__game_dir, 'save')
        with shelve.open(self.__data_path) as data:
            for key in GameData.OPTIONS.keys():
                try:
                    self.settings[key] = data[key]
                except KeyError:
                    self.settings[key] = GameData.OPTIONS[key]

    def __load_images(self) -> None:
        self.__images = {}
        self.__images_dir = os.path.join(A.asset_dir, 'images')
        self.__image_names = ['icon', 'goat']
        for name in self.__image_names:
            self.__images[name] = pg.image.load(os.path.join(
                self.__images_dir, f"{name}.png")).convert_alpha()

    def __load_fonts(self) -> None:
        self.__font = {}
        self.__font_path = os.path.join(self.__asset_dir, 'font.ttf')
        for i in range(5):
            self.__font[i] = pg.font.Font(self.__font_path, 8*(i+1))

    def __get_dir(self) -> None:
        if getattr(sys, 'frozen', False):
            self.__game_dir = os.path.dirname(sys.executable)
        else:
            self.__game_dir = os.path.dirname(__main__.__file__)
        self.__asset_dir = os.path.join(self.__game_dir, 'assets')
