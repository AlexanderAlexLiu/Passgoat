'\nAlex Liu\n2023-02-03\n\nnumber guessing game with pg\n\nfor R.Y.\n'
_U='scores.label'
_T='end.label'
_S='pause.to_title'
_R='pause.resume'
_Q='pause.label'
_P='options.wipe'
_O='options.to_title'
_N='options.label'
_M='title.quit'
_L='title.options'
_K='title.play'
_J='title.goat'
_I='title.caption'
_H='title.label'
_G='ingame.guess'
_F='ingame.answer_hidden'
_E='hard'
_D='mode'
_C='options.complexity'
_B='options.hard_mode'
_A=True
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
from modules.data import GameData as gd
from modules.game_states import GameStates as gs
from modules.colors import Colors as col
import pygame as pg
from modules.objs.image import Image
from modules.objs.button import Button
from modules.objs.textlabel import TextLabel
from modules.objs.colorgroups import ColorGroup
from modules.objs.toggle import Toggle
from modules.objs.counter import Counter
import sys,random
class Passgoat:
	DIGITS='0','1','2','3','4','5','6','7','8','9'
	def __init__(A):A.SIZE=600,400;pg.display.init();pg.font.init();A.surface=pg.display.set_mode(A.SIZE,pg.HIDDEN);A.register_events();A.data=gd();A.decorate_window();A.state=gs.TITLE;A.clock=pg.time.Clock();A.screen_objs=[];A.dirty_rects=[];A.create_objs();A.state_init=False
	def register_events(A):pg.event.set_blocked(None);pg.event.set_allowed((pg.QUIT,pg.MOUSEBUTTONUP,pg.MOUSEBUTTONDOWN,pg.MOUSEMOTION,pg.KEYDOWN,pg.KEYUP,pg.WINDOWMOVED,pg.WINDOWMINIMIZED))
	def quit_game(A):pg.quit();sys.exit()
	def play_game(A):
		B=A.data.settings[_D];A.generate_answer(B);C=TextLabel(' '.join(('_'for A in range(B))),A.data.get_font(2),ColorGroup.LABEL);D=TextLabel(' '.join(('_'for A in range(B))),A.data.get_font(1),ColorGroup.LABEL);C.move_to(y=40);D.move_to(y=200);A.guess=[]
		if B>5 and not A.data.settings[_E]:C.center_right(x=_A);D.center_right(x=_A)
		else:C.center(x=_A);D.center(x=_A)
		A.objs[_F]=C;A.objs[_G]=D;A.change_state(gs.INGAME)
	def decorate_window(A):pg.display.set_icon(A.data.get_image('icon'));pg.display.set_caption('Passgoat','goat')
	def delete_scores(A):A.data.settings['scores'].clear()
	def create_objs(A):A.objs={};B=TextLabel('PASSGOAT',A.data.get_font(4),ColorGroup.LABEL).center(x=_A).move_to(y=40);C=TextLabel('mehhhhhhhhhhh',A.data.get_font(1),ColorGroup.CAPTION).center(x=_A).move_to(y=100);D=Image(A.data.get_image('goat')).move_to(-30,280);E=Button('Play',A.data.get_font(2),ColorGroup.BUTTON,A.play_game).center(x=_A).move_to(y=200);F=Button('Options',A.data.get_font(2),ColorGroup.BUTTON,A.change_state,gs.OPTIONS).center(x=_A).move_to(y=240);G=Button('Quit',A.data.get_font(2),ColorGroup.BUTTON_LESSER,A.quit_game).center(x=_A).move_to(y=280);A.objs[_H]=B;A.objs[_I]=C;A.objs[_J]=D;A.objs[_K]=E;A.objs[_L]=F;A.objs[_M]=G;B=TextLabel('OPTIONS',A.data.get_font(3),ColorGroup.LABEL).center(x=_A).move_to(y=40);C=Button('Save',A.data.get_font(2),ColorGroup.BUTTON_LESSER,A.change_settings).center(x=_A).move_to(y=300);D=Toggle('Hard Mode',A.data.get_font(2),ColorGroup.TOGGLE).center(x=_A).move_to(y=120);E=Counter('Number Count',A.data.get_font(2),ColorGroup.BUTTON,4,10).move_to(200,170);F=Button('Wipe Scores',A.data.get_font(2),ColorGroup.BUTTON,A.delete_scores).center(x=_A).move_to(y=220);A.objs[_N]=B;A.objs[_O]=C;A.objs[_B]=D;A.objs[_C]=E;A.objs[_P]=F;B=TextLabel('PAUSE',A.data.get_font(3),ColorGroup.LABEL).center(x=_A).move_to(y=40);C=Button('Resume',A.data.get_font(4),ColorGroup.BUTTON,A.change_state,gs.INGAME).center(x=_A).move_to(y=150);D=Button('Back to Title',A.data.get_font(2),ColorGroup.BUTTON_LESSER,A.change_state,gs.TITLE).center(x=_A).move_to(y=280);A.objs[_Q]=B;A.objs[_R]=C;A.objs[_S]=D;B=TextLabel('YOU GUESSED IT!',A.data.get_font(3),ColorGroup.LABEL).center(x=_A).move_to(y=40);A.objs[_T]=B;B=TextLabel('SCORES',A.data.get_font(3),ColorGroup.LABEL).center(x=_A).move_to(y=40);A.objs[_U]=B
	def handle_events(A):
		for B in pg.event.get():
			print(B)
			match B.type:
				case pg.QUIT:A.data.save_data();A.quit_game()
				case pg.KEYDOWN:
					if A.state==gs.INGAME:
						if B.key==27:A.change_state(gs.PAUSE)
						elif B.unicode in Passgoat.DIGITS:A.guess.append(B.unicode)
				case pg.WINDOWMINIMIZED|pg.WINDOWMOVED:
					if A.state==gs.INGAME:A.change_state(gs.PAUSE)
			for C in A.screen_objs:C.handle_event(B)
	def change_state(A,state):A.state=state;A.state_init=False
	def update(A):
		if not A.state_init:
			A.screen_objs.clear();A.dirty_rects.append(A.surface.get_rect());A.state_init=_A
			match A.state:
				case gs.TITLE:A.objs[_H].add_to(A.screen_objs);A.objs[_I].add_to(A.screen_objs);A.objs[_J].add_to(A.screen_objs);A.objs[_K].add_to(A.screen_objs);A.objs[_L].add_to(A.screen_objs);A.objs[_M].add_to(A.screen_objs)
				case gs.OPTIONS:A.objs[_N].add_to(A.screen_objs);A.objs[_O].add_to(A.screen_objs);A.objs[_B].add_to(A.screen_objs);A.objs[_B].set_toggle(A.data.settings[_E]);A.objs[_C].add_to(A.screen_objs);A.objs[_C].set_count(A.data.settings[_D]);A.objs[_P].add_to(A.screen_objs)
				case gs.INGAME:A.objs[_F].add_to(A.screen_objs);A.objs[_G].add_to(A.screen_objs)
				case gs.PAUSE:A.objs[_Q].add_to(A.screen_objs);A.objs[_R].add_to(A.screen_objs);A.objs[_S].add_to(A.screen_objs)
				case gs.END:A.objs[_T].add_to(A.screen_objs)
				case gs.SCORES:A.objs[_U].add_to(A.screen_objs)
		print(A.clock.get_fps())
		for C in A.screen_objs:
			B=C.update()
			if B:A.dirty_rects.extend(B)
	def change_settings(A):A.data.settings[_E]=A.objs[_B].get_toggle();A.data.settings[_D]=A.objs[_C].get_count();A.change_state(gs.TITLE)
	def generate_answer(B,mode):
		A=mode
		if A>5:B.answer=random.choices(Passgoat.DIGITS,k=A)
		else:B.answer=random.sample(Passgoat.DIGITS,A)
	def draw(A):
		A.surface.fill(col.WHITE)
		for B in A.screen_objs:B.draw(A.surface)
		pg.display.update(A.dirty_rects);A.clock.tick_busy_loop(420);A.dirty_rects.clear()
	def run(A):
		A.surface=pg.display.set_mode(A.SIZE,pg.SHOWN)
		while 1:A.handle_events();A.update();A.draw()
if __name__=='__main__':game=Passgoat();game.run()