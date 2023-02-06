from modules.containers.container import Container
from modules.objs.button import Button
from modules.objs.toggle import Toggle
from modules.objs.textlabel import TextLabel
from modules.objs.counter import Counter
from modules.objs.specialbutton import SpecialButton
import modules.objs.colorgroups as ColorGroups
from modules.data import GameData
from typing import Callable
from modules.game_states import GameStates
import random
import pygame as pg

class InGame(Container):
    DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    def __init__(self, data : GameData, change_state : Callable, win_con : Callable) -> None:
        super().__init__()
        self.data, self.change_state = data, change_state
        self.win_func = win_con
        self.answer_label = TextLabel('', self.data.get_font(3), ColorGroups.LABEL)
        self.guess_count_label = TextLabel('', self.data.get_font(1), ColorGroups.LABEL)
        self.number_tickers = [Toggle(str(i), self.data.get_font(2), ColorGroups.TICKER) for i in range(10)]
        self.guess_output_label = TextLabel('', self.data.get_font(1), ColorGroups.LABEL)
        self.move_tickers()
    def gen_answer(self) -> None:
        if self.mode > 5:
            self.answer = random.choices(InGame.DIGITS, k=self.mode)
        else:
            self.answer = random.sample(InGame.DIGITS, k=self.mode)
    def reset_game(self) -> None:
        self.hard, self.mode = self.data.get_setting('hard'), self.data.get_setting('mode')
        self.answer = []
        self.guess_output_label.set_text('Make a guess').center(x=True).move(y=240)
        self.gen_answer()
        self.allow_input = True
        self.guess_slots = [SpecialButton('_', self.data.get_font(2), ColorGroups.SPECIAL, self.deny_input) for i in range(self.mode)]
        self.move_slots()
        self.guess_count = 0
        self.guess_count_label.set_text(f'GUESSES: {self.guess_count}').center(x=True).move(y=20)
        self.children.clear()
        if not self.hard:
            self.children.extend(self.number_tickers)
        self.children.append(self.answer_label)
        self.children.append(self.guess_output_label)
        self.children.extend(self.guess_slots)
        self.children.append(self.guess_count_label)
        self.reset_tickers()
        self.answer_label.set_text(' '.join('_' for i in range(self.data.get_setting('mode'))))
        self.move_answer_label()
        print(self.answer)
    def get_guess(self) -> list[str]:
        guess = []
        for slot in self.guess_slots:
            if slot.get_lock() or (slot.get_text() != '_' and not slot.ghosted):
                guess.append(slot.get_text())
            else:
                guess.append(None)
        return guess
    def move_answer_label(self) -> None:
        self.answer_label.center(x=True).move(y=40)
    def deny_input(self) -> None:
        self.allow_input = False
    def make_guess(self) -> None:
        self.guess_count+=1
        if self.answer == self.get_guess():
            self.win_func(self.guess_count, self.get_guess())
        else:
            correct, right_place = 0, 0
            if self.mode > 5:
                # ADD FOR THIS
                pass
            else:
                for i, string in enumerate(self.get_guess()):
                    if string in self.answer:
                        correct+=1
                        if self.answer.index(string) == i:
                            correct-=1
                            right_place+=1
            self.guess_count_label.set_text(f'GUESSES: {self.guess_count}').center(x=True).move(y=20)
            self.guess_count_label.set_dirty(True)
            self.guess_output_label.set_text(f'{correct} in answer, {right_place} in place').center(x=True)
            self.guess_output_label.set_dirty(True)
            # add to scrollable
    def handle_event(self, event: pg.event.Event) -> None:
        match event.type:
            case pg.WINDOWMOVED | pg.WINDOWMINIMIZED:
                self.change_state(GameStates.PAUSE)
            case pg.KEYDOWN:
                if event.key == 27:
                    self.change_state(GameStates.PAUSE)
                elif event.key == 8:
                    last_index = -1
                    for i, string in enumerate(self.get_guess()):
                        if string != None and not self.guess_slots[i].get_lock():
                            last_index = i
                    print(f"LAST INDEX {last_index}")
                    if last_index != -1:
                        if self.guess_slots[last_index].ghost_value != '':
                            self.guess_slots[last_index].set_text(self.guess_slots[i])
                            self.guess_slots[last_index].ghosted = True
                        else:
                            self.guess_slots[last_index].set_text('_')
                        self.guess_slots[last_index].set_dirty()
                elif event.key == 13:
                    if None not in self.get_guess():
                        self.make_guess()
                        for slot in self.guess_slots:
                            if slot.ghost_value != '':
                                slot.set_text(slot.ghost_value)
                                slot.ghosted = True
                            else:
                                if not slot.get_lock():
                                    slot.set_text('_')
                            slot.set_dirty(True)
                elif event.unicode.isnumeric():
                    if self.mode > 5:
                        super().handle_event(event)
                        if self.allow_input:
                            for i, string in enumerate(self.get_guess()):
                                if string == None:
                                    self.guess_slots[i].set_text(event.unicode)
                                    if self.guess_slots[i].ghosted:
                                        self.guess_slots[i].ghosted = False
                                    self.guess_slots[i].set_dirty()
                                    break
                        else:
                            self.allow_input = True
                    else:
                        if event.unicode not in self.get_guess():
                            super().handle_event(event)
                            if self.allow_input:
                                for i, string in enumerate(self.get_guess()):
                                    if string == None:
                                        self.guess_slots[i].set_text(event.unicode)
                                        if self.guess_slots[i].ghosted:
                                            self.guess_slots[i].ghosted = False
                                        self.guess_slots[i].set_dirty()
                                        break
                            else:
                                self.allow_input = True
                elif event.key == 32:
                    super().handle_event(event)
            case _:
                super().handle_event(event)
    def reset_tickers(self) -> None:
        for ticker in self.number_tickers:
            ticker.set_toggle(False)
    def move_slots(self) -> None:
        slot_width = self.guess_slots[0].rect.w
        slot_spacing = 10
        slots_width = slot_width * self.mode + slot_spacing * (self.mode-1)
        slots_start_x = (800 - slots_width) / 2
        slots_y = 200
        for i, slot in enumerate(self.guess_slots):
            slot.move(x=slots_start_x+(slot_width+slot_spacing)*i, y=slots_y)
    def move_tickers(self) -> None:
        ticker_width = self.number_tickers[0].rect.w
        ticker_spacing = 10
        tickers_width = ticker_width * 10 + ticker_spacing * 9
        tickers_start_x = (800 - tickers_width) / 2
        tickers_y = 300
        for i, ticker in enumerate(self.number_tickers):
            ticker.move(x=tickers_start_x+(ticker_width+ticker_spacing)*i, y=tickers_y)