#!/usr/bin/env python
from constants import DISCOVERY_URL

class App():
    def __init__(self, config_manager, hue_manager, led_controller):
        try:
            conf = config_manager.Env(['HUE_TOKEN', 'ROOM_NAME'])
            room_name = conf.env['ROOM_NAME']
            token = conf.env['HUE_TOKEN']
            self.led_controller = led_controller
            self.room = hue_manager.Room(room_name, hue_manager.Bridge(token, DISCOVERY_URL))
            self.keyboard = state.Keyboard(self.room)
            self.update_leds()
        except TypeError:
            self.led_controller.set_all(255, 0, 0)

    def update_leds(self):
        for key in self.keyboard.keys:
            self.led_controller.set_led(key, *self.keyboard.keys[key]['color']())

    def execute_action(self, index):
        app.keyboard.keys[index]['action']()

if __name__ == '__main__':
    import keybow
    import shutdown
    import hue
    import time
    import config
    import state
    
    app = App(config, hue, keybow)

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
