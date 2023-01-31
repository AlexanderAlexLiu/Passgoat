import os
from game import Game

# used to hide the extra dialogue that appears on startup in pygame games
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

if __name__ == '__main__':
    # create a new game instance
    passgoat = Game()
    # start the main game loop
    passgoat.run()