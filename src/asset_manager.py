import pygame as pg
import os, sys

class AssetManager:
    def __init__(self, dir : str) -> None:
        self.parent_dir = dir
        self.asset_dir = self.get_asset_dir()
        self.icon = None
        self.load_icon()
        self.font = {}
        self.load_fonts()
    def load_fonts(self) -> None:
        font_path = os.path.join(self.asset_dir, 'font.ttf')
        self.font[4] = pg.font.Font(font_path, 40)
        self.font[3] = pg.font.Font(font_path, 32)
        self.font[2] = pg.font.Font(font_path, 24)
        self.font[1] = pg.font.Font(font_path, 16)
    def get_font(self, n : int) -> pg.font.Font:
        return self.font[n]
    def load_icon(self) -> None:
        self.icon = pg.image.load(os.path.join(self.asset_dir, 'icon.png')).convert()
    def get_icon(self) -> pg.Surface:
        return self.icon
    def get_asset_dir(self) -> str:
        '''
        returns where assets SHOULD be looked for if the program is frozen vs running in ide
        '''
        asset_folder_path = ''
        if getattr(sys, 'frozen', False):
            # frozen program
            asset_folder_path = os.path.dirname(sys.executable)
        else:
            # not frozen
            asset_folder_path = os.path.dirname(self.parent_dir)
        return os.path.join(asset_folder_path, 'assets')
