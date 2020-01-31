#!/usr/bin/env python
from constants import DISCOVERY_URL

class App():
    def __init__(self, room, state, led_controller):
        try:
            self.room = room
            self.state = state
            self.led_controller = led_controller
            self.update_leds()
        except TypeError:
            self.led_controller.set_all(255, 0, 0)

    def update_leds(self):
        for key in self.state.keyboards[self.state.mode]:
            self.led_controller.set_led(key, *self.state.keyboards[self.state.mode][key].color())

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

    keyboard_one = [
        keyboard.Key(0, room.dim, lambda: [room.get_state('bri') - 50] * 3 if room.get_state('on') else [0] * 3),
        keyboard.Key(1, room.toggle_on_off, lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0)),
        keyboard.Key(2, room.bright, lambda: [room.get_state('bri') + 50] * 3 if room.get_state('on') else [0] * 3)
    ]

    state_engine = state.Engine([keyboard_one])
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
