'''
Alex Liu
2023-02-03

number guessing game with pygame

for R.Y.
'''

from data import GameData
import pygame, sys

class Passgoat:
    def __init__(self) -> None:
        self.SIZE = (600, 400)
        pygame.display.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode(self.SIZE)
        #self.surface = pygame.display.set_mode(self.SIZE, pygame.HIDDEN)
        pygame.display.iconify()
        self.data = GameData()
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def update(self) -> None:
        pass
    def draw(self) -> None:
        pass
    def run(self) -> None:
        while 1:
            self.handle_events()
            self.update()
            self.draw()
if __name__ == '__main__':
    game = Passgoat()
    game.run()