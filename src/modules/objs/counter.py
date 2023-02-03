from __future__ import annotations
from modules.objs.button import Button
from modules.objs.colorgroups import ColorGroup
import pygame as pg
class Counter(Button):
	def __init__(A,text,font,colors,lower,upper):super().__init__(text,font,colors);A.lower,A.upper=lower,upper;A.count=A.lower;A.label=text;A.func=A.increase
	def increase(A):
		A.count+=1
		if A.count>A.upper:A.count=A.lower
		A.set_text(f"{A.label} : {A.count}")
	def get_count(A):return A.count
	def set_count(A,count):
		B=count
		if A.lower<=B<=A.upper:A.count=B;A.set_text(f"{A.label} : {A.count}")