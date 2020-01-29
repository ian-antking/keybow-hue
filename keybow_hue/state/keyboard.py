class Keyboard:
    def __init__(self, room):
        self.room = room
        self.keys = {
            0: {
                'action': room.dim,
                'color': lambda: [self.validate_brightness(room.get_state('bri') - 50)] * 3 if room.get_state('on') else [0] * 3
            },
            1: {
                'action': room.toggle_on_off,
                'color': lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0)
            },
            2: {
                'action': room.bright,
                'color': lambda: [self.validate_brightness(room.get_state('bri') + 50)] * 3 if room.get_state('on') else [0] * 3
            },
        }

    def validate_brightness(self, brightness):
        if brightness >= 255:
            return 255
        if brightness <= 0:
            return 0
        return brightness


if __name__ == '__main__':
    exit()
