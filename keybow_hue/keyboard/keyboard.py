class Keyboard:
    def __init__(self):
        self.keys = {}

    def validate_brightness(self, brightness):
        if brightness >= 255:
            return 255
        if brightness <= 0:
            return 0
        return brightness

    def add_key(self, key):
        self.keys[key['index']] = {
            'action': key['action'],
            'color': key['color']
        }


if __name__ == '__main__':
    exit()
