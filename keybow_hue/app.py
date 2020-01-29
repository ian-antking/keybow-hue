#!/usr/bin/env python
import keybow
import shutdown
import hue
import time
import config
import interface
from constants import DISCOVERY_URL

@keybow.on()
def handle_key(index, state):

    if state:
        keybow.set_led(index, 0, 0, 255)
        keyboard.keys[index]['action']()
    else:
        update_leds()

def update_leds():
    for key in keyboard.keys:
        keybow.set_led(key, *keyboard.keys[key]['color']())

if __name__ == '__main__':
    try:
        conf = config.Env(['HUE_TOKEN', 'ROOM_NAME'])
        room = hue.Room(conf.env['ROOM_NAME'], hue.Bridge(conf.env['HUE_TOKEN'], DISCOVERY_URL))
        keyboard = interface.Keyboard(room)
        update_leds()
    except TypeError:
        keybow.set_all(255, 0, 0)

    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()
