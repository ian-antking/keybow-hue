class Key:
    def __init__(self, index, action, color):
        self.index = index
        self.action = action
        self.color = color

    def execute_action(self):
        self.action()

    def get_color(self):
        return self.color()