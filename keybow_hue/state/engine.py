class Engine:
    def __init__(self):
        self.mode = 0
        self.keyboards = []

    def get_keyboard(self):
        return self.keyboards[self.mode % len(self.keyboards)]

    def add_keyboard(self, keyboard):
        self.keyboards.append(keyboard)

    def change_mode(self):
        self.mode += 1
