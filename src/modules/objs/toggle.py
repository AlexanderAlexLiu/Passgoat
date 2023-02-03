from __future__ import annotations
from modules.objs.button import Button
from modules.objs.colorgroups import ColorGroup
import pygame as pg
from typing import Callable
class Toggle(Button):
	ALIAS=True
	def __init__(A,text,font,colors):super().__init__(text,font,colors,None);A.surface_toggle=A.font.render(A.text,Toggle.ALIAS,A.colors[3]);A.func=A.do_toggle;A.toggle=False
	def set_toggle(A,toggle):A.toggle=toggle
	def do_toggle(A):A.toggle=not A.toggle
	def handle_event(A,event):return super().handle_event(event)
	def draw(A,surface):
		B=surface
		if A.dirty:
			if A.click:B.blit(A.surface_click,A.rect)
			elif A.hover:B.blit(A.surface_hover,A.rect)
			elif A.toggle:B.blit(A.surface_toggle,A.rect)
			else:B.blit(A.surface,A.rect)
			A.old_rect=A.rect.copy();A.set_dirty(False)
	def get_toggle(A):return A.toggle