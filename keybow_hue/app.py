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
        if index == 2:
            room.brighten()
        if index == 1:
            room.dim()
        if index == 0:
            room.toggle_on_off():
    else:
        keybow.set_led(index, room.brightness, room.brightness, room.brightness)


if __name__ == '__main__':
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')
    room_name = os.getenv('ROOM_NAME')

    if not hue_token or not bridge_ip:
        keybow.set_all(255, 0, 0)
        print('No config')
    else:
        room = hue.Room(hue_token, bridge_ip, room_name)
        keybow.set_led(2, room.brightness + 50, room.brightness + 50, room.brightness + 50)
        keybow.set_led(1, room.brightness - 50, room.brightness - 50, room.brightness - 50)

    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()