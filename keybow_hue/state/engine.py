class Engine:
    def __init__(self, keyboards=[]):
        self.mode = 0
        self.keyboards = keyboards

    def get_keyboard(self):
        return self.keyboards[self.mode % len(self.keyboards)]

    def change_mode(self):
        self.mode += 1
