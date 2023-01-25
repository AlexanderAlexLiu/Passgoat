import random

class GameManager:
    def __init__(self) -> None:
        self.guess = []
        self.answer = []
    def gen_ans(self) -> None:
        self.ans = random.sample(list(range(10)), 4)