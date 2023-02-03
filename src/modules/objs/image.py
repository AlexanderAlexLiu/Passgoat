from __future__ import annotations
_A=False
from modules.objs.gameobject import GameObject
import pygame as pg
class Image(GameObject):
	def __init__(A,image):super().__init__();A.surface=image;A.rect=A.surface.get_rect();A.old_rect=A.rect.copy()
	def move_to(A,x=None,y=None):
		A.old_rect=A.rect.copy()
		if x:A.rect.x=x
		if y:A.rect.y=y
		return A
	def center(A,x=_A,y=_A):
		if x:A.move_to(x=(600-A.rect.w)/2)
		if y:A.move_to(y=(400-A.rect.h)/2)
		return A
	def update(A):
		if A.dirty:return[A.rect,A.old_rect]
	def draw(A,surface):
		if A.dirty:surface.blit(A.surface,A.rect);A.old_rect=A.rect.copy();A.dirty=_A