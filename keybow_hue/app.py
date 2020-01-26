#!/usr/bin/env python
import keybow
import shutdown
import hue
import time
from dotenv import load_dotenv
import os

load_dotenv()

dimmer_keys = [1, 2]

@keybow.on()
def handle_key(index, state):

    if state:
        keybow.set_led(index, 0, 255, 0)
        keys[index]['action']()
    else:
        keybow.set_led(index, *keys[index]['color']())


if __name__ == '__main__':
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')
    room_name = os.getenv('ROOM_NAME')

    if not hue_token or not bridge_ip:
        keybow.set_all(255, 0, 0)
        print('No config')
    else:
        room = hue.Room(hue_token, bridge_ip, room_name)
        keys = {
            0: {
                'name': 'power',
                'action': room.toggle_on_off,
                'color': lambda: (0, 255, 0) if room.get_state('on') else (255, 0, 0)
            },
            1: {
                'name': 'dim',
                'action': room.dim,
                'color': lambda: (room.get_state('bri') - 50, room.get_state('bri') - 50, room.get_state('bri') - 50)
            },
            2: {
                'name': 'brighten',
                'action': room.brighten,
                'color': lambda: (room.get_state('bri') + 50, room.get_state('bri') + 50, room.get_state('bri') + 50)
            },
        }

    killer = shutdown.Detector()
    for key in keys:
        keybow.set_led(key, *keys[key]['color']())
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()