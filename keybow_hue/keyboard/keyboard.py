class Keyboard:
    def __init__(self):
        self.keys = {}

    def add_key(self, key):
        self.keys[key.index] = {
            'action': key.action,
            'color': key.color
        }

    def get_key(self, index):
        return self.keys[index]


if __name__ == '__main__':
    exit()
