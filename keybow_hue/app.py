#!/usr/bin/env python
import keybow
import shutdown
import hue
import time
import config
import interface
from constants import DISCOVERY_URL

class App():
    def __init__(self, config_manager, hue_manager):
        try:
            conf = config.Env(['HUE_TOKEN', 'ROOM_NAME'])
            self.room = hue.Room(conf.env['ROOM_NAME'], hue.Bridge(conf.env['HUE_TOKEN'], DISCOVERY_URL))
            self.keyboard = interface.Keyboard(self.room)
            self.update_leds()
        except TypeError:
            keybow.set_all(255, 0, 0)

    def update_leds(self):
        for key in self.keyboard.keys:
            keybow.set_led(key, *self.keyboard.keys[key]['color']())

if __name__ == '__main__':
    app = App(config, hue)

    @keybow.on()
    def handle_key(index, state):

        if state:
            keybow.set_led(index, 0, 0, 255)
            app.keyboard.keys[index]['action']()
        else:
            app.update_leds()

    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()
