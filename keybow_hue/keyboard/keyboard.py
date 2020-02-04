class Keyboard:
    def __init__(self):
        self.keys = []

    def add_key(self, key):
        self.keys.append(key)

    def get_key(self, index):
        return [key for key in self.keys if key.index == index][0]


if __name__ == '__main__':
    exit()
