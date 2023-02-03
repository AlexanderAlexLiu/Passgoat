from modules.objs.gameobject import GameObject
import pygame as pg
class ScrollabeList(GameObject):
	def __init__(A):super().__init__();A.surface=pg.Surface((600,400))
	def draw(A,surface):
		if A.dirty:0