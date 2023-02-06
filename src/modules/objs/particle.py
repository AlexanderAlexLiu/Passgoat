import random
from modules.objs.gameobject import GameObject
import pygame as pg
import math
class Particle(GameObject):
    def __init__(self, x, y, clock : pg.time.Clock) -> None:
        super().__init__()
        self.size = random.randint(5, 10)
        self.grav = random.random() * 0.2 + 0.2
        self.surface = pg.Surface((self.size, self.size))
        self.surface.fill(pg.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)).correct_gamma(2))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sway_factor = random.randint(1, 10)
        self.clock = clock
        self.old_rect = self.rect.copy()
        self.counter = random.randint(0, 10000)
        self.sway = pg.Vector2(1, 0)

    def update(self) -> list[pg.Rect]:
        if self.dirty:
            self.old_rect = self.rect.copy()
            self.rect.y += self.grav * self.clock.get_time()
            return [self.old_rect, self.rect]

    def draw(self, surface):
        if self.dirty:
            surface.blit(self.surface, self.rect)
            self.old_rect = self.rect.copy()