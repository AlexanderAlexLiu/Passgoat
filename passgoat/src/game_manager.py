from button_label import ButtonLabel
from text_label import TextLabel
from toggle_label import ToggleLabel
from colors import Colors
import pygame
'''
List of numbers to cross out -> A bunch of toggle buttons
Ghost numbers (lock feature?) -> ghost numbers will be replaced with any input, lock with double click?
different difficulties:
	5 numbers (one of each) -> oh my god I want to jump
	anything beyond (repeated numbers ok) -> jesus christ I want to jump
minutes, hours... -> pass in clock object to the game
scroll with mouse pwease uwu -> mouse scroll event on game
personal record? -> uhh leaderboard? how to sort?
reset history placement	-> this should be done in reset()
number of guesses to solve - shown at end -> easy clap
Fix description -> done in cx_freeze
'''

class GameManager:
    def __init__(self, ) -> None:
        self.guess = []
        self.locked_slots = []
