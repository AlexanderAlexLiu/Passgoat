'''
Alex Liu
2023-01-31

Font class to keep the fonts in-game
'''
import pygame.font as font
import os

class Fonts:
    '''
    class to keep the fonts used in-game
    not sure if this is a good method to divide
    a game into multiple parts, but it seems like it
    '''
    # constants for the class
    TINY = None
    SMALL = None
    NORM = None
    BIG = None
    LARGE = None
    # flag to keep track of if the class was initialized
    is_init = False
    def init(font_dir : str) -> None:
        '''
        given the path to the asset directory, try to load a single
        font named font.ttf from that folder 
        '''
        if Fonts.is_init:
            return
        if not font.get_init():
            font.init()
        path = os.path.join(font_dir, 'font.ttf')
        Fonts.TINY = font.Font(path, 8)
        Fonts.SMALL = font.Font(path, 16)
        Fonts.NORM = font.Font(path, 24)
        Fonts.BIG = font.Font(path, 32)
        Fonts.LARGE = font.Font(path, 40)