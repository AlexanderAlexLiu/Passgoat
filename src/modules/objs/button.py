from __future__ import annotations
_A=False
from modules.objs.textlabel import TextLabel
from modules.objs.colorgroups import ColorGroup
import pygame as pg
from typing import Callable
class Button(TextLabel):
	ALIAS=True
	def __init__(A,text,font,colors,func=None,param=None):super().__init__(text,font,colors);A.surface_hover=A.font.render(A.text,Button.ALIAS,A.colors[1]);A.surface_click=A.font.render(A.text,Button.ALIAS,A.colors[2]);A.hover,A.click=_A,_A;A.func,A.param=func,param
	def set_text(A,text):super().set_text(text);A.surface_hover=A.font.render(A.text,Button.ALIAS,A.colors[1]);A.surface_click=A.font.render(A.text,Button.ALIAS,A.colors[2]);return A
	def draw(A,surface):
		B=surface
		if A.dirty:
			if A.click:B.blit(A.surface_click,A.rect)
			elif A.hover:B.blit(A.surface_hover,A.rect)
			else:B.blit(A.surface,A.rect)
			A.old_rect=A.rect.copy();A.set_dirty(_A)
	def handle_event(A,event):
		B=event
		match B.type:
			case pg.MOUSEBUTTONDOWN:
				if A.rect.collidepoint(B.pos):A.click=True;A.set_dirty()
			case pg.MOUSEBUTTONUP:
				if A.click:
					A.click=_A
					if not A.rect.collidepoint(B.pos):A.hover=_A
					if A.func:
						if A.param==None:A.func()
						else:A.func(A.param)
					A.set_dirty()
			case pg.MOUSEMOTION:
				if A.rect.collidepoint(B.pos):
					if not A.hover:A.hover=True;A.set_dirty()
				elif A.hover:A.hover=_A;A.set_dirty()
	def add_to(A,ls):super().add_to(ls);A.hover=_A;A.click=_A