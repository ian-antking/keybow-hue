#!/usr/bin/env python
import keybow
import time
import shutdown
from dotenv import load_dotenv
import os

load_dotenv()

control_keys = [0, 3, 6, 9]

@keybow.on()
def handle_key(index, state):

    if state:
        keybow.set_led(index, 0, 255, 0)
    else:
        keybow.set_led(index, 0, 0, 0)


if __name__ == '__main__':
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')

    if not hue_token or not bridge_ip:
        keybow.setAll(255, 0, 0)
    else:
        for key in control_keys:
            keybow.set_led(key, 127, 127, 127)

    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()