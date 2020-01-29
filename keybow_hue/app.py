#!/usr/bin/env python
from constants import DISCOVERY_URL

class App():
    def __init__(self, conf, hue_manager, state_manager):
        room_name = conf.env['ROOM_NAME']
        hue_token = conf.env['HUE_TOKEN'],

        self.room = hue_manager.Room(
            room_name,
            hue_manager.Bridge(
                hue_token,
                DISCOVERY_URL
            )
        )
        self.state = state_manager.Keyboard(self.room)

    def update_leds(self, led_handler):
        for key in self.state.keys:
            led_handler(key, *self.state.keys[key]['color']())

    def execute_action(self, index):
        self.state.keys[index]['action']()


if __name__ == '__main__':
    import keybow
    import shutdown
    import hue
    import time
    import config
    import state

    try: 
        conf = config.Env(['HUE_TOKEN', 'ROOM_NAME'])
    except TypeError:
        keybow.set_all(255, 0, 0)
        print(TypeError)
        time.sleep(30)
        exit()
    
    app = App(conf, hue, state)
    app.update_leds(keybow.set_led)

    @keybow.on()
    def handle_key(index, state):

        if state:
            keybow.set_led(index, 0, 0, 255)
            app.execute_action(index)
        else:
            app.update_leds(keybow.set_led)

    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()
