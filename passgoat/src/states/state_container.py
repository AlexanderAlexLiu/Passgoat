class StateContainer:
    def __init__(self) -> None:
        self.children = []
    def add_to(self, on_screen_objs : list) -> None:
        on_screen_objs.extend(self.children)
    def placeholder(self, arg):
        print('PLACEHOLDER FOR: ' + arg)