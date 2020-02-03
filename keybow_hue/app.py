#!/usr/bin/env python
from constants import DISCOVERY_URL

class App():
    def __init__(self, room, state, led_controller):
        try:
            self.room = room
            self.state = state
            self.led_controller = led_controller
            self.update_leds()
        except TypeError as error:
            print(error)
            self.led_controller.set_all(255, 0, 0)

    def validate_brightness(self, brightness):
        if brightness >= 255:
            return 255
        if brightness <= 0:
            return 0
        return brightness

    def validate_color(self, color=[]):
        validated_color = []
        for value in color:
            validated_color.append(self.validate_brightness(value))
        return validated_color

    def update_leds(self):
        for key in self.state.keyboards[self.state.mode].keys:
            color = self.validate_color(self.state.keyboards[self.state.mode].keys[key]['color']())
            self.led_controller.set_led(key.index, *color)

    def execute_action(self, index):
        self.state.keyboards[self.state.mode][index].action()

if __name__ == '__main__':
    import keybow
    import keyboard
    import shutdown
    import hue
    import time
    import config
    import state
    
    conf = config.Env(['HUE_TOKEN', 'ROOM_NAME'])
    room = hue.Room(conf.env['ROOM_NAME'], hue.Bridge(conf.env['HUE_TOKEN'], DISCOVERY_URL))

    keyboard_one = keyboard.Keyboard()
    keyboard_one.add_key(keyboard.Key(0, room.dim, lambda: [room.get_state('bri') - 50] * 3 if room.get_state('on') else [0] * 3))
    keyboard_one.add_key(keyboard.Key(1, room.toggle_on_off, lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0)))
    keyboard_one.add_key(keyboard.Key(2, room.bright, lambda: [room.get_state('bri') + 50] * 3 if room.get_state('on') else [0] * 3))
    

    state_engine = state.Engine()
    state_engine.add_keyboard(keyboard_one)
    app = App(hue, state_engine, keybow)

    @keybow.on()
    def handle_key(index, state):

        if state:
            keybow.set_led(index, 0, 0, 255)
            app.execute_action(index)
        else:
            app.update_leds()


    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()
