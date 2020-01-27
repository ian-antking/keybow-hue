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
        keybow.set_led(index, 0, 0, 255)
        keys[index]['action']()
    else:
        update_leds()

def update_leds():
    for key in keys:
        keybow.set_led(key, *keys[key]['color']() or [0] * 3)

def validate_brightness(brightness):
    if brightness >= 255:
        return 255
    if brightness <= 0:
        return 0
    return brightness

if __name__ == '__main__':
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')
    room_name = os.getenv('ROOM_NAME')

    if not hue_token or not bridge_ip or not room_name:
        keybow.set_all(255, 0, 0)
        print('No config')
    else:
        room = hue.Room(hue_token, bridge_ip, room_name)
        keys = {
            0: {
                'name': 'dim',
                'action': room.dim,
                'color': lambda: [validate_brightness(room.get_state('bri') - 50)] * 3 if room.get_state('on') else [0] * 3
            },
            1: {
                'name': 'power',
                'action': room.toggle_on_off,
                'color': lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0)
            },
            2: {
                'name': 'brighten',
                'action': room.brighten,
                'color': lambda: [validate_brightness(room.get_state('bri') + 50)] * 3 if room.get_state('on') else [0] * 3
            },
        }

    killer = shutdown.Detector()
    update_leds()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()