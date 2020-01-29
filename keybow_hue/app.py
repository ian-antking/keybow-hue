#!/usr/bin/env python
import keybow
import shutdown
import hue
import time
import config
import requests

@keybow.on()
def handle_key(index, state):

    if state:
        keybow.set_led(index, 0, 0, 255)
        keys[index]['action']()
    else:
        update_leds()

def update_leds():
    for key in keys:
        keybow.set_led(key, *keys[key]['color']())

def validate_brightness(brightness):
    if brightness >= 255:
        return 255
    if brightness <= 0:
        return 0
    return brightness

if __name__ == '__main__':
    env_vars = ['HUE_TOKEN', 'ROOM_NAME']
    conf = config.Env(env_vars)

    if not conf.env['HUE_TOKEN'] or not conf.env['ROOM_NAME']:
        keybow.set_all(255, 0, 0)
    else:
        room = hue.Room(conf.env['ROOM_NAME'], hue.Bridge(conf.env['HUE_TOKEN'], requests))
        keys = {
            0: {
                'action': room.dim,
                'color': lambda: [validate_brightness(room.get_state('bri') - 50)] * 3 if room.get_state('on') else [0] * 3
            },
            1: {
                'action': room.toggle_on_off,
                'color': lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0)
            },
            2: {
                'action': room.bright,
                'color': lambda: [validate_brightness(room.get_state('bri') + 50)] * 3 if room.get_state('on') else [0] * 3
            },
        }
        update_leds()

    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()